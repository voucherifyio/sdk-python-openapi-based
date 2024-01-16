# DiscountPercent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Defines the type of the voucher. | [default to 'PERCENT']
**percent_off** | **float** | The percent discount that the customer will receive. | 
**percent_off_formula** | **str** |  | [optional] 
**amount_limit** | **float** | Upper limit allowed to be applied as a discount. Value is multiplied by 100 to precisely represent 2 decimal places. For example, a $6 maximum discount is written as 600. | [optional] 
**aggregated_amount_limit** | **int** | Maximum discount amount per order. | [optional] 
**effect** | [**DiscountPercentVouchersEffectTypes**](DiscountPercentVouchersEffectTypes.md) |  | [optional] 
**is_dynamic** | **bool** | Flag indicating whether the discount was calculated using a formula. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


