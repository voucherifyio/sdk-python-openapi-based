# VoucherTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique transaction ID. | 
**source_id** | **str** | The merchant’s transaction ID if it is different from the Voucherify transaction ID. It is really useful in case of an integration between multiple systems. It can be a transaction ID from a CRM system, database or 3rd-party service. In case of a redemption, this value is null. | [optional] 
**voucher_id** | **str** | Unique voucher ID. | 
**campaign_id** | **str** | Unqiue campaign ID of the voucher&#39;s parent campaign if it is part of campaign that generates bulk codes. | 
**source** | **str** | The channel through which the transaction took place, whether through the API or the the Dashboard. In case of a redemption, this value is null. | [optional] 
**reason** | **str** | Reason why the transaction occurred. In case of a redemption, this value is null. | [optional] 
**type** | [**LoyaltyCardTransactionsType**](LoyaltyCardTransactionsType.md) |  | 
**details** | [**VoucherTransactionDetails**](VoucherTransactionDetails.md) |  | 
**related_transaction_id** | **str** | The related transaction ID on the receiving card. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the transaction was created in ISO 8601 format. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


