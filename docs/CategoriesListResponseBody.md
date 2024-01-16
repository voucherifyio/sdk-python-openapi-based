# CategoriesListResponseBody

Response body schema for **GET** `/categories`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about categories in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of category objects. | [default to 'data']
**data** | [**List[Category]**](Category.md) |  | 
**total** | **int** | Total number of categories. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


