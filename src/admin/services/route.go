package services

import (
	"log"

	"pks.pyfreebilling.com/models"
	"pks.pyfreebilling.com/utils/filters"
)

// Route Service
var (
	RouteService routeServiceInterface = &routeService{}
)

type routeService struct{}

type routeServiceInterface interface {
	GetRoute(id int64) (*models.Route, error)
	CreateRoute(models.Route) (*models.Route, error)
	UpdateRoute(models.Route) (*models.Route, error)
	DeleteRoute(id int64) error
	GetRoutes(filter filters.Filters) (*models.Routes, *filters.Pagination, error)
}

// GetRoute gets the route object by id
func (s *routeService) GetRoute(id int64) (*models.Route, error) {
	var route models.Route
	if err := models.GetRoute(&route, id); err != nil {
		return nil, err
	}

	return &route, nil
}

// CreateRoute saves the route object and returns the saved object
func (s *routeService) CreateRoute(route models.Route) (*models.Route, error) {
	if err := models.CreateRoute(&route); err != nil {
		return nil, err
	}

	return &route, nil
}

// UpdateRoute updates the route object and returns the updated object
func (s *routeService) UpdateRoute(route models.Route) (*models.Route, error) {
	if err := models.UpdateRoute(&route); err != nil {
		return nil, err
	}

	return &route, nil
}

// DeleteRoute deletes the route object by id
func (s *routeService) DeleteRoute(id int64) error {
	if err := models.DeleteRoute(id); err != nil {
		return err
	}

	return nil
}

// GetRoutes gets the list of routes
func (s *routeService) GetRoutes(filter filters.Filters) (*models.Routes, *filters.Pagination, error) {
	// Count the number of routes
	routeCount, err := models.CountRoutes()
	if err != nil {
		return nil, nil, err
	}
	// get Pagnition informations
	p, paginateErr := filters.Paginate(filter.Page, int(routeCount), filter.PageSize)
	if paginateErr != nil {
		log.Printf("Error in pagination: %v", paginateErr)
		return nil, nil, paginateErr
	}

	// Gather the routes
	var routes models.Routes
	if err := models.GetRoutes(&routes, filter); err != nil {
		return nil, nil, err
	}

	return &routes, p, nil

}
