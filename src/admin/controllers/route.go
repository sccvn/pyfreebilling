package controllers

import (
	"fmt"
	"log"
	"net/http"
	"strconv"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/go-playground/validator/v10"
	"pks.pyfreebilling.com/models"
	"pks.pyfreebilling.com/services"      // Import the missing package
	"pks.pyfreebilling.com/utils/filters" // Import the missing package
)

// GetRoutes godoc
//
//	@Summary		Get a paginated list of routes
//	@Description	Responds with the list of routes as JSON.
//	@Tags			routes
//	@Produce		json
//	@Param			page		query		int		false	"int valid"		minimum(1)												maximum(10000000)	default(1)
//	@Param			page_size	query		int		false	"int valid"		minimum(5)												maximum(100)		default(5)
//	@Param			sort		query		string	false	"string enums"	Enums(id, name, ip_address, -id, -name, -ip_address)	default(id)
//	@Success		200			{object}	utils.PaginatedResponseHTTP{data=models.Routes}
//	@Error			400 {object} utils.ResponseErrorHTTP{}
//	@Error			404 {object} utils.ResponseErrorHTTP{}
//	@Failure		500	{object}	utils.ResponseErrorHTTP{}
//	@Router			/routes [get]
func GetRoutes(c *gin.Context) {
	// implementation goes here
	var filter filters.Filters
	if err := c.ShouldBindQuery(&filter); err != nil {
		fmt.Printf("Invalid Input: %v", err.Error())
		c.JSON(http.StatusBadRequest, gin.H{
			"error":   true,
			"message": "Invalid inputs. Please check your inputs",
		})
		return
	}
	fmt.Printf("Filter OK: %v", filter)
	filter.Sort = filter.GetSort()
	filter.SortSafelist = []string{"id", "did", "-id", "-did"}
	fmt.Printf("Filter OK: %v", filter)

	routes, p, err := services.RouteService.GetRoutes(filter)
	if err != nil {
		fmt.Printf("Error: %v", err.Error())
		c.JSON(http.StatusInternalServerError, gin.H{
			"error":   true,
			"message": "Internal server error",
		})
		return
	}
	switch c.Request.Header.Get("Accept") {
	case "application/json":
		c.JSON(http.StatusOK, gin.H{
			"error":      false,
			"messages":   "Routes list",
			"data":       routes,
			"pagination": p,
		})
	default:
		c.HTML(http.StatusOK, "routes.html", gin.H{
			"title":      "Route List",
			"routes":     routes,
			"pagination": p,
		})
	}
}

// CreateRoute godoc
//
//	@Summary		Create a new route
//	@Description	Create a new route JSON and stors in DB. Return saved JSON
//	@Tags			routes
//	@Accept			json
//	@Produce		json
//	@Param			route	body		models.Route	true	"Route object"
//	@Success		201		{object}	models.Route
//	@Failure		400		{object}	utils.ResponseErrorHTTP
//	@Failure		500		{object}	utils.ResponseErrorHTTP
//	@Router			/routes [post]
func CreateRoute(c *gin.Context) {
	// implementation goes here
	var route models.Route

	switch c.Request.Header.Get("Accept") {
	case "application/json":
		if err := c.ShouldBindJSON(&route); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{
				"error":   true,
				"message": "Invalid inputs. Please check your inputs",
			})
			return
		}
	default:
		if err := c.ShouldBind(&route); err != nil {
			verrs := err.(validator.ValidationErrors)
			messages := make([]string, len(verrs))
			for i, verr := range verrs {
				messages[i] = fmt.Sprintf("%s: %s", verr.Field(), verr.Tag())
			}
			c.JSON(http.StatusBadRequest, gin.H{
				"error":   true,
				"message": "Invalid inputs. Please check your inputs",
			})
			return
		}
	}
	route.CreatedAt = time.Now()

	newRoute, savErr := services.RouteService.CreateRoute(route)
	if savErr != nil {
		fmt.Printf("error in creating route: %s", savErr)
		switch c.Request.Header.Get("Accept") {
		case "application/json":
			c.JSON(http.StatusInternalServerError, gin.H{
				"error":   true,
				"message": "Error in creating Route",
			})
			return
		default:
			if strings.Contains(fmt.Sprint(savErr), "UNIQUE constraint failed") {
				log.Printf("DB duplicate key : %v", savErr)
				c.HTML(http.StatusBadRequest, "routes/routes.html",
					gin.H{"error": "Unique constraint failed"})
				return
			}
			c.HTML(http.StatusBadRequest, "",
				gin.H{"error": "Unexpected error when saving in DB"})
			return
		}
	}

	c.Header("Location", c.FullPath()+"/"+strconv.Itoa(int(newRoute.ID)))

	switch c.Request.Header.Get("Accept") {
	case "application/json":
		c.JSON(http.StatusCreated, gin.H{
			"error":   false,
			"message": "Route created successfully",
			"data":    newRoute,
		})
	default:
		c.HTML(http.StatusCreated, "routes/new.html", newRoute)
	}
}
