# LoyaltiesMemberActivityListResponseBody

Response body schema for retrieving member activity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about member activities in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of member activity objects. | [optional] [default to 'data']
**data** | [**List[MemberActivity]**](MemberActivity.md) | Array of member activity objects. | [optional] 
**has_more** | **bool** | As query results are always limited (by the limit parameter), the &#x60;has_more&#x60; flag indicates if there are more records for given filter parameters. This lets you know if you can run another request with a &#x60;starting_after_id&#x60; query or a different limit to get more records returned in the results. | [optional] 
**more_starting_after** | **str** | Returns an ID that can be used to return another page of results. Use the event id in the &#x60;starting_after_id&#x60; query parameter to display another page of the results starting after the event with that ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

