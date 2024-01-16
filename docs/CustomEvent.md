# CustomEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique custom event ID. | [optional] 
**object** | **str** | The object represented is an &#x60;event&#x60;. | [default to 'event']
**type** | **str** | The event name. | 
**customer** | [**SimpleCustomerRequiredObjectType**](SimpleCustomerRequiredObjectType.md) |  | 
**referral** | [**CustomEventReferral**](CustomEventReferral.md) |  | 
**loyalty** | **object** |  | 
**metadata** | **object** | A set of custom key/value pairs that you can attach to a customer. The metadata object stores all custom attributes assigned to the custom event. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the custom event was created in ISO 8601 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


