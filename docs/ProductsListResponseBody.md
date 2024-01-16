# ProductsListResponseBody

Response body schema for **GET** `/products`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about products in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of product objects. | [default to 'products']
**products** | [**List[Product]**](Product.md) | Contains array of product objects. | 
**total** | **int** | Total number of product objects. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


