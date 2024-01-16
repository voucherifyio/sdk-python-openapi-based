# PublicationsListResponseBody

Response body schema for listing publications using **GET** `/publications`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about publications in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of publications. | [default to 'publications']
**publications** | [**List[PublicationsListResponseBodyPublicationsItem]**](PublicationsListResponseBodyPublicationsItem.md) | Contains array of publication objects, voucher object will be simplified. | 
**total** | **int** | Total number of publications. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


