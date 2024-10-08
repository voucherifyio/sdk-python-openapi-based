# ValidationRulesListResponseBody

Response body schema for **GET** `v1/validation-rules`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about validation rules. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of validation rules. | [optional] [default to 'data']
**data** | [**List[ValidationRule]**](ValidationRule.md) | An array of validation rules. | [optional] 
**total** | **int** | Total number of validation rules in the project. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


