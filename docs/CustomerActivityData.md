# CustomerActivityData

Event data object schema.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | 
**unconfirmed_customer** | [**EventCustomerConfirmedUnconfirmedCustomer**](EventCustomerConfirmedUnconfirmedCustomer.md) |  | [optional] 
**referrer** | [**SimpleCustomer**](SimpleCustomer.md) |  | 
**campaign** | [**SimpleCampaign**](SimpleCampaign.md) |  | 
**voucher** | [**SimpleVoucher**](SimpleVoucher.md) |  | 
**custom_event** | [**CustomEvent**](CustomEvent.md) |  | 
**redemption** | [**RedemptionInternal**](RedemptionInternal.md) |  | [optional] 
**segment** | [**SimpleSegment**](SimpleSegment.md) |  | 
**distribution** | **object** |  | [optional] 
**sent_at** | **datetime** | Timestamp representing the date and time when the distribution was sent in ISO 8601 format. | 
**recovered_at** | **datetime** | Timestamp representing the date and time when the distribution was recovered in ISO 8601 format. | 
**failed_at** | **datetime** | Timestamp representing the date and time when the distribution failed in ISO 8601 format. | 
**holder** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**reward** | [**SimpleRedemptionRewardResult**](SimpleRedemptionRewardResult.md) |  | [optional] 
**referral_tier** | [**SimpleReferralTier**](SimpleReferralTier.md) |  | [optional] 
**balance** | **int** |  | [optional] 
**customer_event** | **object** |  | [optional] 
**loyalty_tier** | [**LoyaltyTier**](LoyaltyTier.md) |  | 
**earning_rule** | [**EarningRule**](EarningRule.md) |  | [optional] 
**order** | [**OrderCalculated**](OrderCalculated.md) |  | [optional] 
**event** | **object** |  | [optional] 
**transaction** | [**VoucherTransaction**](VoucherTransaction.md) |  | [optional] 
**source_voucher** | [**SimpleVoucher**](SimpleVoucher.md) |  | [optional] 
**destination_voucher** | [**SimpleVoucher**](SimpleVoucher.md) |  | [optional] 
**points** | **int** |  | [optional] 
**buckets** | [**List[VoucherTransaction]**](VoucherTransaction.md) |  | [optional] 
**publication** | **object** |  | [optional] 
**validation** | [**ValidationEntity**](ValidationEntity.md) |  | [optional] 
**promotion_tier** | [**SimplePromotionTier**](SimplePromotionTier.md) |  | [optional] 
**redemption_rollback** | [**SimpleRedemption**](SimpleRedemption.md) |  | [optional] 
**consents** | [**List[SimpleConsent]**](SimpleConsent.md) |  | [optional] 
**reward_redemption** | **object** |  | [optional] 
**reward_assignment** | [**RewardAssignment**](RewardAssignment.md) |  | [optional] 
**source** | **str** |  | [optional] 
**loyalty** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**loyalty_tier_from** | [**LoyaltyTier**](LoyaltyTier.md) |  | 
**loyalty_tier_to** | [**LoyaltyTier**](LoyaltyTier.md) |  | 
**expiration_date** | **datetime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


