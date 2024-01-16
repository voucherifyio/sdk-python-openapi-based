# ProductCollectionsCreateResponseBody

Response body schema for **POST** `/product-collections`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product collection ID. | 
**name** | **str** | Unique user-defined product collection name. | 
**type** | **str** | Describes whether the product collection is dynamic (products come in and leave based on set criteria) or static (manually selected products). | 
**filter** | [**ProductCollectionsCreateDynamicRequestBodyFilter**](ProductCollectionsCreateDynamicRequestBodyFilter.md) |  | [optional] 
**products** | [**List[ProductCollectionsItemProductsItem]**](ProductCollectionsItemProductsItem.md) | Defines a set of products for a &#x60;STATIC&#x60; product collection type. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the product collection was created in ISO 8601 format. | 
**object** | **str** | The type of object represented by JSON. This object stores information about the static product collection. | [default to 'products_collection']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


