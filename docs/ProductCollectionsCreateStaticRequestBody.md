# ProductCollectionsCreateStaticRequestBody

Response body schema for **POST** `/product-collections`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Show that the product collection is static (manually selected products). | [default to 'STATIC']
**name** | **str** | Unique user-defined product collection name. | 
**products** | [**List[ProductCollectionsCreateDynamicRequestBodyProductsItem]**](ProductCollectionsCreateDynamicRequestBodyProductsItem.md) | Defines a set of products for a &#x60;STATIC&#x60; product collection type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


