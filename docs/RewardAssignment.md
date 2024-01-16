# RewardAssignment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique reward assignment ID, assigned by Voucherify. | 
**reward_id** | **str** | Associated reward ID. | 
**created_at** | **datetime** | Timestamp representing the date and time when the reward assignment was created in ISO 8601 format. | 
**updated_at** | **datetime** | Timestamp representing the date and time when the reward assignment was updated in ISO 8601 format. | [optional] 
**object** | **str** | The type of object represented by the JSON. This object stores information about the reward assignment. | [default to 'reward_assignment']
**related_object_id** | **str** | Related object ID to which the reward was assigned. | 
**related_object_type** | **str** | Related object type to which the reward was assigned. | [default to 'campaign']
**parameters** | [**RewardAssignmentParametersParameters**](RewardAssignmentParametersParameters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


