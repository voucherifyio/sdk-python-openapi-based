# VoucherTransactionDetailsBalance

Contains information on how the balance was affected by the transaction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of voucher whose balance is being adjusted due to the transaction. | [default to 'loyalty_card']
**total** | **int** | The available points prior to the transaction. | 
**object** | **str** | The type of object represented by the JSON. | [default to 'balance']
**points** | **int** | The amount of points being used up in the transaction. | 
**balance** | **int** | The points balance on the loyalty card after the points in the transaction are subtracted from the loyalty card. | 
**related_object** | [**VoucherTransactionDetailsBalanceRelatedObject**](VoucherTransactionDetailsBalanceRelatedObject.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


