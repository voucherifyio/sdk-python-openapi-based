# VoucherRedemption

Stores a summary of redemptions that have been applied to the voucher.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | How many times a voucher can be redeemed. A &#x60;null&#x60; value means unlimited. | [optional] 
**redeemed_quantity** | **int** | How many times a voucher has already been redeemed. | [optional] 
**redeemed_amount** | **int** | Total amount redeemed. Value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 balance is written as 10000. | [optional] 
**redeemed_points** | **int** | Total loyalty points redeemed. | [optional] 
**object** | **str** | The type of object represented is by default &#x60;list&#x60;. To get this list, you need to make a call to the endpoint returned in the url attribute. | [optional] [default to 'list']
**url** | **str** | The endpoint where this list of redemptions can be accessed using a GET method. &#x60;/v1/vouchers/{voucher_code}/redemptions&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


