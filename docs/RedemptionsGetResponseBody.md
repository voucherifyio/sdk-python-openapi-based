# RedemptionsGetResponseBody

Response body schema for **GET** `/redemptions/{redemptionId}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique redemption ID. | 
**object** | **str** | The type of object represented by the JSON | [default to 'redemption_rollback']
**var_date** | **datetime** | Timestamp representing the date and time when the object was created in ISO 8601 format. | 
**customer_id** | **str** | Unique customer ID of the redeeming customer. | [optional] 
**tracking_id** | **str** | Hashed customer source ID. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the redemption. | [optional] 
**amount** | **int** | A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items&#39; amounts. | [optional] 
**redemption** | **str** | Unique redemption ID of the parent redemption. | [optional] 
**result** | **str** | Redemption result. | 
**status** | **str** | Redemption status. | 
**related_redemptions** | [**RedemptionRollbackRelatedRedemptions**](RedemptionRollbackRelatedRedemptions.md) |  | [optional] 
**failure_code** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide a generic reason as to why the redemption failed. | [optional] 
**failure_message** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide a more expanded reason as to why the redemption failed. | [optional] 
**order** | [**OrderCalculatedNoCustomerData**](OrderCalculatedNoCustomerData.md) |  | [optional] 
**channel** | [**RedemptionChannel**](RedemptionChannel.md) |  | 
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**related_object_type** | **str** | Defines the related object. | 
**related_object_id** | **str** | Unique related object ID assigned by Voucherify, i.e. v_lfZi4rcEGe0sN9gmnj40bzwK2FH6QUno for a voucher. | 
**voucher** | [**Voucher**](Voucher.md) |  | [optional] 
**promotion_tier** | [**PromotionTier**](PromotionTier.md) |  | [optional] 
**reward** | [**RedemptionRewardResult**](RedemptionRewardResult.md) |  | [optional] 
**gift** | [**RedemptionGift**](RedemptionGift.md) |  | [optional] 
**loyalty_card** | [**RedemptionLoyaltyCard**](RedemptionLoyaltyCard.md) |  | [optional] 
**reason** | **str** | System generated cause for the redemption being invalid in the context of the provided parameters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


