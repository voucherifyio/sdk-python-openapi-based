# SimpleVoucher


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier that represents the voucher assigned by Voucherify. | [optional] 
**code** | **str** | Voucher code. | 
**gift** | [**Gift**](Gift.md) |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**loyalty_card** | **object** | Defines the loyalty card details. | [optional] 
**type** | **str** | Type of the object. | [optional] [default to 'voucher']
**campaign** | **object** | Campaign object | [optional] 
**campaign_id** | **str** | Campaign unique ID. | [optional] 
**is_referral_code** | **bool** | Flag indicating whether this voucher is a referral code; &#x60;true&#x60; for campaign type &#x60;REFERRAL_PROGRAM&#x60;. | [optional] 
**holder_id** | **str** | Unique customer ID of campaign owner. | [optional] 
**referrer_id** | **str** | Unique referrer ID. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the order was created in ISO 8601 format. | [optional] 
**object** | **str** | The type of object represented by JSON. | [optional] [default to 'voucher']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


