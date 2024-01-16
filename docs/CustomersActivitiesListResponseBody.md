# CustomersActivitiesListResponseBody

Request body schema for **GET** `/customers/{customerId}/activities`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about customer activities in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of customer activity objects. | [default to 'data']
**data** | [**List[CustomerActivity]**](CustomerActivity.md) | Array of customer activity objects. | 
**total** | **int** | Total number of customer activities. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


