# voucherify_client.SegmentsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_segment**](SegmentsApi.md#delete_segment) | **DELETE** /v1/segments/{segmentId} | Delete Segment


# **delete_segment**
> delete_segment(segment_id)

Delete Segment

This method deletes a customer segment.

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import voucherify_client
from voucherify_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify_client.Configuration(
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
with voucherify_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify_client.SegmentsApi(api_client)
    segment_id = 'segment_id_example' # str | A unique customer segment ID.

    try:
        # Delete Segment
        api_instance.delete_segment(segment_id)
    except Exception as e:
        print("Exception when calling SegmentsApi->delete_segment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **str**| A unique customer segment ID. | 

### Return type

void (empty response body)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns no content if deletion is successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

