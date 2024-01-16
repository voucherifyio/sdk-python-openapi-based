# ProductCollectionsProductsList

Response body schema for **GET** /product-collections/{productCollectionID}/products.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about products and SKUs. | [default to 'list']
**data_ref** | **str** | Identifies the name of the JSON property that contains the array of products and SKUs. | [default to 'data']
**data** | [**List[ProductCollectionsProductsListProductsItem]**](ProductCollectionsProductsListProductsItem.md) | A dictionary that contains an array of products and SKUs. | 
**total** | **int** | Total number of products &amp; SKUs in the product collection. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


