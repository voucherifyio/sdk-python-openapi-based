# ValidationsValidatePartialResponseBody

Response body schema for POST `/validations` where at least one promotion must be valid

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | The result of the validation. It takes all of the redeemables into account and returns a &#x60;false&#x60; if at least one redeemable is inapplicable. Returns &#x60;true&#x60; if all redeemables are applicable. | 
**redeemables** | [**List[ValidationsRedeemableApplicable]**](ValidationsRedeemableApplicable.md) | Lists validation results of each redeemable. If a redeemable can be applied, the API returns &#x60;\&quot;status\&quot;: \&quot;APPLICABLE\&quot;&#x60;. | 
**inapplicable_redeemables** | [**List[ValidationsRedeemableInapplicable]**](ValidationsRedeemableInapplicable.md) | Lists validation results of each inapplicable redeemable. | 
**order** | [**OrderCalculated**](OrderCalculated.md) |  | [optional] 
**tracking_id** | **str** | Hashed customer source ID. | [optional] 
**session** | [**Session**](Session.md) |  | [optional] 
**application_mode** | **str** |  | [default to 'PARTIAL']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


