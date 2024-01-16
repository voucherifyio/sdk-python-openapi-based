# RedemptionsListResponseBody

Response body schema for **GET** `/redemptions`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about redemptions in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of redemption objects. | [default to 'redemptions']
**redemptions** | [**List[RedemptionsListResponseBodyRedemptionsItem]**](RedemptionsListResponseBodyRedemptionsItem.md) |  | 
**total** | **int** | Total number of redemptions. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


