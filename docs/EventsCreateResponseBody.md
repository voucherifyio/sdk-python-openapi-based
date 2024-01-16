# EventsCreateResponseBody

Response body schema for **POST** `/events`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The object represented is an &#x60;event&#x60;. | [default to 'event']
**type** | **str** | The event name. | 
**customer** | [**SimpleCustomerRequiredObjectType**](SimpleCustomerRequiredObjectType.md) |  | 
**referral** | **object** | A &#x60;null&#x60; referral object. | 
**loyalty** | **object** | A &#x60;null&#x60; loyalty object. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


