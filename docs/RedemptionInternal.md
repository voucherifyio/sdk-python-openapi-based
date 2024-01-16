# RedemptionInternal

Model Used for internal communication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique redemption ID. | [optional] 
**object** | **str** | The type of object represented by the JSON. This object stores information about the &#x60;redemption&#x60;. | [optional] [default to 'redemption']
**created_at** | **datetime** | Timestamp representing the date and time when the redemption was created in ISO 8601 format. | [optional] 
**tracking_id** | **str** | Hashed customer source ID. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the redemption. | [optional] 
**channel_type** | **str** | The source of the channel for the redemption rollback. A &#x60;USER&#x60; corresponds to the Voucherify Dashboard and an &#x60;API&#x60; corresponds to the API. | [optional] 
**channel_id** | **str** | Unique channel ID of the user performing the redemption. This is either a user ID from a user using the Voucherify Dashboard or an X-APP-Id of a user using the API. | [optional] 
**failure_code** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide a generic reason as to why the redemption failed. | [optional] 
**failure_message** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide a more expanded reason as to why the redemption failed. | [optional] 
**order** | [**OrderCalculated**](OrderCalculated.md) |  | [optional] 
**previous_order** | [**OrderCalculated**](OrderCalculated.md) |  | [optional] 
**reward** | [**RedemptionRewardResult**](RedemptionRewardResult.md) |  | [optional] 
**amount** | **int** | A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items&#39; amounts. | [optional] 
**reason** | **str** | System generated cause for the redemption being invalid in the context of the provided parameters. | [optional] 
**result** | **str** | Redemption result. | [optional] 
**status** | **str** | Redemption status. | [optional] 
**related_redemptions** | [**RedemptionInternalRelatedRedemptions**](RedemptionInternalRelatedRedemptions.md) |  | [optional] 
**parent_redemption_id** | **str** | Unique redemption ID of the parent redemption. | [optional] 
**redemption** | **str** | Unique redemption ID of the parent redemption. | [optional] 
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**customer_id** | **str** | Unique customer ID of the redeeming customer. | [optional] 
**related_object_type** | **str** | Defines the related object. | [optional] 
**related_object_id** | **str** | Unique related object ID assigned by Voucherify, i.e. v_lfZi4rcEGe0sN9gmnj40bzwK2FH6QUno for a voucher. | [optional] 
**related_object_parent_id** | **str** | Unique related parent object ID assigned by Voucherify, i.e. v_lfZi4rcEGe0sN9gmnj40bzwK2FH6QUno for a voucher. | [optional] 
**campaign_name** | **str** | Campaign name | [optional] 
**voucher** | [**Voucher**](Voucher.md) |  | [optional] 
**promotion_tier** | [**PromotionTier**](PromotionTier.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


