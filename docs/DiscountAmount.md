# DiscountAmount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Defines the type of the voucher. | [default to 'AMOUNT']
**amount_off** | **float** | Amount taken off the subtotal of a price. Value is multiplied by 100 to precisely represent 2 decimal places. For example, a $10 discount is written as 1000. | 
**amount_off_formula** | **str** |  | [optional] 
**aggregated_amount_limit** | **int** | Maximum discount amount per order. | [optional] 
**effect** | [**DiscountAmountVouchersEffectTypes**](DiscountAmountVouchersEffectTypes.md) |  | [optional] 
**is_dynamic** | **bool** | Flag indicating whether the discount was calculated using a formula. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


