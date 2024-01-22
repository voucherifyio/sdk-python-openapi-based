# ExportCustomerBaseParameters

List of available fields and filters that can be exported with an order along with the sorting order of the returned data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**ExportCustomerOrder**](ExportCustomerOrder.md) |  | [optional] 
**fields** | [**List[ExportCustomerFields]**](ExportCustomerFields.md) | Array of strings containing the data in the export. These fields define the headers in the CSV file. | [optional] 
**filters** | **object** | Allowed additional properties must start with \&quot;metadata.\&quot; or \&quot;address.\&quot; or \&quot;summary.\&quot; or \&quot;loyalty.\&quot; or \&quot;loyalty_tier.\&quot; or \&quot;loyalty_points.\&quot; or \&quot;system_metadata.\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


