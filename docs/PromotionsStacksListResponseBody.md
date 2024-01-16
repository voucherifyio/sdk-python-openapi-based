# PromotionsStacksListResponseBody

Response body schema for **GET** `/promotions/stacks` and for **GET** `/promotions/{campaignId}/stacks`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about promotion stacks in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of promotion stack objects. | [default to 'data']
**data** | [**List[PromotionStack]**](PromotionStack.md) | Contains array of promotion stack objects. | 
**total** | **int** | Total number of promotion stacks. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


