# LoyaltiesMembersBalanceUpdateResponseBody

Response schema for **POST** `/loyalties/members/{memberId}/balance` and for **POST** `/loyalties/{campaignId}/members/{memberId}/balance`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** | The incremental points removed or added to the current balance on the loyalty card. | 
**total** | **int** | The total of points accrued over the lifetime of the loyalty card. | 
**balance** | **int** | The balance after adding/removing points. | 
**type** | **str** | The type of voucher being modified. | 
**object** | **str** | The type of object represented by JSON. Default is balance. | [default to 'balance']
**related_object** | [**LoyaltiesMembersBalanceUpdateResponseBodyRelatedObject**](LoyaltiesMembersBalanceUpdateResponseBodyRelatedObject.md) |  | 
**operation_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


