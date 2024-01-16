# SimpleRedemptionRewardResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**assignment_id** | **str** | Unique reward assignment ID assigned by Voucherify. | [optional] 
**voucher** | [**SimpleVoucher**](SimpleVoucher.md) |  | [optional] 
**product** | [**SimpleProduct**](SimpleProduct.md) |  | [optional] 
**sku** | [**SimpleSku**](SimpleSku.md) |  | [optional] 
**loyalty_tier_id** | **str** | Unique loyalty tier ID assigned by Voucherify. | [optional] 
**id** | **str** | Unique reward ID, assigned by Voucherify. | [optional] 
**object** | **str** | The type of object represented by the JSON. This object stores information about the reward. | [optional] [default to 'reward']
**name** | **str** | Reward name. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the reward was created in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the reward was updated in ISO 8601 format. | [optional] 
**parameters** | **object** | Defines how the reward is generated. | [optional] 
**type** | **str** | Reward type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


