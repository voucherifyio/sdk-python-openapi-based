# ExportsListResponseBody

Response body schema for **GET** `/exports`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about exports. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of exports. | [default to 'exports']
**exports** | [**List[Export]**](Export.md) | An array of export objects. | 
**total** | **int** | Total number of exports. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


