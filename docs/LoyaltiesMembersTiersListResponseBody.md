# LoyaltiesMembersTiersListResponseBody

Response body schema for **GET** `/loyalties/members/{memberId}/tiers`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about loyalty tiers in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of loyalty tier objects. | [default to 'data']
**data** | [**List[LoyaltyTier]**](LoyaltyTier.md) |  | 
**total** | **int** | Total number of loyalty tier objects. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


