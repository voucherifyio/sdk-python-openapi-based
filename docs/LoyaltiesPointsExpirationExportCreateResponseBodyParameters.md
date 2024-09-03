# LoyaltiesPointsExpirationExportCreateResponseBodyParameters

List of fields and filters that were passed in the request body to create the export.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** | How the export is filtered, where the dash &#x60;-&#x60; preceding a sorting option means sorting in a descending order. | [optional] 
**fields** | **List[str]** | Array of strings containing the data that was exported. These fields define the headers in the CSV file.    The array can be a combination of any of the following available fields:    | **Field** | **Definition** | **Example Export** | |:---|:---|:---| | id | Loyalty points bucket ID. | lopb_Wl1o3EjJIHSNjvO5BDLy4z1n | | campaign_id | Campaign ID of the parent loyalty campaign. | camp_7s3uXI44aKfIk5IhmeOPr6ic | | voucher_id | Voucher ID of the parent loyalty card. | v_YLn0WVWXSXbUfDvxgrgUbtfJ3SQIY655 | | status | Status of the loyalty points bucket. | &#x60;ACTIVE&#x60; or &#x60;INACTIVE&#x60; | | expires_at | Timestamp in ISO 8601 format representing the date when the points expire. | 2022-06-30 | | points | Number of points. | 1000 | | [optional] 
**filters** | [**LoyaltiesPointsExpirationExportCreateResponseBodyParametersFilters**](LoyaltiesPointsExpirationExportCreateResponseBodyParametersFilters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

