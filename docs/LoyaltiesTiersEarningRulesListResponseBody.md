# LoyaltiesTiersEarningRulesListResponseBody

Response body schema for **GET** `/loyalties/{campaignId}/tiers/{loyaltyTierId}/earning-rules`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about earning rules in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of earning rule objects. | [default to 'data']
**data** | [**List[EarningRule]**](EarningRule.md) | Contains array of earning rule objects. | 
**total** | **int** | Total number of earning rule objects. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


