# LoyaltiesMembersTransfersCreateResponseBodyValidityTimeframe

Set recurrent time periods when the voucher is valid. For example, valid for 1 hour every other day.start_date required when including the validity_timeframe.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** | Defines the amount of time the voucher will be active in ISO 8601 format. For example, a voucher with a duration of PT1H will be valid for a duration of one hour. | [optional] 
**duration** | **str** | Defines the intervening time between two time points in ISO 8601 format, expressed as a duration. For example, a voucher with an interval of P2D will be active every other day. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


