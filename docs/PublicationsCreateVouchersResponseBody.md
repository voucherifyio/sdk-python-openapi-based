# PublicationsCreateVouchersResponseBody

Response body schema for **POST** `/publication` and **GET** `/publications/create`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique publication ID, assigned by Voucherify. | 
**object** | **str** | The type of object represented by the JSON. This object stores information about the &#x60;publication&#x60;. | [default to 'publication']
**created_at** | **datetime** | Timestamp representing the date and time when the publication was created in ISO 8601 format. | 
**customer_id** | **str** | Unique customer ID of the customer receiving the publication. | 
**tracking_id** | **str** | Customer&#39;s &#x60;source_id&#x60;. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the publication. A set of key/value pairs that you can attach to a publication object. It can be useful for storing additional information about the publication in a structured format. | 
**channel** | **str** | How the publication was originated. It can be your own custom channel or an example value provided here. | [default to 'API']
**source_id** | **str** | The merchant’s publication ID if it is different from the Voucherify publication ID. It&#39;s an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service.  | [optional] 
**result** | **str** | Status of the publication attempt. | [default to 'SUCCESS']
**customer** | [**CustomerWithSummaryLoyaltyReferrals**](CustomerWithSummaryLoyaltyReferrals.md) |  | 
**vouchers_id** | **List[str]** | Contains the unique internal voucher ID that was assigned by Voucherify. | 
**vouchers** | **List[str]** | Contains the unique voucher codes that was assigned by Voucherify. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


