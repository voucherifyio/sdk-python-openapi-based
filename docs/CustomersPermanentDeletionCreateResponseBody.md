# CustomersPermanentDeletionCreateResponseBody

Response body schema for **POST** `/customers/{customerId}/permanent-deletion`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique permanent deletion object ID. | 
**created_at** | **datetime** | Timestamp representing the date and time when the customer was requested to be deleted in ISO 8601 format. | 
**related_object_id** | **str** | Unique customer ID that is being deleted. | 
**related_object** | **str** | Object being deleted. | [default to 'customer']
**status** | **str** | Deletion status. | [default to 'DONE']
**data_json** | [**CustomersPermanentDeletionCreateResponseBodyDataJson**](CustomersPermanentDeletionCreateResponseBodyDataJson.md) |  | 
**object** | **str** | The type of object represented by JSON. | [default to 'pernament_deletion']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


