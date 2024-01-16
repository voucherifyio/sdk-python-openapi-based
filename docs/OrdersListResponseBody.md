# OrdersListResponseBody

Response body schema representing **GET** `/orders`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about orders in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of order objects. | [default to 'orders']
**orders** | [**List[OrderCalculatedNoCustomerData]**](OrderCalculatedNoCustomerData.md) | Contains array of order objects. | 
**total** | **int** | Total number of orders. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


