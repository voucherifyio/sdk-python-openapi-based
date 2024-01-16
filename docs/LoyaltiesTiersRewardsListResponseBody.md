# LoyaltiesTiersRewardsListResponseBody

Response body schema for **GET** `/loyalties/{campaignId}/tiers/{loyaltyTierId}/rewards`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about loyalty tier rewards in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of loyalty tier reward objects. | [default to 'data']
**data** | [**List[LoyaltiesLoyaltyTierReward]**](LoyaltiesLoyaltyTierReward.md) | Contains array of loyalty tier reward objects. | 
**total** | **int** | Total number of loyalty tier reward objects. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


