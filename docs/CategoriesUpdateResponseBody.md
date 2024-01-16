# CategoriesUpdateResponseBody

Response body schema for **PUT** `/categories/{categoryId}`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique category ID assigned by Voucherify. | 
**name** | **str** | Category name. | 
**hierarchy** | **int** | Category hierarchy. | 
**object** | **str** |  | [default to 'category']
**created_at** | **datetime** | Timestamp representing the date and time when the category was created in ISO 8601 format. | 
**updated_at** | **datetime** | Timestamp representing the date and time when the category was updated in ISO 8601 format. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


