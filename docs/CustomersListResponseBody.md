# CustomersListResponseBody

Response body schema for **GET** `/customers`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about customers in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of customer objects. | [default to 'customers']
**customers** | [**List[CustomerWithSummaryLoyaltyReferrals]**](CustomerWithSummaryLoyaltyReferrals.md) | Contains array of customer objects. | 
**total** | **int** | Total number of customers. | 
**has_more** | **bool** | As query results are always limited (by the limit parameter), the &#x60;has_more&#x60; flag indicates whether there are more records for given filter parameters. This let&#39;s you know if you are able to run another request (with a different end date filter) to get more records returned in the results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


