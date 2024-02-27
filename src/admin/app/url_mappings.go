package app

import (
	"net/http"

	"github.com/gin-gonic/gin"
	swaggerFiles "github.com/swaggo/files"     // swagger embed files
	ginSwagger "github.com/swaggo/gin-swagger" // gin-swagger middleware
	"pks.pyfreebilling.com/controllers"
	_ "pks.pyfreebilling.com/docs"
)

// mapUrls function lists the project urls
func mapUrls() {
	api := r.Group("v1")

	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "home.html", gin.H{})
	})

	gw := r.Group("gateways")
	gw.GET("", controllers.GetGateways)
	gw.GET("/new", controllers.CreateGatewayGet)
	gw.POST("/new", controllers.CreateGateway)
	gw.GET("/:id", controllers.GetGatewayByID)
	gw.DELETE("/:id", controllers.DeleteGateway)

	// Handle the gateway's routes
	gr := api.Group("gateways")
	{
		gr.GET("", controllers.GetGateways)
		gr.POST("", controllers.CreateGateway)
		gr.GET("/:id", controllers.GetGatewayByID)
		gr.PUT("/:id", controllers.UpdateGateway)
		gr.DELETE("/:id", controllers.DeleteGateway)
	}

	routes := r.Group("routes")
	routes.GET("", controllers.GetRoutes)
	routes.POST("/new", controllers.CreateRoute)
	// routes.GET("/:id", controllers.GetRouteByID)
	// routes.DELETE("/:id", controllers.DeleteRoute)

	// Handle the route's routes
	rr := api.Group("routes")
	{
		rr.GET("", controllers.GetRoutes)
		rr.POST("", controllers.CreateRoute)
		// rr.GET("/:id", controllers.GetRouteByID)
		// rr.PUT("/:id", controllers.UpdateRoute)
		// rr.DELETE("/:id", controllers.DeleteRoute)
	}

	// Handle health route
	api.GET("/health", controllers.HealthCheck)

	//Register handler for Swagger
	r.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))
}
