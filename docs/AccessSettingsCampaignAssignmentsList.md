# AccessSettingsCampaignAssignmentsList

Lists all assignments of the campaign to areas and stores if the Areas and Stores feature is enabled (Enterprise feature).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. Default is &#x60;list&#x60;. This object stores information about campaign assignments to areas and stores | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of campaign assignments. | [optional] [default to 'data']
**data** | [**List[AreaStoreCampaignAssignment]**](AreaStoreCampaignAssignment.md) | Contains an array of campaign assignments. | [optional] 
**total** | **int** | Total number of areas and stores to which the campaign is assigned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

