# voucherify_client.PublicationsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_publication**](PublicationsApi.md#create_publication) | **POST** /v1/publications | Create Publication
[**create_publication1**](PublicationsApi.md#create_publication1) | **GET** /v1/publications/create | Create Publication
[**list_publications**](PublicationsApi.md#list_publications) | **GET** /v1/publications | List Publications


# **create_publication**
> PublicationsCreateResponseBody create_publication(join_once=join_once, publications_create_request_body=publications_create_request_body)

Create Publication

This method selects vouchers that are suitable for publication, adds a publish entry and returns the publication.  A voucher is suitable for publication when it's active and hasn't been published yet.    <!-- theme: warning --> > 🚧 Clearly define the source of the voucher > > You must clearly define which source you want to publish the voucher code from. It can either be a code from a campaign or a specific voucher identified by a code.   <!-- theme: warning --> > 🚧 Publish multiple vouchers > In case you want to publish multiple vouchers within a single publication, you need to specify the campaign name and number of vouchers you want to publish.   <!-- theme: info -->  > 📘 Auto-update campaign > > In case you want to ensure the number of publishable codes increases automatically with the number of customers, you should use an **auto-update** campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.publications_create_request_body import PublicationsCreateRequestBody
from voucherify_client.models.publications_create_response_body import PublicationsCreateResponseBody
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
    api_instance = voucherify_client.PublicationsApi(api_client)
    join_once = True # bool | Through this flag, you can control if a particular person gets only one and always the same code even if the app sends multiple publication requests. It means that if you have a referral program, a referrer is assigned only to one code if an integration sends publication requests more than once for the same customer. (optional)
    publications_create_request_body = {"campaign":{"name":"campaign-name"},"customer":{"source_id":"source-id","Name":"Customer Name","email":"customer email"},"voucher":"voucher-code","metadata":{"key":"value"}} # PublicationsCreateRequestBody | Specify the publication parameters. (optional)

    try:
        # Create Publication
        api_response = api_instance.create_publication(join_once=join_once, publications_create_request_body=publications_create_request_body)
        print("The response of PublicationsApi->create_publication:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->create_publication: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **join_once** | **bool**| Through this flag, you can control if a particular person gets only one and always the same code even if the app sends multiple publication requests. It means that if you have a referral program, a referrer is assigned only to one code if an integration sends publication requests more than once for the same customer. | [optional] 
 **publications_create_request_body** | [**PublicationsCreateRequestBody**](PublicationsCreateRequestBody.md)| Specify the publication parameters. | [optional] 

### Return type

[**PublicationsCreateResponseBody**](PublicationsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a publication object if a valid identifier was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_publication1**
> PublicationsCreateResponseBody create_publication1(customer, join_once=join_once, voucher=voucher, campaign=campaign, source_id=source_id, metadata=metadata)

Create Publication

This method selects vouchers that are suitable for publication, adds a publish entry and returns the publication.  A voucher is suitable for publication when it's active and hasn't been published yet. > ❗️ Limited access > > Access to this endpoint is limited. This endpoint is designed for specific integrations and the API keys need to be configured to access this endpoint. Navigate to the **Dashboard** &rarr; **Project Settings** &rarr; **General** &rarr; **Integration Keys** to set up a pair of API keys and use them to send the request.    <!-- theme: warning --> > 🚧 Clearly define the source of the voucher > > You must clearly define which source you want to publish the voucher code from. It can either be a code from a campaign or a specific voucher identified by a code.   <!-- theme: warning --> > 🚧 Publish multiple vouchers > This endpoint does not support the publishing of multiple vouchers from a single campaign. In case you want to publish multiple vouchers within a single publication, you need to use a [dedicated endpoint](ref:create-publication).    <!-- theme: info -->  > 📘 Auto-update campaign > > In case you want to ensure the number of publishable codes increases automatically with the number of customers, you should use an **auto-update** campaign.    ## Example Request  ```markdown Publication Query  /publications/create?campaign[name]=BlackFriday&customer[source_id]=Customer_Source_ID  ```    <!-- theme: danger --> > ❗️ Required   > > Query param `voucher` OR `campaign` MUST be filled out. If you provide both, `campaign` param will be skipped.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.create_publication_campaign import CreatePublicationCampaign
from voucherify_client.models.publications_create_response_body import PublicationsCreateResponseBody
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
    api_instance = voucherify_client.PublicationsApi(api_client)
    customer = voucherify_client.Customer() # Customer | Contains information about the customer to whom the publication was directed.
    join_once = True # bool | Through this flag, you can control if a particular person gets only one and always the same code even if the app sends multiple publication requests. It means that if you have a referral program, a referrer is assigned only to one code if an integration sends publication requests more than once for the same customer. (optional)
    voucher = 'voucher_example' # str | Code of voucher being published. (optional)
    campaign = voucherify_client.CreatePublicationCampaign() # CreatePublicationCampaign | Create publication with campaign. (optional)
    source_id = 'source_id_example' # str | The merchant’s publication ID if it is different from the Voucherify publication ID. It's an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. If `source_id` is provided only 1 voucher can be published per request. (optional)
    metadata = None # object | The metadata object stores all custom attributes assigned to the publication. A set of key/value pairs that you can attach to a publication object. It can be useful for storing additional information about the publication in a structured format. (optional)

    try:
        # Create Publication
        api_response = api_instance.create_publication1(customer, join_once=join_once, voucher=voucher, campaign=campaign, source_id=source_id, metadata=metadata)
        print("The response of PublicationsApi->create_publication1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->create_publication1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer** | [**Customer**](.md)| Contains information about the customer to whom the publication was directed. | 
 **join_once** | **bool**| Through this flag, you can control if a particular person gets only one and always the same code even if the app sends multiple publication requests. It means that if you have a referral program, a referrer is assigned only to one code if an integration sends publication requests more than once for the same customer. | [optional] 
 **voucher** | **str**| Code of voucher being published. | [optional] 
 **campaign** | [**CreatePublicationCampaign**](.md)| Create publication with campaign. | [optional] 
 **source_id** | **str**| The merchant’s publication ID if it is different from the Voucherify publication ID. It&#39;s an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. If &#x60;source_id&#x60; is provided only 1 voucher can be published per request. | [optional] 
 **metadata** | [**object**](.md)| The metadata object stores all custom attributes assigned to the publication. A set of key/value pairs that you can attach to a publication object. It can be useful for storing additional information about the publication in a structured format. | [optional] 

### Return type

[**PublicationsCreateResponseBody**](PublicationsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a publication object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_publications**
> PublicationsListResponseBody list_publications(limit=limit, page=page, order=order, campaign=campaign, customer=customer, voucher=voucher, result=result, voucher_type=voucher_type, is_referral_code=is_referral_code, filters=filters, source_id=source_id)

List Publications

Retrieve a list of publications. To return a **particular** publication, you can use the `source_id` query parameter and provide the `source_id` of the publication you are looking for specifically.  ## Pagination  <!-- theme: warning --> > 🚧 Important! > > If you want to scroll through a huge set of records, it is recommended to use the <!-- [Exports API](OpenAPI.json/components/schemas/16_obj_export_object) -->[Exports API](ref:create-export). This API will return an error `page_over_limit` if you reach a page above 1000.  ## Filter Query  The `filters` query parameter allows for joining multiple parameters with logical operators. The syntax looks as follows:  <!-- title: \"Filter template\" --> ```url filters[<field_name>][conditions][<operator>][<index>]=<value> ```  ### Operators:  <!-- title: \"Operators\" --> ```     \"$in\"     \"$not_in\"     \"$is\"     \"$is_not\"     \"$has_value\"     \"$is_unknown\"     \"$contains\"     \"$starts_with\"     \"$ends_with\"     \"$more_than\"     \"$less_than\"     \"$more_than_equal\"     \"$less_than_equal\" ```  ### Examples  <!-- title: \"Example 1 - List publications of a given customer\" --> ```url GET /v1/publications?filters[customer_id][conditions][$is][0]=cust_lUET6gRpO5Wxlg5p2j2gRCgL ``` <!-- title: \"Example 2 - List publications of 2 customers\" --> ```url GET /v1/publications?filters[customer_id][conditions][$in][0]=cust_lUET6gRpO5Wxlg5p2j2gRCgL&filters[customer_id][conditions][$in][1]=cust_aR7NfHusxT7PdTMAKMfWDXnc ``` <!-- title: \"Example 3 - List publications of 2 customers using junction operator\" --> ```url GET /v1/publications?filters[customer_id][conditions][$is][0]=cust_lUET6gRpO5Wxlg5p2j2gRCgL&filters[customer_id][conditions][$is][1]=cust_aR7NfHusxT7PdTMAKMfWDXnc&filters[junction]=OR ```

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.parameter_order_list_publications import ParameterOrderListPublications
from voucherify_client.models.parameter_result_list_publications import ParameterResultListPublications
from voucherify_client.models.parameter_voucher_type_list_publications import ParameterVoucherTypeListPublications
from voucherify_client.models.publications_list_response_body import PublicationsListResponseBody
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
    api_instance = voucherify_client.PublicationsApi(api_client)
    limit = 56 # int | A limit on the number of objects to be returned. Limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. (optional)
    order = voucherify_client.ParameterOrderListPublications() # ParameterOrderListPublications | Sorts the results using one of the filtering options, where the dash `-` preceding a sorting option means sorting in a descending order. (optional)
    campaign = 'campaign_example' # str | Filters by a given campaign name. (optional)
    customer = 'customer_example' # str | Filters by a unique customer ID. (optional)
    voucher = 'voucher_example' # str | Filters by a given voucher code. (optional)
    result = voucherify_client.ParameterResultListPublications() # ParameterResultListPublications | Filters by a publication result. (optional)
    voucher_type = voucherify_client.ParameterVoucherTypeListPublications() # ParameterVoucherTypeListPublications | Filters by a voucher type. (optional)
    is_referral_code = True # bool | This filter works only for the `true` option. If set to `true`, the query returns only publications of codes from referral campaigns.  (optional)
    filters = 'filters_example' # str | Allows for combining the filters mentioned in the endpoint description. (optional)
    source_id = 'source_id_example' # str | Using this endpoint with a particular publication `source_id`, which was sent with the original request to create a publication, returns in the response, exactly the same code published initially because the code was assigned to the given publication. As a result, you can use this endpoint as a reference and return a code that was assigned in a publication by using a particular `source_id`. (optional)

    try:
        # List Publications
        api_response = api_instance.list_publications(limit=limit, page=page, order=order, campaign=campaign, customer=customer, voucher=voucher, result=result, voucher_type=voucher_type, is_referral_code=is_referral_code, filters=filters, source_id=source_id)
        print("The response of PublicationsApi->list_publications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicationsApi->list_publications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| A limit on the number of objects to be returned. Limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. | [optional] 
 **order** | [**ParameterOrderListPublications**](.md)| Sorts the results using one of the filtering options, where the dash &#x60;-&#x60; preceding a sorting option means sorting in a descending order. | [optional] 
 **campaign** | **str**| Filters by a given campaign name. | [optional] 
 **customer** | **str**| Filters by a unique customer ID. | [optional] 
 **voucher** | **str**| Filters by a given voucher code. | [optional] 
 **result** | [**ParameterResultListPublications**](.md)| Filters by a publication result. | [optional] 
 **voucher_type** | [**ParameterVoucherTypeListPublications**](.md)| Filters by a voucher type. | [optional] 
 **is_referral_code** | **bool**| This filter works only for the &#x60;true&#x60; option. If set to &#x60;true&#x60;, the query returns only publications of codes from referral campaigns.  | [optional] 
 **filters** | **str**| Allows for combining the filters mentioned in the endpoint description. | [optional] 
 **source_id** | **str**| Using this endpoint with a particular publication &#x60;source_id&#x60;, which was sent with the original request to create a publication, returns in the response, exactly the same code published initially because the code was assigned to the given publication. As a result, you can use this endpoint as a reference and return a code that was assigned in a publication by using a particular &#x60;source_id&#x60;. | [optional] 

### Return type

[**PublicationsListResponseBody**](PublicationsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of publications you’ve previously created with &lt;!-- [create publication](OpenAPI.json/paths/~1publications/post) --&gt;[create publication](ref:create-publication) or implicitly by the distribution manager. The publications are returned in sorted order, with the most recent ones appearing first. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

