# CampaignVoucher

Schema model for a campaign voucher.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of voucher. | [default to 'DISCOUNT_VOUCHER']
**discount** | [**Discount**](Discount.md) |  | [optional] 
**gift** | [**Gift**](Gift.md) |  | [optional] 
**loyalty_card** | [**CampaignLoyaltyCard**](CampaignLoyaltyCard.md) |  | [optional] 
**redemption** | [**CampaignLoyaltyVoucherRedemption**](CampaignLoyaltyVoucherRedemption.md) |  | 
**code_config** | [**CodeConfigRequiredLengthCharsetPattern**](CodeConfigRequiredLengthCharsetPattern.md) |  | 
**is_referral_code** | **bool** | Flag indicating whether this voucher is a referral code; &#x60;true&#x60; for campaign type &#x60;REFERRAL_PROGRAM&#x60;. | 
**start_date** | **datetime** | Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date.  | [optional] 
**expiration_date** | **datetime** | Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date. | [optional] 
**validity_timeframe** | [**CampaignBaseValidityTimeframe**](CampaignBaseValidityTimeframe.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


