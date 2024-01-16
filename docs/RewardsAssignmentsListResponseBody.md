# RewardsAssignmentsListResponseBody

Response body schema for **GET** `/rewards/{rewardID}/assignments`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about reward assignments in a dictionary. | [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of reward assignments. | [default to 'data']
**data** | [**List[RewardAssignment]**](RewardAssignment.md) |  | 
**total** | **int** | Total number of reward assignments. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


