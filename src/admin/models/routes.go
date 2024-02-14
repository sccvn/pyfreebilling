package models

import (
	"log"
	"time"

	"pks.pyfreebilling.com/utils/filters"
)

type GetRouteRequest struct {
	ID int64 `uri:"id" binding:"required,min=1"`
}

// Route is the main route model
type Route struct {
	ID        int64      `json:"id" gorm:"primarykey"`
	CreatedAt time.Time  `json:"created_at,"`
	UpdatedAt time.Time  `json:"updated_at"`
	DID       string     `form:"did" json:"did" binding:"required" gorm:"unique,not null:true"`
	Gateways  *[]Gateway `json:",omitempty" gorm:"foreignKey:ID;constraint:OnUpdate:CASCADE,OnDelete:SET NULL;"`
}

// Routes represents many routes
type Routes []Route

// GetRoute by ID
func GetRoute(route *Route, id int64) error {
	// implementation goes here
	if err := DB.Take(&route, id).Error; err != nil {
		return err
	}
	return nil
}

// GetRoutes queries the DB to find routes with offset and limit
func GetRoutes(routes *Routes, filter filters.Filters) error {
	// implementation goes here
	sortOrder, err := filter.SortOrder()
	if err != nil {
		sortOrder = "id"
	}
	if err := DB.Limit(filter.Limit()).Offset(filter.Offset()).Order(sortOrder).Find(&routes).Error; err != nil {
		return err
	}
	return nil
}

// CountRoutes counts routes in DB
func CountRoutes() (int64, error) {
	// implementation goes here
	var routeCount int64
	if err := DB.Table("routes").Count(&routeCount).Error; err != nil {
		return 0, err
	}
	log.Printf("Items count : %v", routeCount)
	return routeCount, nil
}

// CreateRoute creates a new route
func CreateRoute(route *Route) error {
	// implementation goes here
	if req := DB.Create(&route); req.Error != nil {
		return req.Error
	}
	return nil
}

// UpdateRoute updates a route
func UpdateRoute(route *Route) error {
	// implementation goes here
	if err := DB.Save(&route).Error; err != nil {
		return err
	}
	return nil
}

// DeleteRoute deletes a route
func DeleteRoute(id int64) error {
	// implementation goes here
	if err := DB.Delete(&Route{}, id).Error; err != nil {
		return err
	}
	return nil
}

// FindRouteByDID finds a route by DID
func FindRouteByDID(did string) (*Route, error) {
	// implementation goes here
	route := &Route{}
	err := DB.Where("did = ?", did).First(&route).Error
	if err != nil {
		return nil, err
	}
	return route, nil
}

// FindRouteByDIDAndGateway finds a route by DID and Gateway
func FindRouteByDIDAndGateway(did string, gatewayID int64) (*Route, error) {
	// implementation goes here
	route := &Route{}
	err := DB.Where("did = ? AND gateway_id = ?", did, gatewayID).First(&route).Error
	if err != nil {
		return nil, err
	}
	return route, nil
}
