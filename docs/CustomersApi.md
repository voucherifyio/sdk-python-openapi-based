# voucherify_client.CustomersApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer**](CustomersApi.md#create_customer) | **POST** /v1/customers | Create Customer
[**customer_permanently_deletion**](CustomersApi.md#customer_permanently_deletion) | **POST** /v1/customers/{customerId}/permanent-deletion | Delete Customer Permanently
[**delete_customer**](CustomersApi.md#delete_customer) | **DELETE** /v1/customers/{customerId} | Delete Customer
[**get_customer**](CustomersApi.md#get_customer) | **GET** /v1/customers/{customerId} | Get Customer
[**import_customers_using_csv**](CustomersApi.md#import_customers_using_csv) | **POST** /v1/customers/importCSV | Import and Update Customers using CSV
[**list_customer_activities**](CustomersApi.md#list_customer_activities) | **GET** /v1/customers/{customerId}/activities | List Customer Activities
[**list_customer_segments**](CustomersApi.md#list_customer_segments) | **GET** /v1/customers/{customerId}/segments | List Customer&#39;s Segments
[**list_customers**](CustomersApi.md#list_customers) | **GET** /v1/customers | List Customers
[**update_customer**](CustomersApi.md#update_customer) | **PUT** /v1/customers/{customerId} | Update Customer
[**update_customers_consents**](CustomersApi.md#update_customers_consents) | **PUT** /v1/customers/{customerId}/consents | Update Customer&#39;s consents
[**update_customers_in_bulk**](CustomersApi.md#update_customers_in_bulk) | **POST** /v1/customers/bulk/async | Update Customers in bulk
[**update_customers_metadata_in_bulk**](CustomersApi.md#update_customers_metadata_in_bulk) | **POST** /v1/customers/metadata/async | Update Customers&#39; Metadata in bulk


# **create_customer**
> CustomersCreateResponseBody create_customer(customers_create_request_body=customers_create_request_body)

Create Customer

Creates a customer object.  <!-- theme: info -->  > 📘 Upsert Mode > > If you pass an `id` or a `source_id` that already exists in the customer database, Voucherify will return a related customer object with updated fields.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.customers_create_request_body import CustomersCreateRequestBody
from voucherify_client.models.customers_create_response_body import CustomersCreateResponseBody
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
    api_instance = voucherify_client.CustomersApi(api_client)
    customers_create_request_body = {"source_id":"source_123","name":"Bob Smith","description":"A frequent customer","email":"bob.smith@email.com","phone":"+1 933 222 3333","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthdate":"2022-01-01"} # CustomersCreateRequestBody | Create a customer with specified parameters. (optional)

    try:
        # Create Customer
        api_response = api_instance.create_customer(customers_create_request_body=customers_create_request_body)
        print("The response of CustomersApi->create_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customers_create_request_body** | [**CustomersCreateRequestBody**](CustomersCreateRequestBody.md)| Create a customer with specified parameters. | [optional] 

### Return type

[**CustomersCreateResponseBody**](CustomersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a customer object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_permanently_deletion**
> CustomersPermanentDeletionCreateResponseBody customer_permanently_deletion(customer_id)

Delete Customer Permanently

The organization user can remove consumer data permanently from the Voucherify system by using this API method. It d​eletes all customer data and connected resources. It makes the customer profile forgotten by Voucherify.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.customers_permanent_deletion_create_response_body import CustomersPermanentDeletionCreateResponseBody
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
    api_instance = voucherify_client.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify customer's `id` or `source_id`.

    try:
        # Delete Customer Permanently
        api_response = api_instance.customer_permanently_deletion(customer_id)
        print("The response of CustomersApi->customer_permanently_deletion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customer_permanently_deletion: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify customer&#39;s &#x60;id&#x60; or &#x60;source_id&#x60;. | 

### Return type

[**CustomersPermanentDeletionCreateResponseBody**](CustomersPermanentDeletionCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a permanent deletion object and status of the deletion. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer**
> delete_customer(customer_id)

Delete Customer

This method deletes a customer.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
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
    api_instance = voucherify_client.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify customer's `id` or `source_id`.

    try:
        # Delete Customer
        api_instance.delete_customer(customer_id)
    except Exception as e:
        print("Exception when calling CustomersApi->delete_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify customer&#39;s &#x60;id&#x60; or &#x60;source_id&#x60;. | 

### Return type

void (empty response body)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns no content if deletion is successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer**
> CustomersGetResponseBody get_customer(customer_id)

Get Customer

Retrieve customer details.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.customers_get_response_body import CustomersGetResponseBody
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
    api_instance = voucherify_client.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify customer's `id` or `source_id`.

    try:
        # Get Customer
        api_response = api_instance.get_customer(customer_id)
        print("The response of CustomersApi->get_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->get_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify customer&#39;s &#x60;id&#x60; or &#x60;source_id&#x60;. | 

### Return type

[**CustomersGetResponseBody**](CustomersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a customer object if a valid identifier was provided. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_customers_using_csv**
> CustomersImportCsvCreateResponseBody import_customers_using_csv(file)

Import and Update Customers using CSV

This API method lets you import or update customer data. To get a proper and valid response, please send a CSV file with data separated by commas.    ## Request Example <!-- title: \"Example Request\" lineNumbers: true --> ```cURL curl -X POST \\   https://api.voucherify.io/v1/customers/importCSV \\   -F file=@/path/to/customers.csv \\   -H \"X-App-Id: c70a6f00-cf91-4756-9df5-47628850002b\" \\   -H \"X-App-Token: 3266b9f8-e246-4f79-bdf0-833929b1380c\" ``` ## CSV File Format  The CSV file has to include headers in the first line. All properties which cannot be mapped to standard customer fields will be added to the metadata object.  <!-- theme: info --> > 📘 Standard customer fields mapping > > **No spaces allowed in field names**   > Id, Name, Email, Phone, Birthdate, Source_id, Address_line_1, Address_line_2, Address_Postal_Code, Address_City, Address_State, Address_Country, Description, Metadata_name_1, Metadata_name_2  ## Update Customers using CSV  If you would like to update customer's data, you can do it using the CSV file with new data. However, remember to include a `source_id` in your CSV file to manage the update successfully.  This API request starts a process that affects Voucherify data in bulk.   In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the `IN_PROGRESS` status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.   The result will return the async ID. You can verify the status of your request via this [API request](ref:get-async-action).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.customers_import_csv_create_response_body import CustomersImportCsvCreateResponseBody
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
    api_instance = voucherify_client.CustomersApi(api_client)
    file = None # bytearray | File path.

    try:
        # Import and Update Customers using CSV
        api_response = api_instance.import_customers_using_csv(file)
        print("The response of CustomersApi->import_customers_using_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->import_customers_using_csv: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| File path. | 

### Return type

[**CustomersImportCsvCreateResponseBody**](CustomersImportCsvCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Returns ID of the scheduled async action. The response informs you that your request has been accepted and customers will be added to the repository asynchronously. To check the import status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using the &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_activities**
> CustomersActivitiesListResponseBody list_customer_activities(customer_id, limit=limit, order=order, starting_after=starting_after, starting_after_id=starting_after_id, campaign_type=campaign_type, campaign_id=campaign_id, product_id=product_id, start_date=start_date, end_date=end_date)

List Customer Activities

Retrieve customer activities.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.customers_activities_list_response_body import CustomersActivitiesListResponseBody
from voucherify_client.models.parameter_campaign_type import ParameterCampaignType
from voucherify_client.models.parameter_order import ParameterOrder
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
    api_instance = voucherify_client.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify customer's `id` or source ID of the customer who performed the activities.
    limit = 56 # int | A limit on the number of objects to be returned. Limit can range between 1 and 100 items. (optional)
    order = voucherify_client.ParameterOrder() # ParameterOrder | Sorts the results using one of the filtering options, where the dash `-` preceding a sorting option means sorting in a descending order. (optional)
    starting_after = '2013-10-20T19:20:30+01:00' # datetime | A cursor for use in pagination. `starting_after` is a date-time value that defines your place in the list based on `created_at` property from the activity object. For instance, if you make a list request and receive 100 objects, ending with an object created at `2020-05-24T13:43:09.024Z`, your subsequent call can include `starting_after=2020-05-24T13:43:09.024Z` in order to fetch the next page of the list. (optional)
    starting_after_id = 'starting_after_id_example' # str | By applying this filter value, you will get events starting after an event with the given ID. (optional)
    campaign_type = voucherify_client.ParameterCampaignType() # ParameterCampaignType | Through this parameter you can control a type of campaign by which Voucherify will filter related customer's activity. API will return only records related to that given type. Allowed values: DISCOUNT_COUPONS, REFERRAL_PROGRAM, GIFT_VOUCHERS, PROMOTION, LOYALTY_PROGRAM (optional)
    campaign_id = 'campaign_id_example' # str | By applying this parameter you request only events related to specific campaign identified by its ID. (optional)
    product_id = 'product_id_example' # str | By applying this parameter you request only events related to specific product identified by its ID. (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. (optional)

    try:
        # List Customer Activities
        api_response = api_instance.list_customer_activities(customer_id, limit=limit, order=order, starting_after=starting_after, starting_after_id=starting_after_id, campaign_type=campaign_type, campaign_id=campaign_id, product_id=product_id, start_date=start_date, end_date=end_date)
        print("The response of CustomersApi->list_customer_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->list_customer_activities: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify customer&#39;s &#x60;id&#x60; or source ID of the customer who performed the activities. | 
 **limit** | **int**| A limit on the number of objects to be returned. Limit can range between 1 and 100 items. | [optional] 
 **order** | [**ParameterOrder**](.md)| Sorts the results using one of the filtering options, where the dash &#x60;-&#x60; preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after** | **datetime**| A cursor for use in pagination. &#x60;starting_after&#x60; is a date-time value that defines your place in the list based on &#x60;created_at&#x60; property from the activity object. For instance, if you make a list request and receive 100 objects, ending with an object created at &#x60;2020-05-24T13:43:09.024Z&#x60;, your subsequent call can include &#x60;starting_after&#x3D;2020-05-24T13:43:09.024Z&#x60; in order to fetch the next page of the list. | [optional] 
 **starting_after_id** | **str**| By applying this filter value, you will get events starting after an event with the given ID. | [optional] 
 **campaign_type** | [**ParameterCampaignType**](.md)| Through this parameter you can control a type of campaign by which Voucherify will filter related customer&#39;s activity. API will return only records related to that given type. Allowed values: DISCOUNT_COUPONS, REFERRAL_PROGRAM, GIFT_VOUCHERS, PROMOTION, LOYALTY_PROGRAM | [optional] 
 **campaign_id** | **str**| By applying this parameter you request only events related to specific campaign identified by its ID. | [optional] 
 **product_id** | **str**| By applying this parameter you request only events related to specific product identified by its ID. | [optional] 
 **start_date** | **datetime**| Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. | [optional] 
 **end_date** | **datetime**| Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. | [optional] 

### Return type

[**CustomersActivitiesListResponseBody**](CustomersActivitiesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a dictionary with customer activities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_segments**
> CustomersSegmentsListResponseBody list_customer_segments(customer_id)

List Customer's Segments

Returns the list of segments IDs to which the customer belongs to.    If you pass a `customerId` which is not stored and recognized by Voucherify as an existing customer in the system, the response will generate a list of segments that the customer would potentialy qualify for if they were to become a customer tracked in the system.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.customers_segments_list_response_body import CustomersSegmentsListResponseBody
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
    api_instance = voucherify_client.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | Unique identifier of a customer represented by an internal customer ID or customer source ID.

    try:
        # List Customer's Segments
        api_response = api_instance.list_customer_segments(customer_id)
        print("The response of CustomersApi->list_customer_segments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->list_customer_segments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Unique identifier of a customer represented by an internal customer ID or customer source ID. | 

### Return type

[**CustomersSegmentsListResponseBody**](CustomersSegmentsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The method returns segment(s) to which the given customer belongs to. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customers**
> CustomersListResponseBody list_customers(limit=limit, page=page, email=email, city=city, name=name, segment_id=segment_id, created_at_before=created_at_before, created_at_after=created_at_after, updated_at_before=updated_at_before, updated_at_after=updated_at_after, order=order, starting_after=starting_after)

List Customers

Returns a list of customers.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.customers_list_response_body import CustomersListResponseBody
from voucherify_client.models.parameter_order_list_customers import ParameterOrderListCustomers
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
    api_instance = voucherify_client.CustomersApi(api_client)
    limit = 56 # int | A limit on the number of objects to be returned. Limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. (optional)
    email = 'email_example' # str | Limit the customers to the ones that have this specific email address. (optional)
    city = 'city_example' # str | Limit the customers to the ones that are located in the specified city. (optional)
    name = 'name_example' # str | Filter customers by the name property. (optional)
    segment_id = 'segment_id_example' # str | Filter customers by the segment id. (optional)
    created_at_before = '2013-10-20T19:20:30+01:00' # datetime | Filter customers by date customer was created. (optional)
    created_at_after = '2013-10-20T19:20:30+01:00' # datetime | Filter customers by date customer was created. (optional)
    updated_at_before = '2013-10-20T19:20:30+01:00' # datetime | Filter customers by date customer was updated last time. (optional)
    updated_at_after = '2013-10-20T19:20:30+01:00' # datetime | Filter customers by date customer was updated last time. (optional)
    order = voucherify_client.ParameterOrderListCustomers() # ParameterOrderListCustomers | This is a property that controls the sorting direction of the results. Sort the results using one of the filtering options, where the dash `-` preceding a sorting option means sorting in a descending order. (optional)
    starting_after = '2013-10-20T19:20:30+01:00' # datetime | A cursor for use in pagination. This is a date-time value that defines your place in the list based on `created_at` property from the customer object. For instance, if you make a list request and receive 100 objects, ending with an object created at `2020-05-24T13:43:09.024Z`, your subsequent call can include `starting_after=2020-05-24T13:43:09.024Z` in order to fetch the next page of the list.  <!-- title: Options --> | **Option** | **Format** | **Sorting** | |:---|:---|:---| | Return customers **before** a specific creation date  | - set `starting_after` parameter to the breakpoint date | Sorting order is **descending**; the most recent dates first and least recent dates last. | | Return customers **after** a specific create or update date | - include the `order` parameter set to `created_at` or `updated_at`<br>- set `starting_after` to the breakpoint date | Sorting order is **ascending**; the least recent dates first and the most recent dates last. |  (optional)

    try:
        # List Customers
        api_response = api_instance.list_customers(limit=limit, page=page, email=email, city=city, name=name, segment_id=segment_id, created_at_before=created_at_before, created_at_after=created_at_after, updated_at_before=updated_at_before, updated_at_after=updated_at_after, order=order, starting_after=starting_after)
        print("The response of CustomersApi->list_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->list_customers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| A limit on the number of objects to be returned. Limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. | [optional] 
 **email** | **str**| Limit the customers to the ones that have this specific email address. | [optional] 
 **city** | **str**| Limit the customers to the ones that are located in the specified city. | [optional] 
 **name** | **str**| Filter customers by the name property. | [optional] 
 **segment_id** | **str**| Filter customers by the segment id. | [optional] 
 **created_at_before** | **datetime**| Filter customers by date customer was created. | [optional] 
 **created_at_after** | **datetime**| Filter customers by date customer was created. | [optional] 
 **updated_at_before** | **datetime**| Filter customers by date customer was updated last time. | [optional] 
 **updated_at_after** | **datetime**| Filter customers by date customer was updated last time. | [optional] 
 **order** | [**ParameterOrderListCustomers**](.md)| This is a property that controls the sorting direction of the results. Sort the results using one of the filtering options, where the dash &#x60;-&#x60; preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after** | **datetime**| A cursor for use in pagination. This is a date-time value that defines your place in the list based on &#x60;created_at&#x60; property from the customer object. For instance, if you make a list request and receive 100 objects, ending with an object created at &#x60;2020-05-24T13:43:09.024Z&#x60;, your subsequent call can include &#x60;starting_after&#x3D;2020-05-24T13:43:09.024Z&#x60; in order to fetch the next page of the list.  &lt;!-- title: Options --&gt; | **Option** | **Format** | **Sorting** | |:---|:---|:---| | Return customers **before** a specific creation date  | - set &#x60;starting_after&#x60; parameter to the breakpoint date | Sorting order is **descending**; the most recent dates first and least recent dates last. | | Return customers **after** a specific create or update date | - include the &#x60;order&#x60; parameter set to &#x60;created_at&#x60; or &#x60;updated_at&#x60;&lt;br&gt;- set &#x60;starting_after&#x60; to the breakpoint date | Sorting order is **ascending**; the least recent dates first and the most recent dates last. |  | [optional] 

### Return type

[**CustomersListResponseBody**](CustomersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a dictionary with customer objects. The customers are returned sorted by creation date, with the most recent customers appearing first. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer**
> CustomersUpdateResponseBody update_customer(customer_id, customers_update_request_body=customers_update_request_body)

Update Customer

Updates the specified customer by setting the values of the parameters passed in the request body. Any parameters not provided in the payload will be left unchanged.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.customers_update_request_body import CustomersUpdateRequestBody
from voucherify_client.models.customers_update_response_body import CustomersUpdateResponseBody
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
    api_instance = voucherify_client.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify customer's `id` or `source_id`.
    customers_update_request_body = {"name":"Alice McDonald","email":"alice.mdconald@email.com","description":"Updating customer data","phone":"+1 (132) 222-2222","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthdate":"2022-01-01","birthday":"2022-01-02"} # CustomersUpdateRequestBody | Specify the parameters to be updated. (optional)

    try:
        # Update Customer
        api_response = api_instance.update_customer(customer_id, customers_update_request_body=customers_update_request_body)
        print("The response of CustomersApi->update_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->update_customer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify customer&#39;s &#x60;id&#x60; or &#x60;source_id&#x60;. | 
 **customers_update_request_body** | [**CustomersUpdateRequestBody**](CustomersUpdateRequestBody.md)| Specify the parameters to be updated. | [optional] 

### Return type

[**CustomersUpdateResponseBody**](CustomersUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a customer object if updates were successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customers_consents**
> update_customers_consents(customer_id, body=body)

Update Customer's consents

Update marketing permissions for the specified customer.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
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
    api_instance = voucherify_client.CustomersApi(api_client)
    customer_id = 'customer_id_example' # str | A Voucherify unique customer identifier or source ID.
    body = {"cnst_6jQ5XcUOLnj5L7ImQAdBsJ1I":true,"cnst_VCmucIvAsmDYw2PPAok6bcYy":false} # object | Key-value pairs where the key is the consent identifier and value is a boolean that identifies if a customer has given the consent or not. To deny all consents use \"unsubscribed\" as a consent identifier and \"true\" as its value.    #### Examples  <!-- title: \"Request Body\" lineNumbers: true --> ```json {     \"cnst_aIdUulAh0SCsOCaS3005y7yS\": true,     \"cnst_aIdUulAhwewqaS31213fdsfds\": false } ```  Opt-out from all communication:  <!-- title: \"Request Body\" lineNumbers: true --> ```json {     \"unsubscribed\": true } ``` (optional)

    try:
        # Update Customer's consents
        api_instance.update_customers_consents(customer_id, body=body)
    except Exception as e:
        print("Exception when calling CustomersApi->update_customers_consents: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| A Voucherify unique customer identifier or source ID. | 
 **body** | **object**| Key-value pairs where the key is the consent identifier and value is a boolean that identifies if a customer has given the consent or not. To deny all consents use \&quot;unsubscribed\&quot; as a consent identifier and \&quot;true\&quot; as its value.    #### Examples  &lt;!-- title: \&quot;Request Body\&quot; lineNumbers: true --&gt; &#x60;&#x60;&#x60;json {     \&quot;cnst_aIdUulAh0SCsOCaS3005y7yS\&quot;: true,     \&quot;cnst_aIdUulAhwewqaS31213fdsfds\&quot;: false } &#x60;&#x60;&#x60;  Opt-out from all communication:  &lt;!-- title: \&quot;Request Body\&quot; lineNumbers: true --&gt; &#x60;&#x60;&#x60;json {     \&quot;unsubscribed\&quot;: true } &#x60;&#x60;&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returns no content if the consents were updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customers_in_bulk**
> CustomersUpdateInBulkResponseBody update_customers_in_bulk(customers_update_in_bulk_request_body=customers_update_in_bulk_request_body)

Update Customers in bulk

Update several customers in one asynchronous operation.   In one request, it is possible to update a maximum of **100** records. In the response body, you get a unique async action identifier.    If a requested customer object is not found, then an **upsert** occurs. This is reflected in the <!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) -->[Get Async Action](ref:get-async-action) endpoint as follows:    <!-- title: \"Response\" lineNumbers: true --> ```json {     \"found\": false,     \"updated\": true } ```  This API request starts a process that affects Voucherify data in bulk.   In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the `IN_PROGRESS` status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.   The result will return the async ID. You can verify the status of your request via this [API request](ref:get-async-action).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.customers_update_in_bulk_request_body import CustomersUpdateInBulkRequestBody
from voucherify_client.models.customers_update_in_bulk_response_body import CustomersUpdateInBulkResponseBody
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
    api_instance = voucherify_client.CustomersApi(api_client)
    customers_update_in_bulk_request_body = [{"source_id":"John.Smith@email.com","name":"John Smith","email":"john.smith@email.com","description":"Updating customer data","phone":"+1 (132) 222-2222","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthday":"2022-04-04"},{"source_id":"Jane.Smith@email.com","name":"Jane Smith","email":"Jane.Smith@email.com","description":"Updating customer data","phone":"+1 (132) 222-2222","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthday":"2022-03-03"},{"source_id":"Sally.Smith@email.com","name":"Sally Smith","email":"Sally.Smith@email.com","description":"Updating customer data","phone":"+1 (132) 222-2222","address":{"city":"New York","country":"United States","line_1":"123 Main St.","line_2":"APT 3 BLG 4","postal_code":"10001","state":"NY"},"metadata":{"lang":"en","test":true},"birthdate":"2022-02-02"}] # List[CustomersUpdateInBulkRequestBody] | Specify the customer fields that you would like to update in each customer object. (optional)

    try:
        # Update Customers in bulk
        api_response = api_instance.update_customers_in_bulk(customers_update_in_bulk_request_body=customers_update_in_bulk_request_body)
        print("The response of CustomersApi->update_customers_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->update_customers_in_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customers_update_in_bulk_request_body** | [**List[CustomersUpdateInBulkRequestBody]**](CustomersUpdateInBulkRequestBody.md)| Specify the customer fields that you would like to update in each customer object. | [optional] 

### Return type

[**CustomersUpdateInBulkResponseBody**](CustomersUpdateInBulkResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Returns ID of the scheduled async action. The response informs you that your request has been accepted and customers will be updated in the repository asynchronously. To check the update status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using the &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customers_metadata_in_bulk**
> CustomersMetadataUpdateInBulkResponseBody update_customers_metadata_in_bulk(customers_metadata_update_in_bulk_request_body=customers_metadata_update_in_bulk_request_body)

Update Customers' Metadata in bulk

Update several customers metadata properties in one asynchronous operation.   In one request, it is possible to update a maximum of **100** records. In the response body, you get a unique async action identifier.    If a requested customer object is not found, then an **upsert** occurs. This is reflected in the <!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) -->[Get Async Action](ref:get-async-action) endpoint as follows:    <!-- title: \"Response\" lineNumbers: true --> ```json {     \"found\": false,     \"updated\": true } ```  This API request starts a process that affects Voucherify data in bulk.   In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the `IN_PROGRESS` status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.   The result will return the async ID. You can verify the status of your request via this [API request](ref:get-async-action).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.customers_metadata_update_in_bulk_request_body import CustomersMetadataUpdateInBulkRequestBody
from voucherify_client.models.customers_metadata_update_in_bulk_response_body import CustomersMetadataUpdateInBulkResponseBody
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
    api_instance = voucherify_client.CustomersApi(api_client)
    customers_metadata_update_in_bulk_request_body = {"source_ids":["source_123","source_456"],"metadata":{"lang":"en","test":false}} # CustomersMetadataUpdateInBulkRequestBody | List the `source_ids` of the customer's you would like to update along with the metadata key value pairs. (optional)

    try:
        # Update Customers' Metadata in bulk
        api_response = api_instance.update_customers_metadata_in_bulk(customers_metadata_update_in_bulk_request_body=customers_metadata_update_in_bulk_request_body)
        print("The response of CustomersApi->update_customers_metadata_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->update_customers_metadata_in_bulk: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customers_metadata_update_in_bulk_request_body** | [**CustomersMetadataUpdateInBulkRequestBody**](CustomersMetadataUpdateInBulkRequestBody.md)| List the &#x60;source_ids&#x60; of the customer&#39;s you would like to update along with the metadata key value pairs. | [optional] 

### Return type

[**CustomersMetadataUpdateInBulkResponseBody**](CustomersMetadataUpdateInBulkResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Returns ID of the scheduled async action. The response informs you that your request has been accepted and customers will be updated in the repository asynchronously. To check the update status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using the &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

