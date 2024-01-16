# ExportVoucherTransactions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique export ID. | 
**object** | **str** | The type of object being represented. This object stores information about the export. | [default to 'export']
**created_at** | **datetime** | Timestamp representing the date and time when the export was scheduled in ISO 8601 format. | 
**status** | **str** | Status of the export. Informs you whether the export has already been completed, i.e. indicates whether the file containing the exported data has been generated. | 
**channel** | **str** | The channel through which the export was triggered. | [optional] 
**result** | [**ExportBaseResult**](ExportBaseResult.md) |  | [optional] 
**user_id** | **str** | Identifies the specific user who initiated the export through the Voucherify Dashboard; returned when the channel value is WEBSITE. | [optional] 
**exported_object** | **str** | The type of object to be exported. | [default to 'voucher_transactions']
**parameters** | [**LoyaltiesMembersTransactionsExportCreateRequestBodyParameters**](LoyaltiesMembersTransactionsExportCreateRequestBodyParameters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


