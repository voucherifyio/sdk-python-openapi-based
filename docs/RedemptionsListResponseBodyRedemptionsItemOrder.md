# RedemptionsListResponseBodyRedemptionsItemOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID assigned by Voucherify of an existing order that will be linked to the redemption of this request. | [optional] 
**source_id** | **str** | Unique source ID of an existing order that will be linked to the redemption of this request. | [optional] 
**status** | **str** | The order status. | [optional] 
**amount** | **int** | A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items&#39; amounts. | [optional] 
**initial_amount** | **int** | A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items&#39; amounts. | [optional] 
**discount_amount** | **int** | Sum of all order-level discounts applied to the order. | [optional] 
**items_discount_amount** | **int** | Sum of all product-specific discounts applied to the order. | [optional] 
**total_discount_amount** | **int** | Sum of all order-level AND all product-specific discounts applied to the order. | [optional] 
**total_amount** | **int** | Order amount after undoing all the discounts through the rollback redemption. | [optional] 
**applied_discount_amount** | **int** | This field shows the order-level discount applied. | [optional] 
**items_applied_discount_amount** | **int** | Sum of all product-specific discounts applied in a particular request.   &#x60;sum(items, i &#x3D;&gt; i.applied_discount_amount)&#x60; | [optional] 
**total_applied_discount_amount** | **int** | Sum of all order-level AND all product-specific discounts applied in a particular request.   &#x60;total_applied_discount_amount&#x60; &#x3D; &#x60;applied_discount_amount&#x60; + &#x60;items_applied_discount_amount&#x60; | [optional] 
**items** | [**List[OrderCalculatedItem]**](OrderCalculatedItem.md) | Array of items applied to the order. | [optional] 
**metadata** | **object** |  | [optional] 
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'order']
**created_at** | **datetime** | Timestamp representing the date and time when the order was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the order was last updated in ISO 8601 format. | [optional] 
**customer_id** | **str** | Unique customer ID of the customer making the purchase. | [optional] 
**referrer_id** | **str** | Unique referrer ID. | [optional] 
**customer** | [**RedemptionsListResponseBodyRedemptionsItemOrderCustomer**](RedemptionsListResponseBodyRedemptionsItemOrderCustomer.md) |  | [optional] 
**referrer** | [**RedemptionsListResponseBodyRedemptionsItemOrderReferrer**](RedemptionsListResponseBodyRedemptionsItemOrderReferrer.md) |  | [optional] 
**redemptions** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

