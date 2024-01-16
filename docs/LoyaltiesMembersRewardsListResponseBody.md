# LoyaltiesMembersRewardsListResponseBody

Response body schema for **GET** `/loyalties/members/{memberId}/rewards`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of loyalty reward objects. | [default to 'data']
**data** | [**List[LoyaltiesMembersRewardsListResponseBodyDataItem]**](LoyaltiesMembersRewardsListResponseBodyDataItem.md) | Contains array of loyalty reward objects. | 
**total** | **int** | Total number of loyalty reward objects. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


