# VouchersBalanceUpdateResponseBody

Response body schema for `vouchers/{code}/balance.`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The incremental amount added (positive integer) or subtracted (negative integer) to the current balance on the gift card or loyalty card. Value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 amount is written as 10000. | 
**total** | **int** | Total income incurred over the lifespan of the gift card or loyalty card. | 
**balance** | **int** | The balance after adding or subtracting a specified amount. Value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 amount is written as 10000. | 
**type** | **str** | The type of voucher being modified. | 
**operation_type** | **str** |  | [default to 'MANUAL']
**object** | **str** | The type of object represented by JSON. Default is &#x60;balance&#x60;. | [default to 'balance']
**related_object** | [**VouchersBalanceUpdateResponseBodyRelatedObject**](VouchersBalanceUpdateResponseBodyRelatedObject.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


