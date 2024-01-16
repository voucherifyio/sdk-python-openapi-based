# VouchersTransactionsExportCreateResponseBody

Response body schema for **POST** `/vouchers/{code}/transactions/export`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique export ID. | 
**object** | **str** | The type of object being represented. This object stores information about the &#x60;export&#x60;. | [default to 'export']
**created_at** | **datetime** | Timestamp representing the date and time when the export was scheduled in ISO 8601 format. | 
**status** | **str** | Status of the export. Informs you whether the export has already been completed, i.e. indicates whether the file containing the exported data has been generated. | [default to 'SCHEDULED']
**channel** | **str** | The channel through which the export was triggered. | [default to 'API']
**exported_object** | **str** | The type of exported object. | [default to 'voucher_transactions']
**parameters** | [**VoucherTransactionsFilters**](VoucherTransactionsFilters.md) |  | 
**result** | [**VoucherTransactionsExportResult**](VoucherTransactionsExportResult.md) |  | [optional] 
**user_id** | **str** | Identifies the specific user who initiated the export through the Voucherify Dashboard; returned when the &#x60;channel&#x60; value is &#x60;WEBSITE&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


