# voucherify_client.QualificationsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_eligibility**](QualificationsApi.md#check_eligibility) | **POST** /v1/qualifications | Check Eligibility
[**check_eligibility_client_side**](QualificationsApi.md#check_eligibility_client_side) | **POST** /client/v1/qualifications | Check Eligibility (client-side)


# **check_eligibility**
> QualificationsCheckEligibilityResponseBody check_eligibility(qualifications_check_eligibility_request_body=qualifications_check_eligibility_request_body)

Check Eligibility

<!-- theme: warning --> > 🚧 The Qualifications endpoint in the basic mode ignores the rules checking: >  > - Limit of total redeemed discount amount per campaign > - Limit of total redemptions count per campaign > - Redemptions per customer > - Redemptions per customer in a campaign   Generate a list of redeemables that are applicable in the context of the customer and order.  The new qualifications method is an improved version of [Campaign Qualifications](ref:examine-campaigns-qualification), [Voucher Qualifications](ref:examine-vouchers-qualification), and [Promotions Validation](ref:validate-promotions) API requests. The new qualification method introduces the following improvements:  - Qualification results are returned faster - No limit on the number of returned redeemables - Introduces new qualification scenarios, not available in the previous version  > 👍 Scenario Guide > > Read our dedicated guide to learn about some use cases this endpoint can cover [here](doc:checking-eligibility).  ## Paging   The Voucherify Qualifications API request will return to you all of the redeemables available for the customer in batches of up to 50 redeemables. To get the next batch of redeemables, you need to use the `starting_after` cursor.  To process of paging the redeemables works in the following manner:  - You send the first API request for Qualifications without the `starting_after` parameter. - The response will contain a parameter named `has_more`. If the parameter's value is set to `true`, then more redeemables are available. - Get the value of the `created_at` parameter of the last returned redeemable. The value of this parameter will be used as a cursor to retrieve the next page of redeemables. - Send another API request for Qualification with the `starting_after` parameter set to the value taken from the `created_at` parameter from the last returned redeemable. - Voucherify will return the next page of redeemables. - If the `has_more` parameter is set to `true`, apply steps 3-5 to get the next page of redeemables.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.qualifications_check_eligibility_request_body import QualificationsCheckEligibilityRequestBody
from voucherify_client.models.qualifications_check_eligibility_response_body import QualificationsCheckEligibilityResponseBody
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

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify_client.QualificationsApi(api_client)
    qualifications_check_eligibility_request_body = voucherify_client.QualificationsCheckEligibilityRequestBody() # QualificationsCheckEligibilityRequestBody | Define order and customer context. (optional)

    try:
        # Check Eligibility
        api_response = api_instance.check_eligibility(qualifications_check_eligibility_request_body=qualifications_check_eligibility_request_body)
        print("The response of QualificationsApi->check_eligibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualificationsApi->check_eligibility: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qualifications_check_eligibility_request_body** | [**QualificationsCheckEligibilityRequestBody**](QualificationsCheckEligibilityRequestBody.md)| Define order and customer context. | [optional] 

### Return type

[**QualificationsCheckEligibilityResponseBody**](QualificationsCheckEligibilityResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a qualifications object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_eligibility_client_side**
> ClientQualificationsCheckEligibilityResponseBody check_eligibility_client_side(client_qualifications_check_eligibility_request_body=client_qualifications_check_eligibility_request_body)

Check Eligibility (client-side)

Generate a list of redeemables that are applicable in the context of the customer and order.  The new qualifications method is an improved version of [Campaign Qualifications](ref:examine-campaigns-qualification), [Voucher Qualifications](ref:examine-vouchers-qualification), and [Promotions Validation](ref:validate-promotions) API requests. The new qualification method introduces the following improvements:  - Qualification results are returned faster - No limit on the number of returned redeemables - Introduces new qualification scenarios, not available in the previous version  > 👍 Scenario Guide > > Read our dedicated guide to learn about some use cases this endpoint can cover [here](doc:checking-eligibility).  ## Paging   The Voucherify Qualifications API request will return to you all of the redeemables available for the customer in batches of up to 50 redeemables. To get the next batch of redeemables, you need to use the `starting_after` cursor.  To process of paging the redeemables works in the following manner:  - You send the first API request for Qualifications without the `starting_after` parameter. - The response will contain a parameter named `has_more`. If the parameter's value is set to `true`, then more redeemables are available. - Get the value of the `created_at` parameter of the last returned redeemable. The value of this parameter will be used as a cursor to retrieve the next page of redeemables. - Send another API request for Qualification with the `starting_after` parameter set to the value taken from the `created_at` parameter from the last returned redeemable. - Voucherify will return the next page of redeemables. - If the `has_more` parameter is set to `true`, apply steps 3-5 to get the next page of redeemables.

### Example

* Api Key Authentication (X-Client-Application-Id):
* Api Key Authentication (X-Client-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.client_qualifications_check_eligibility_request_body import ClientQualificationsCheckEligibilityRequestBody
from voucherify_client.models.client_qualifications_check_eligibility_response_body import ClientQualificationsCheckEligibilityResponseBody
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

# Configure API key authorization: X-Client-Application-Id
configuration.api_key['X-Client-Application-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Application-Id'] = 'Bearer'

# Configure API key authorization: X-Client-Token
configuration.api_key['X-Client-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Client-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify_client.QualificationsApi(api_client)
    client_qualifications_check_eligibility_request_body = voucherify_client.ClientQualificationsCheckEligibilityRequestBody() # ClientQualificationsCheckEligibilityRequestBody | Define order and customer context. (optional)

    try:
        # Check Eligibility (client-side)
        api_response = api_instance.check_eligibility_client_side(client_qualifications_check_eligibility_request_body=client_qualifications_check_eligibility_request_body)
        print("The response of QualificationsApi->check_eligibility_client_side:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QualificationsApi->check_eligibility_client_side: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_qualifications_check_eligibility_request_body** | [**ClientQualificationsCheckEligibilityRequestBody**](ClientQualificationsCheckEligibilityRequestBody.md)| Define order and customer context. | [optional] 

### Return type

[**ClientQualificationsCheckEligibilityResponseBody**](ClientQualificationsCheckEligibilityResponseBody.md)

### Authorization

[X-Client-Application-Id](../README.md#X-Client-Application-Id), [X-Client-Token](../README.md#X-Client-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a qualifications object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

