# openapi_client.EventsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track_custom_event**](EventsApi.md#track_custom_event) | **POST** /v1/events | Track Custom Event
[**track_custom_event_client_side**](EventsApi.md#track_custom_event_client_side) | **POST** /client/v1/events | Track Custom Event (client-side)


# **track_custom_event**
> EventsCreateResponseBody track_custom_event(events_create_request_body=events_create_request_body)

Track Custom Event

To track a custom event, you create an event object.    The event object must be linked to the customer who performs the action. If a customer doesn't exist in Voucherify, the customer will be created.

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.events_create_request_body import EventsCreateRequestBody
from openapi_client.models.events_create_response_body import EventsCreateResponseBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id-1
configuration.api_key['X-App-Id-1'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id-1'] = 'Bearer'

# Configure API key authorization: X-App-Token-1
configuration.api_key['X-App-Token-1'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token-1'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventsApi(api_client)
    events_create_request_body = {"event":"event-name","customer":{"source_id":"referee-source_id"},"referral":{"code":"voucher-code","referrer_id":"referrer-source_id"}} # EventsCreateRequestBody | Specify the details of the custom event. (optional)

    try:
        # Track Custom Event
        api_response = api_instance.track_custom_event(events_create_request_body=events_create_request_body)
        print("The response of EventsApi->track_custom_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->track_custom_event: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events_create_request_body** | [**EventsCreateRequestBody**](EventsCreateRequestBody.md)| Specify the details of the custom event. | [optional] 

### Return type

[**EventsCreateResponseBody**](EventsCreateResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the event type if the event was received by the application. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_custom_event_client_side**
> ClientEventsCreateResponseBody track_custom_event_client_side(origin, client_events_create_request_body=client_events_create_request_body)

Track Custom Event (client-side)

To track a custom event, you create an event object.    The event object must be linked to the customer who performs the action. If a customer doesn't exist in Voucherify, the customer will be created.

### Example

* Api Key Authentication (X-Client-Application-Id-1):
* Api Key Authentication (X-Client-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.client_events_create_request_body import ClientEventsCreateRequestBody
from openapi_client.models.client_events_create_response_body import ClientEventsCreateResponseBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-Client-Application-Id-1
configuration.api_key['X-Client-Application-Id-1'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Application-Id-1'] = 'Bearer'

# Configure API key authorization: X-Client-Token-1
configuration.api_key['X-Client-Token-1'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Token-1'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventsApi(api_client)
    origin = 'origin_example' # str | Indicates the origin (scheme, hostname, and port).
    client_events_create_request_body = {"event":"user_subscribed","customer":{"source_id":"source_customer_event"},"referral":{"code":"46jL0kYI","referrer_id":"cust_Vzck5i8U3OhcEUFY6MKhN9Rv"},"metadata":{"login":"bob","pricing_plan":"PP1","volume_number":4}} # ClientEventsCreateRequestBody | Specify the details of the custom event. (optional)

    try:
        # Track Custom Event (client-side)
        api_response = api_instance.track_custom_event_client_side(origin, client_events_create_request_body=client_events_create_request_body)
        print("The response of EventsApi->track_custom_event_client_side:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->track_custom_event_client_side: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**| Indicates the origin (scheme, hostname, and port). | 
 **client_events_create_request_body** | [**ClientEventsCreateRequestBody**](ClientEventsCreateRequestBody.md)| Specify the details of the custom event. | [optional] 

### Return type

[**ClientEventsCreateResponseBody**](ClientEventsCreateResponseBody.md)

### Authorization

[X-Client-Application-Id-1](../README.md#X-Client-Application-Id-1), [X-Client-Token-1](../README.md#X-Client-Token-1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the event type if the event was received by the application. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

