# EventCustomerVouchersLoyaltyPointsExpired

Event data object schema for `customer.voucher.loyalty_card.points_expired`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**campaign** | [**SimpleCampaign**](SimpleCampaign.md) |  | [optional] 
**voucher** | [**SimpleVoucher**](SimpleVoucher.md) |  | [optional] 
**points** | **int** |  | [optional] 
**buckets** | [**List[VoucherTransaction]**](VoucherTransaction.md) |  | [optional] 
**transaction** | [**VoucherTransaction**](VoucherTransaction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


