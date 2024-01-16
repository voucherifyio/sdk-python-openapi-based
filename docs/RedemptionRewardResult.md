# RedemptionRewardResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**assignment_id** | **str** | Unique reward assignment ID assigned by Voucherify. | [optional] 
**voucher** | [**RedemptionRewardResultVoucher**](RedemptionRewardResultVoucher.md) |  | [optional] 
**product** | [**RedemptionRewardResultProduct**](RedemptionRewardResultProduct.md) |  | [optional] 
**sku** | [**RedemptionRewardResultSku**](RedemptionRewardResultSku.md) |  | [optional] 
**loyalty_tier_id** | **str** | Unique loyalty tier ID assigned by Voucherify. | [optional] 
**id** | **str** | Unique reward ID. | [optional] 
**name** | **str** | Name of the reward. | [optional] 
**object** | **str** | The type of object represented by the JSON | [optional] [default to 'reward']
**created_at** | **datetime** | Timestamp representing the date and time when the redemption was created in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp in ISO 8601 format indicating when the reward was updated. | [optional] 
**parameters** | [**RedemptionRewardResultParameters**](RedemptionRewardResultParameters.md) |  | [optional] 
**type** | **str** | Reward type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


