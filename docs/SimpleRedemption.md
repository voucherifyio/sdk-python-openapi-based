# SimpleRedemption

This is an object representing a simple redemption.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique redemption ID. | [optional] 
**customer_id** | **str** | Unique customer ID of the redeeming customer. | [optional] 
**tracking_id** | **str** | Hashed customer source ID. | [optional] 
**var_date** | **datetime** | Timestamp representing the date and time when the redemption was created in ISO 8601 format. | [optional] 
**amount** | **int** | A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items&#39; amounts. | [optional] 
**order** | [**SimpleOrder**](SimpleOrder.md) |  | [optional] 
**reward** | [**SimpleRedemptionRewardResult**](SimpleRedemptionRewardResult.md) |  | [optional] 
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**result** | **str** | Redemption result. | [optional] 
**voucher** | [**SimpleVoucher**](SimpleVoucher.md) |  | [optional] 
**promotion_tier** | [**SimplePromotionTier**](SimplePromotionTier.md) |  | [optional] 
**redemption** | **str** | Unique redemption ID of the parent redemption. | [optional] 
**object** | **str** | The type of object represented by the JSON. This object stores information about the &#x60;redemption&#x60;. | [optional] [default to 'redemption']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


