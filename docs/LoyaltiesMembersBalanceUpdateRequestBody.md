# LoyaltiesMembersBalanceUpdateRequestBody

Request Body schema for **post** `/loyalties/members/{memberId}/balance` and **POST** `/loyalties/{campaignId}/members/{memberId}/balance`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** | Incremental balance to be added to/subtracted from the loyalty card.  - To add points: 100 - To subtract points, add a minus: -100 | 
**expiration_type** | [**PointsExpirationTypes**](PointsExpirationTypes.md) |  | [optional] 
**expiration_date** | **datetime** | Set expiration date for added points, i.e. &#x60;YYYY-MM-DD&#x60;. This parameter is required only when expiration_type is set to &#x60;CUSTOM_DATE&#x60;. | [optional] 
**reason** | **str** | Reason for the transfer. | [optional] 
**source_id** | **str** | The merchant’s transaction ID if it is different from the Voucherify transaction ID. It is really useful in case of an integration between multiple systems. It can be a transaction ID from a CRM system, database or 3rd-party service. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


