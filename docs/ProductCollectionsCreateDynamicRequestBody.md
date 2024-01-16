# ProductCollectionsCreateDynamicRequestBody

Response body schema for **POST** `/product-collections`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Show that the product collection is dynamic (products come in and leave based on set criteria). | [default to 'AUTO_UPDATE']
**name** | **str** | Unique user-defined product collection name. | 
**filter** | [**ProductCollectionsCreateDynamicRequestBodyFilter**](ProductCollectionsCreateDynamicRequestBodyFilter.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


