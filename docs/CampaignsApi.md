# openapi_client.CampaignsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_voucher_with_specific_code_to_campaign**](CampaignsApi.md#add_voucher_with_specific_code_to_campaign) | **POST** /v1/campaigns/{campaignId}/vouchers/{code} | Add Voucher with Specific Code to Campaign
[**add_vouchers_to_campaign**](CampaignsApi.md#add_vouchers_to_campaign) | **POST** /v1/campaigns/{campaignId}/vouchers | Add Vouchers to Campaign
[**create_campaign**](CampaignsApi.md#create_campaign) | **POST** /v1/campaigns | Create Campaign
[**delete_campaign**](CampaignsApi.md#delete_campaign) | **DELETE** /v1/campaigns/{campaignId} | Delete Campaign
[**disable_campaign**](CampaignsApi.md#disable_campaign) | **POST** /v1/campaigns/{campaignId}/disable | Disable Campaign
[**enable_campaign**](CampaignsApi.md#enable_campaign) | **POST** /v1/campaigns/{campaignId}/enable | Enable Campaign
[**get_campaign**](CampaignsApi.md#get_campaign) | **GET** /v1/campaigns/{campaignId} | Get Campaign
[**import_vouchers_to_campaign**](CampaignsApi.md#import_vouchers_to_campaign) | **POST** /v1/campaigns/{campaignId}/import | Import Vouchers to Campaign
[**import_vouchers_to_campaign_using_csv**](CampaignsApi.md#import_vouchers_to_campaign_using_csv) | **POST** /v1/campaigns/{campaignId}/importCSV | Import Vouchers to Campaign by CSV
[**list_campaigns**](CampaignsApi.md#list_campaigns) | **GET** /v1/campaigns | List Campaigns
[**update_campaign**](CampaignsApi.md#update_campaign) | **PUT** /v1/campaigns/{campaignId} | Update Campaign


# **add_voucher_with_specific_code_to_campaign**
> CampaignsVouchersCreateResponseBody add_voucher_with_specific_code_to_campaign(campaign_id, code, campaigns_vouchers_create_request_body=campaigns_vouchers_create_request_body)

Add Voucher with Specific Code to Campaign

This method gives a possibility to add a new voucher to an existing campaign. The voucher definition will be inherited from the definition kept in the campaign profile. However, you are able to overwrite a few properties inherited from the campaign.

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_vouchers_create_request_body import CampaignsVouchersCreateRequestBody
from openapi_client.models.campaigns_vouchers_create_response_body import CampaignsVouchersCreateResponseBody
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
    api_instance = openapi_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the campaign to which voucher will be added. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value.
    code = 'code_example' # str | A custom **code** that identifies the voucher.
    campaigns_vouchers_create_request_body = {"category_id":"cat_0bb81a481615a37b5e","start_date":"2022-09-24T00:00:00Z","expiration_date":"2022-09-25T23:59:59Z","active":false,"redemption":{"quantity":null},"additional_info":"Voucher added using API","metadata":{"Season":"Fall"}} # CampaignsVouchersCreateRequestBody | Specify the voucher parameters that you would like to overwrite. (optional)

    try:
        # Add Voucher with Specific Code to Campaign
        api_response = api_instance.add_voucher_with_specific_code_to_campaign(campaign_id, code, campaigns_vouchers_create_request_body=campaigns_vouchers_create_request_body)
        print("The response of CampaignsApi->add_voucher_with_specific_code_to_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->add_voucher_with_specific_code_to_campaign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the campaign to which voucher will be added. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value. | 
 **code** | **str**| A custom **code** that identifies the voucher. | 
 **campaigns_vouchers_create_request_body** | [**CampaignsVouchersCreateRequestBody**](CampaignsVouchersCreateRequestBody.md)| Specify the voucher parameters that you would like to overwrite. | [optional] 

### Return type

[**CampaignsVouchersCreateResponseBody**](CampaignsVouchersCreateResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a voucher object if the call succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_vouchers_to_campaign**
> CampaignsVouchersCreateResponseBody add_vouchers_to_campaign(campaign_id, vouchers_count=vouchers_count, campaigns_vouchers_create_in_bulk_request_body=campaigns_vouchers_create_in_bulk_request_body)

Add Vouchers to Campaign

This method gives the possibility to push new vouchers to an existing campaign. New vouchers will inherit properties from the campaign profile. However, it is possible to overwrite some of them in the request body. If you provide an optional `code_config` parameter with a voucher code configuration, then it will be used to generate new voucher codes. Otherwise, the voucher code configuration from the campaign will be used.  This API request starts a process that affects Voucherify data in bulk.   In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the `IN_PROGRESS` status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.   The result will return the async ID. You can verify the status of your request via this [API request](ref:get-async-action).

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_vouchers_create_in_bulk_request_body import CampaignsVouchersCreateInBulkRequestBody
from openapi_client.models.campaigns_vouchers_create_response_body import CampaignsVouchersCreateResponseBody
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
    api_instance = openapi_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the campaign to which voucher(s) will be added. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value.
    vouchers_count = 56 # int | Number of vouchers that should be added. (optional)
    campaigns_vouchers_create_in_bulk_request_body = {"start_date":"2022-09-24T00:00:00Z","expiration_date":"2022-09-25T23:59:59Z","active":false,"redemption":{"quantity":null},"code_config":{"charset":"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ","length":8,"prefix":"Add-","pattern":null,"postfix":"-API"},"additional_info":"Voucher added using API","metadata":{"Season":"Fall"}} # CampaignsVouchersCreateInBulkRequestBody | Specify the voucher parameters that you would like to overwrite. (optional)

    try:
        # Add Vouchers to Campaign
        api_response = api_instance.add_vouchers_to_campaign(campaign_id, vouchers_count=vouchers_count, campaigns_vouchers_create_in_bulk_request_body=campaigns_vouchers_create_in_bulk_request_body)
        print("The response of CampaignsApi->add_vouchers_to_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->add_vouchers_to_campaign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the campaign to which voucher(s) will be added. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value. | 
 **vouchers_count** | **int**| Number of vouchers that should be added. | [optional] 
 **campaigns_vouchers_create_in_bulk_request_body** | [**CampaignsVouchersCreateInBulkRequestBody**](CampaignsVouchersCreateInBulkRequestBody.md)| Specify the voucher parameters that you would like to overwrite. | [optional] 

### Return type

[**CampaignsVouchersCreateResponseBody**](CampaignsVouchersCreateResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a voucher object if the call succeeded for a voucher count of 1. |  -  |
**202** | Returns an &#x60;async_action_id&#x60; if the request was made to create more than 1 voucher. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign**
> CampaignsCreateResponseBody create_campaign(campaigns_create_request_body=campaigns_create_request_body)

Create Campaign

Method to create a batch of vouchers aggregated in one campaign. You can choose a variety of voucher types and define a unique pattern for generating codes.   <!-- theme: info -->  > 📘 Global uniqueness > > All campaign codes are unique across the whole project. Voucherify will not allow you to generate 2 campaigns with the same coupon code.   <!-- theme: warning --> > 🚧 Code generation status > > This is an asynchronous action; you can't read or modify a newly created campaign until the code generation is completed. See the `creation_status` field in the <!-- [campaign object](OpenAPI.json/components/schemas/Campaign) -->[campaign object](ref:get-campaign) description.

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_create_request_body import CampaignsCreateRequestBody
from openapi_client.models.campaigns_create_response_body import CampaignsCreateResponseBody
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
    api_instance = openapi_client.CampaignsApi(api_client)
    campaigns_create_request_body = {"name":"Discount Campaign 4","campaign_type":"DISCOUNT_COUPONS","join_once":true,"type":"AUTO_UPDATE","category_id":"cat_0bb343dee3cdb5ec0c","start_date":"2020-08-16T00:00:00Z","expiration_date":"2023-12-26T00:00:00Z","vouchers_count":3,"voucher":{"type":"DISCOUNT_VOUCHER","discount":{"percent_off":10,"type":"PERCENT"},"redemption":{"quantity":10},"code_config":{"pattern":"10OFF-#######"}},"validity_timeframe":{"interval":"P2D","duration":"P1D"},"validity_day_of_week":[0,1,2],"activity_duration_after_publishing":"P24D","use_voucher_metadata_schema":false,"metadata":{"region":"AMER"}} # CampaignsCreateRequestBody | Specify the details of the campaign that you would like to create. (optional)

    try:
        # Create Campaign
        api_response = api_instance.create_campaign(campaigns_create_request_body=campaigns_create_request_body)
        print("The response of CampaignsApi->create_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->create_campaign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaigns_create_request_body** | [**CampaignsCreateRequestBody**](CampaignsCreateRequestBody.md)| Specify the details of the campaign that you would like to create. | [optional] 

### Return type

[**CampaignsCreateResponseBody**](CampaignsCreateResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a campaign object if the call succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign**
> CampaignsDeleteResponseBody delete_campaign(campaign_id, force=force)

Delete Campaign

Permanently deletes a campaign and all related vouchers. This action cannot be undone. Also, this method immediately removes any redemptions on the voucher.  This API request starts a process that affects Voucherify data in bulk.   In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the `IN_PROGRESS` status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.   The result will return the async ID. You can verify the status of your request via this [API request](ref:get-async-action).

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_delete_response_body import CampaignsDeleteResponseBody
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
    api_instance = openapi_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value.
    force = True # bool | If this flag is set to `true`, the campaign and related vouchers will be removed permanently. Going forward, the user will be able to create the next campaign with exactly the same name. (optional)

    try:
        # Delete Campaign
        api_response = api_instance.delete_campaign(campaign_id, force=force)
        print("The response of CampaignsApi->delete_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->delete_campaign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value. | 
 **force** | **bool**| If this flag is set to &#x60;true&#x60;, the campaign and related vouchers will be removed permanently. Going forward, the user will be able to create the next campaign with exactly the same name. | [optional] 

### Return type

[**CampaignsDeleteResponseBody**](CampaignsDeleteResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Returns the ID of the scheduled asynchronous action, informing you that your request has been accepted and the campaign will be deleted from the repository asynchronously. To check the deletion status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_campaign**
> CampaignsDisableResponseBody disable_campaign(campaign_id)

Disable Campaign

There are various times when you'll want to manage a campaign's accessibility. This can be done by two API methods for managing the campaign state - *enable* and *disable*.    Sets campaign state to **inactive**. The vouchers in this campaign can no longer be redeemed.

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_disable_response_body import CampaignsDisableResponseBody
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
    api_instance = openapi_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the campaign being disabled. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value.

    try:
        # Disable Campaign
        api_response = api_instance.disable_campaign(campaign_id)
        print("The response of CampaignsApi->disable_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->disable_campaign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the campaign being disabled. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value. | 

### Return type

[**CampaignsDisableResponseBody**](CampaignsDisableResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an empty json &#x60;{}&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_campaign**
> CampaignsEnableResponseBody enable_campaign(campaign_id)

Enable Campaign

There are various times when you'll want to manage a campaign's accessibility. This can be done by two API methods for managing the campaign state - *enable* and *disable*.    Sets campaign state to **active**. The vouchers in this campaign can be redeemed - only if the redemption occurs after the start date of the campaign and voucher and the voucher and campaign are not expired.

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_enable_response_body import CampaignsEnableResponseBody
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
    api_instance = openapi_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the campaign being enabled. You can either pass the campaign ID, which was assigned by Voucherify or the name of the campaign as the path parameter value.

    try:
        # Enable Campaign
        api_response = api_instance.enable_campaign(campaign_id)
        print("The response of CampaignsApi->enable_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->enable_campaign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the campaign being enabled. You can either pass the campaign ID, which was assigned by Voucherify or the name of the campaign as the path parameter value. | 

### Return type

[**CampaignsEnableResponseBody**](CampaignsEnableResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an empty json &#x60;{}&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign**
> CampaignsGetResponseBody get_campaign(campaign_id)

Get Campaign

Retrieves the campaign with the given campaign ID or campaign name.

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_get_response_body import CampaignsGetResponseBody
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
    api_instance = openapi_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value.

    try:
        # Get Campaign
        api_response = api_instance.get_campaign(campaign_id)
        print("The response of CampaignsApi->get_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->get_campaign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value. | 

### Return type

[**CampaignsGetResponseBody**](CampaignsGetResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a campaign object if a valid identifier was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vouchers_to_campaign**
> CampaignsImportCreateResponseBody import_vouchers_to_campaign(campaign_id, campaigns_import_voucher_item=campaigns_import_voucher_item)

Import Vouchers to Campaign

Imports vouchers to an **existing** campaign.  This API request starts a process that affects Voucherify data in bulk.   In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the `IN_PROGRESS` status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.   The result will return the async ID. You can verify the status of your request via this [API request](ref:get-async-action).

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_import_create_response_body import CampaignsImportCreateResponseBody
from openapi_client.models.campaigns_import_voucher_item import CampaignsImportVoucherItem
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
    api_instance = openapi_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | The ID of an existing campaign to which you're importing the codes. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value.
    campaigns_import_voucher_item = [{"code":"CODE7","category":"First","redemption":{"quantity":1},"metadata":{"season":"Fall"},"additional_info":"secret-code1","active":true},{"code":"CODE8","category":"Second","redemption":{"quantity":18},"metadata":{"season":"Fall"},"additional_info":"secret-code1","active":true},{"code":"CODE9","category_id":"cat_0bb343dee3cdb5ec0c","redemption":{"quantity":4},"metadata":{"season":"Fall"},"additional_info":"secret-code1","active":true}] # List[CampaignsImportVoucherItem] | Discount type, expiration date and the remaining attributes will be taken from the <!-- [Campaign](OpenAPI.json/components/schemas/Campaign) -->[Campaign](ref:get-campaign) settings. (optional)

    try:
        # Import Vouchers to Campaign
        api_response = api_instance.import_vouchers_to_campaign(campaign_id, campaigns_import_voucher_item=campaigns_import_voucher_item)
        print("The response of CampaignsApi->import_vouchers_to_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->import_vouchers_to_campaign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of an existing campaign to which you&#39;re importing the codes. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value. | 
 **campaigns_import_voucher_item** | [**List[CampaignsImportVoucherItem]**](CampaignsImportVoucherItem.md)| Discount type, expiration date and the remaining attributes will be taken from the &lt;!-- [Campaign](OpenAPI.json/components/schemas/Campaign) --&gt;[Campaign](ref:get-campaign) settings. | [optional] 

### Return type

[**CampaignsImportCreateResponseBody**](CampaignsImportCreateResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Returns the ID of the scheduled asynchronous action, informing you that your request has been accepted and the vouchers will be imported to the repository asynchronously. To check the status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vouchers_to_campaign_using_csv**
> CampaignsImportCsvCreateResponseBody import_vouchers_to_campaign_using_csv(campaign_id, file)

Import Vouchers to Campaign by CSV

Imports vouchers to an **existing** campaign.     The CSV file has to include headers in the first line.   Curl Example <!-- title: \"Example Request\" lineNumbers: true --> ```cURL curl -X POST \\   https://api.voucherify.io/v1/campaigns/TEST-CAMPAIGN/importCSV \\   -F file=@/path/to/campaigns.csv \\   -H \"X-App-Id: c70a6f00-cf91-4756-9df5-47628850002b\" \\   -H \"X-App-Token: 3266b9f8-e246-4f79-bdf0-833929b1380c\" ```  You can import values for the following fields: `Code` (**required**), `Category`, `Active`. In a gift cards import, you can also include the current card balance using the `Gift Amount` header and the amount that was redeemed using the `Redeemed Amount` header. In a loyalty cards import, you can also include the current loyalty card score in points using the `Loyalty Points` header. Remaining CSV columns will be mapped to metadata properties.   Discount type, time limits, and validation rules will be taken from the <!-- [campaign object](OpenAPI.json/components/schemas/Campaign) -->[campaign object](ref:get-campaign) settings.    | **Active** | **Code** | **Loyalty Points** | **Gift Amount** | **Redeemed Amount** | **Redeemed Quantity** | **Category** | **Custom_metadata_property** | |---|---|---|---|---|---|---|---| | Use `true` or `false` to enable or disable the voucher; this flag can be used to turn off the ability to redeem a voucher even though it is within the campaign's start/end validity timeframe. | The unique voucher code. | The number of points to be added to the loyalty card. If you leave this undefined, then the initial number of points will be set according to the campaign settings.<br>Context: `LOYALTY_PROGRAM` | The initial gift card balance.<br>Context: `GIFT_VOUCHERS` | The amount that was redeemed from the available balance on a gift card. | The number of times the voucher has been redeemed. | A custom tag for the voucher to help you filter codes; you can either import the category name or a unique Voucherify-assigned category ID. | Any additional data that you would like to store for the given loyalty card as a Custom attribute. Remember to define the metadata schema in the Dashboard prior to importing codes. | |<!-- theme: info -->  > 📘 Active > > The CSV file is allowed in two versions; either with or without a column titled `Active`. It indicates whether the voucher is enabled after the import event.    This API request starts a process that affects Voucherify data in bulk.   In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the `IN_PROGRESS` status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.   The result will return the async ID. You can verify the status of your request via this [API request](ref:get-async-action).

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_import_csv_create_response_body import CampaignsImportCsvCreateResponseBody
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
    api_instance = openapi_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the campaign being enabled. You can either pass the campaign ID, which was assigned by Voucherify or the name of the campaign as the path parameter value.
    file = None # bytearray | File path.

    try:
        # Import Vouchers to Campaign by CSV
        api_response = api_instance.import_vouchers_to_campaign_using_csv(campaign_id, file)
        print("The response of CampaignsApi->import_vouchers_to_campaign_using_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->import_vouchers_to_campaign_using_csv: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the campaign being enabled. You can either pass the campaign ID, which was assigned by Voucherify or the name of the campaign as the path parameter value. | 
 **file** | **bytearray**| File path. | 

### Return type

[**CampaignsImportCsvCreateResponseBody**](CampaignsImportCsvCreateResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the ID of the scheduled asynchronous action, informing you that your request has been accepted and the vouchers will be imported to the repository asynchronously. To check the status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_campaigns**
> CampaignsListResponseBody list_campaigns(limit=limit, page=page, campaign_type=campaign_type, expand=expand, order=order)

List Campaigns

Retrieve a list of campaigns in a project.   The campaigns are returned sorted by creation date, with the most recent campaigns appearing first.    When you get a list of campaigns, you can optionally specify query parameters to customize the amount of campaigns returned per call using `limit`, which page of campaigns to return using `page`, sort the campaigns using the `order` query parameter and filter the results by the `campaign_type`.  This method will return an error when trying to return a limit of more than 100 campaigns.

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_list_response_body import CampaignsListResponseBody
from openapi_client.models.parameter_campaign_type import ParameterCampaignType
from openapi_client.models.parameter_expand_list_campaigns import ParameterExpandListCampaigns
from openapi_client.models.parameter_order_list_campaigns import ParameterOrderListCampaigns
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
    api_instance = openapi_client.CampaignsApi(api_client)
    limit = 56 # int | A limit on the number of objects to be returned. Limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. (optional)
    campaign_type = openapi_client.ParameterCampaignType() # ParameterCampaignType | This attribute allows filtering by campaign type. (optional)
    expand = openapi_client.ParameterExpandListCampaigns() # ParameterExpandListCampaigns | Include an expanded `categories` object in the response. (optional)
    order = openapi_client.ParameterOrderListCampaigns() # ParameterOrderListCampaigns | Sorts the results using one of the filtering options, where the dash `-` preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Campaigns
        api_response = api_instance.list_campaigns(limit=limit, page=page, campaign_type=campaign_type, expand=expand, order=order)
        print("The response of CampaignsApi->list_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->list_campaigns: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| A limit on the number of objects to be returned. Limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. | [optional] 
 **campaign_type** | [**ParameterCampaignType**](.md)| This attribute allows filtering by campaign type. | [optional] 
 **expand** | [**ParameterExpandListCampaigns**](.md)| Include an expanded &#x60;categories&#x60; object in the response. | [optional] 
 **order** | [**ParameterOrderListCampaigns**](.md)| Sorts the results using one of the filtering options, where the dash &#x60;-&#x60; preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**CampaignsListResponseBody**](CampaignsListResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a dictionary with a &#x60;campaign&#x60; property that contains an array of campaigns. The maximum number of campaigns returned is determined by the &#x60;limit&#x60; query parameter. Each entry in the array is a separate campaign object. If no more campaigns are available, the resulting array on a given page will be empty. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign**
> CampaignsUpdateResponseBody update_campaign(campaign_id, campaigns_update_request_body=campaigns_update_request_body)

Update Campaign

Updates the specified campaign by setting the values of the parameters passed in the request body. Any parameters not provided in the payload will be left unchanged.   Fields other than the ones listed in the request body won't be modified. Even if provided, they will be silently skipped.    <!-- theme: warning --> > #### Vouchers will be affected > > This method will update vouchers aggregated in the campaign. It will affect all vouchers that are not published or redeemed yet.

### Example

* Api Key Authentication (X-App-Id-1):
* Api Key Authentication (X-App-Token-1):
```python
import time
import os
import openapi_client
from openapi_client.models.campaigns_update_request_body import CampaignsUpdateRequestBody
from openapi_client.models.campaigns_update_response_body import CampaignsUpdateResponseBody
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
    api_instance = openapi_client.CampaignsApi(api_client)
    campaign_id = 'campaign_id_example' # str | You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value.
    campaigns_update_request_body = {"description":"New description"} # CampaignsUpdateRequestBody | Specify the campaign parameters to be updated. (optional)

    try:
        # Update Campaign
        api_response = api_instance.update_campaign(campaign_id, campaigns_update_request_body=campaigns_update_request_body)
        print("The response of CampaignsApi->update_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->update_campaign: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value. | 
 **campaigns_update_request_body** | [**CampaignsUpdateRequestBody**](CampaignsUpdateRequestBody.md)| Specify the campaign parameters to be updated. | [optional] 

### Return type

[**CampaignsUpdateResponseBody**](CampaignsUpdateResponseBody.md)

### Authorization

[X-App-Id-1](../README.md#X-App-Id-1), [X-App-Token-1](../README.md#X-App-Token-1)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the campaign object if the update succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

