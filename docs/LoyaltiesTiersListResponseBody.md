# LoyaltiesTiersListResponseBody

Response body schema for **GET** `/loyalties/{campaignId}/tiers`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about loyalty tiers in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of loyalty tier objects. | [default to 'data']
**data** | [**List[LoyaltyTier]**](LoyaltyTier.md) | This is an object representing a loyalty tier. Loyalty tiers are used to create a loyalty program with different levels of membership and varied earning rules and rewards based on customer’s tiers. | 
**total** | **int** | Total number of loyalty tier objects. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


