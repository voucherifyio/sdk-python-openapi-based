# ValidationRulesListResponseBody

Response body schema for **GET** `/validation-rules`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about validation rules. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of validation rules. | [default to 'data']
**data** | [**List[ValidationRule]**](ValidationRule.md) | An array of validation rules. | 
**total** | **int** | Total number of validation rules in the project. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


