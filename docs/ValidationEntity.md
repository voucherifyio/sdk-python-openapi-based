# ValidationEntity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique validation id. | [optional] 
**session_id** | **str** | Unique session id. | [optional] 
**status** | **str** | The validation status | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the validation was created in ISO 8601 format. | [optional] 
**customer_id** | **str** | Unique customer ID of the customer making the purchase. | [optional] 
**redeemables** | [**List[ValidationsRedeemableApplicable]**](ValidationsRedeemableApplicable.md) | Lists validation results of each redeemable. | [optional] 
**skipped_redeemables** | [**List[ValidationsRedeemableInapplicable]**](ValidationsRedeemableInapplicable.md) | Lists validation results of each redeemable. | [optional] 
**inapplicable_redeemables** | [**List[ValidationsRedeemableSkipped]**](ValidationsRedeemableSkipped.md) | Lists validation results of each redeemable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


