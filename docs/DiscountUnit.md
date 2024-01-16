# DiscountUnit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discount type. | [default to 'UNIT']
**unit_off** | **int** | Number of units to be granted a full value discount. | [optional] 
**unit_off_formula** | **str** |  | [optional] 
**effect** | [**DiscountUnitVouchersEffectTypes**](DiscountUnitVouchersEffectTypes.md) |  | [optional] 
**unit_type** | **str** | The product deemed as free, chosen from product inventory (e.g. time, items). | 
**product** | [**SimpleProductDiscountUnit**](SimpleProductDiscountUnit.md) |  | [optional] 
**sku** | [**SimpleSkuDiscountUnit**](SimpleSkuDiscountUnit.md) |  | [optional] 
**is_dynamic** | **bool** | Flag indicating whether the discount was calculated using a formula. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


