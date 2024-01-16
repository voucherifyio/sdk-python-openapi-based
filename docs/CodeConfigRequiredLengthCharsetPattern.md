# CodeConfigRequiredLengthCharsetPattern


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **float** | Number of characters in a generated code (excluding prefix and postfix). | 
**charset** | **str** | Characters that can appear in the code.    Examples:  - Alphanumeric: &#x60;0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&#x60;  - Alphabetic: &#x60;abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&#x60;  - Alphabetic Lowercase: &#x60;abcdefghijklmnopqrstuvwxyz&#x60;  - Alphabetic Uppercase: &#x60;ABCDEFGHIJKLMNOPQRSTUVWXYZ&#x60;  - Numbers: &#x60;0123456789&#x60;   - Custom: a custom character set | 
**prefix** | **str** | A text appended before the code. | [optional] 
**postfix** | **str** | A text appended after the code. | [optional] 
**pattern** | **str** | A pattern for codes where hashes (#) will be replaced with random characters. Overrides &#x60;length&#x60;. | 
**initial_count** | **int** | The initial count | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


