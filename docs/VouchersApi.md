# voucherify_client.VouchersApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_voucher**](VouchersApi.md#delete_voucher) | **DELETE** /v1/vouchers/{code} | Delete Voucher
[**disable_voucher**](VouchersApi.md#disable_voucher) | **POST** /v1/vouchers/{code}/disable | Disable Voucher
[**enable_voucher**](VouchersApi.md#enable_voucher) | **POST** /v1/vouchers/{code}/enable | Enable Voucher
[**export_voucher_transactions**](VouchersApi.md#export_voucher_transactions) | **POST** /v1/vouchers/{code}/transactions/export | Export Voucher Transactions
[**get_voucher**](VouchersApi.md#get_voucher) | **GET** /v1/vouchers/{code} | Get Voucher
[**import_vouchers_using_csv**](VouchersApi.md#import_vouchers_using_csv) | **POST** /v1/vouchers/importCSV | Import Vouchers using CSV
[**list_voucher_transactions**](VouchersApi.md#list_voucher_transactions) | **GET** /v1/vouchers/{code}/transactions | List Voucher Transactions
[**release_validation_session**](VouchersApi.md#release_validation_session) | **DELETE** /v1/vouchers/{code}/sessions/{sessionKey} | Release Validation Session
[**update_voucher_balance**](VouchersApi.md#update_voucher_balance) | **POST** /v1/vouchers/{code}/balance | Add or Remove Voucher Balance


# **delete_voucher**
> delete_voucher(code, force=force)

Delete Voucher

Deletes a voucher. This operation cannot be undone. Additionally, this operation removes any redemptions on the voucher.

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
    api_instance = voucherify_client.VouchersApi(api_client)
    code = 'code_example' # str | A unique **code** that identifies the voucher.
    force = True # bool | If this flag is set to `true`, the voucher will be removed permanently. Going forward, the user will be able to create another voucher with exactly the same code. (optional)

    try:
        # Delete Voucher
        api_instance.delete_voucher(code, force=force)
    except Exception as e:
        print("Exception when calling VouchersApi->delete_voucher: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A unique **code** that identifies the voucher. | 
 **force** | **bool**| If this flag is set to &#x60;true&#x60;, the voucher will be removed permanently. Going forward, the user will be able to create another voucher with exactly the same code. | [optional] 

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

# **disable_voucher**
> VouchersDisableResponseBody disable_voucher(code)

Disable Voucher

There are various times when you'll want to manage a voucher's accessibility. This can be done by two API methods for managing the voucher state - *enable* and *disable*.   ___ This method sets the voucher state to **inactive**. The voucher cannot be redeemed.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.vouchers_disable_response_body import VouchersDisableResponseBody
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
    api_instance = voucherify_client.VouchersApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. `v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u`.

    try:
        # Disable Voucher
        api_response = api_instance.disable_voucher(code)
        print("The response of VouchersApi->disable_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->disable_voucher: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. &#x60;v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u&#x60;. | 

### Return type

[**VouchersDisableResponseBody**](VouchersDisableResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a voucher object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_voucher**
> VouchersEnableResponseBody enable_voucher(code)

Enable Voucher

There are various times when you'll want to manage a voucher's accessibility. This can be done by two API methods for managing the voucher state - *enable* and *disable*.   ___ The method sets the voucher state to **active**. The voucher can be redeemed - only if the redemption occurs after the start date and the voucher is not expired.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.vouchers_enable_response_body import VouchersEnableResponseBody
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
    api_instance = voucherify_client.VouchersApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. `v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u`.

    try:
        # Enable Voucher
        api_response = api_instance.enable_voucher(code)
        print("The response of VouchersApi->enable_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->enable_voucher: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. &#x60;v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u&#x60;. | 

### Return type

[**VouchersEnableResponseBody**](VouchersEnableResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a voucher object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_voucher_transactions**
> VouchersTransactionsExportCreateResponseBody export_voucher_transactions(code, vouchers_transactions_export_create_request_body=vouchers_transactions_export_create_request_body)

Export Voucher Transactions

Export transactions that are associated with credit movements on a gift card or loyalty card.  | **Field** | **Definition** | **Example Export** | |:---|:---|:---| | id | Unique transaction ID. | vtx_0cb7811f1c07765800 | | type | Transaction type. | - `CREDITS_REMOVAL` <br> - `CREDITS_ADDITION` <br> - `CREDITS_REFUND` <br> - `CREDITS_REDEMPTION` <br> - `POINTS_ACCRUAL` <br> - `POINTS_CANCELLATION` <br> - `POINTS_REDEMPTION`<br> - `POINTS_REFUND`<br> - `POINTS_ADDITION`<br> - `POINTS_REMOVAL`<br> - `POINTS_EXPIRATION`<br> - `POINTS_TRANSFER_IN`<br> - `POINTS_TRANSFER_OUT` | | source_id | Unique transaction source ID. | 8638 | | reason | Contains the reason for the transaction if one was included originally. |  | | balance | The gift card or loyalty card balance after the transaction. |  | | amount | The amount of gift card or loyalty card credits being allocated during the transaction. This value can either be negative or positive depending on the nature of the transaction. |  | | created_at | Timestamp in ISO 8601 format representing the date and time when the transaction was created. | 2022-03-09T09:16:32.521Z  | | voucher_id | Unique Voucher ID. | v_dky7ksKfPX50Wb2Bxvcoeb1xT20b6tcp | | campaign_id | Parent campaign ID. | camp_FNYR4jhqZBM9xTptxDGgeNBV | | source|  Channel through which the transaction was initiated. | API | | details | More detailed information stored in the form of a JSON. | Provides more details related to the transaction in the form of an object. | | related_transaction_id | Unique transaction ID related to a receiver/donor card in the case of a points transfer from/to another card. | vtx_0c9afe802593b34b80 |

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.vouchers_transactions_export_create_request_body import VouchersTransactionsExportCreateRequestBody
from voucherify_client.models.vouchers_transactions_export_create_response_body import VouchersTransactionsExportCreateResponseBody
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
    api_instance = voucherify_client.VouchersApi(api_client)
    code = 'GIFT-CARD-1' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. `v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u`.
    vouchers_transactions_export_create_request_body = {"parameters":{"order":"-created_at","fields":["id","type","source_id","reason","balance","amount","created_at","voucher_id","campaign_id","details","source"]}} # VouchersTransactionsExportCreateRequestBody | Specify the parameters for the transaction export. (optional)

    try:
        # Export Voucher Transactions
        api_response = api_instance.export_voucher_transactions(code, vouchers_transactions_export_create_request_body=vouchers_transactions_export_create_request_body)
        print("The response of VouchersApi->export_voucher_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->export_voucher_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. &#x60;v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u&#x60;. | 
 **vouchers_transactions_export_create_request_body** | [**VouchersTransactionsExportCreateRequestBody**](VouchersTransactionsExportCreateRequestBody.md)| Specify the parameters for the transaction export. | [optional] 

### Return type

[**VouchersTransactionsExportCreateResponseBody**](VouchersTransactionsExportCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an export object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voucher**
> VouchersGetResponseBody get_voucher(code)

Get Voucher

Retrieves the voucher with the given `code` or unique Voucherify ID. You can either pass the voucher ID which was assigned by Voucherify, e.g., `v_7HxHkf4VAkMuc8u4lZs78lyRwhRze5UE`, or the `code` of the voucher as the path parameter value, e.g., `7fjWdr`.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.vouchers_get_response_body import VouchersGetResponseBody
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
    api_instance = voucherify_client.VouchersApi(api_client)
    code = 'code_example' # str | A unique **code** that identifies the voucher.

    try:
        # Get Voucher
        api_response = api_instance.get_voucher(code)
        print("The response of VouchersApi->get_voucher:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->get_voucher: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A unique **code** that identifies the voucher. | 

### Return type

[**VouchersGetResponseBody**](VouchersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a voucher object if a valid identifier was provided.   Additionally, the response returns validation rules related to the voucher object. They can be inherited from a campaign. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vouchers_using_csv**
> VouchersImportCsvCreateResponseBody import_vouchers_using_csv(file)

Import Vouchers using CSV

Import standalone vouchers into the repository using a CSV file.  The CSV file has to include headers in the first line. All properties listed in the file headers that cannot be mapped to standard voucher fields will be added to the metadata object.    You can find an example CSV file [here](https://support.voucherify.io/article/45-import-codes-and-share-them-digitally#coupons). ___ <!-- title: \"cURL Example Request\" lineNumbers: true --> ```cURL cURL example curl -X POST \\   https://api.voucherify.io/v1/vouchers/importCSV \\   -F file=@/path/to/vouchers.csv \\   -H \"X-App-Id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\" \\   -H \"X-App-Token: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\" ```  <!-- theme: info -->  > 📘 Standard voucher fields mapping > > - Go to the <!-- [import vouchers](OpenAPI.json/paths/~1vouchers~1import) -->[import vouchers](ref:import-vouchers) endpoint to see all standard CSV fields description (body params section). > - Supported CSV file headers: Code,Voucher Type,Value,Discount Type,Category,Start Date,Expiration Date,Redemption Limit,Redeemed Quantity, Redeemed Amount,Active,Additional Info,Custom Metadata Property Name >- **Start and expiration dates** need to be provided in compliance with the ISO 8601 norms. For example, 2020-03-11T09:00:00.000Z.   >    - `YYYY-MM-DD` >    - `YYYY-MM-DDTHH` >    - `YYYY-MM-DDTHH:mm` >    - `YYYY-MM-DDTHH:mm:ss` >    - `YYYY-MM-DDTHH:mm:ssZ` >    - `YYYY-MM-DDTHH:mm:ssZ` >    - `YYYY-MM-DDTHH:mm:ss.SSSZ` > - Custom code attributes (not supported by-default) need to be added as code **metadata**. > - You **cannot import the same codes** to a single Voucherify Project.  <!-- theme: info -->  > 📘 Categories > > In the structure representing your data, you can define a category that the voucher belongs to. You can later use the category of a voucher to group and search by specific criteria in the Dashboard and using the [List Vouchers](ref:list-vouchers) endpoint.  This API request starts a process that affects Voucherify data in bulk.   In case of small jobs (like bulk update) the request is put into a queue and processed once every other bulk request placed in the queue prior to this request is finished. However, when the job takes a longer time (like vouchers generation) then it is processed in small portions in a round-robin fashion. When there is a list of vouchers generation scheduled, then they will all have the `IN_PROGRESS` status shortly. This way, small jobs added just after scheduling big jobs of the same type will be processed in a short time window.   The result will return the async ID. You can verify the status of your request via this [API request](ref:get-async-action).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.vouchers_import_csv_create_response_body import VouchersImportCsvCreateResponseBody
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
    api_instance = voucherify_client.VouchersApi(api_client)
    file = None # bytearray | File path.

    try:
        # Import Vouchers using CSV
        api_response = api_instance.import_vouchers_using_csv(file)
        print("The response of VouchersApi->import_vouchers_using_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->import_vouchers_using_csv: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| File path. | 

### Return type

[**VouchersImportCsvCreateResponseBody**](VouchersImportCsvCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Returns ID of the scheduled async action. The response informs you that your request has been accepted and vouchers will be added to the repository asynchronously. To check the import status and result, copy the &#x60;async_action_id&#x60; from the **response** and pass it using the &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_voucher_transactions**
> VouchersTransactionsListResponseBody list_voucher_transactions(code, limit=limit, page=page)

List Voucher Transactions

List transactions that are associated with credit movements on a gift card or loyalty card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.vouchers_transactions_list_response_body import VouchersTransactionsListResponseBody
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
    api_instance = voucherify_client.VouchersApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. `v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u`.
    limit = 56 # int | A limit on the number of objects to be returned. Limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. (optional)

    try:
        # List Voucher Transactions
        api_response = api_instance.list_voucher_transactions(code, limit=limit, page=page)
        print("The response of VouchersApi->list_voucher_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->list_voucher_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. &#x60;v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u&#x60;. | 
 **limit** | **int**| A limit on the number of objects to be returned. Limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. | [optional] 

### Return type

[**VouchersTransactionsListResponseBody**](VouchersTransactionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a dictionary of transaction objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_validation_session**
> release_validation_session(code, session_key)

Release Validation Session

Manually release a validation session that has been set up for the voucher. This method undos the actions that are explained in our guide on how a validation session was established, you can read more [here](doc:locking-validation-session).   > 📘 Release Session using Dashboard > > You can also use the Validations Manager in the Dashboard to unlock sessions. [Read more](https://support.voucherify.io/article/16-dashboard-sections#validations).

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
    api_instance = voucherify_client.VouchersApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify.
    session_key = 'ssn_yQGMTeKBSw8OOuFPwlBEjzGy8d8VA9Ts' # str | A unique session identifier.

    try:
        # Release Validation Session
        api_instance.release_validation_session(code, session_key)
    except Exception as e:
        print("Exception when calling VouchersApi->release_validation_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify. | 
 **session_key** | **str**| A unique session identifier. | 

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
**204** | Returns no content if the validation session was released successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_voucher_balance**
> VouchersBalanceUpdateResponseBody update_voucher_balance(code, vouchers_balance_update_request_body)

Add or Remove Voucher Balance

Add balance to an existing gift card or loyalty card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.vouchers_balance_update_request_body import VouchersBalanceUpdateRequestBody
from voucherify_client.models.vouchers_balance_update_response_body import VouchersBalanceUpdateResponseBody
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
    api_instance = voucherify_client.VouchersApi(api_client)
    code = 'code_example' # str | A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. `v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u`.
    vouchers_balance_update_request_body = {"amount":10000} # VouchersBalanceUpdateRequestBody | Provide the amount to be added to/subtracted from the voucher.

    try:
        # Add or Remove Voucher Balance
        api_response = api_instance.update_voucher_balance(code, vouchers_balance_update_request_body)
        print("The response of VouchersApi->update_voucher_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VouchersApi->update_voucher_balance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| A **code** that identifies the voucher or a unique voucher ID assigned by Voucherify, i.e. &#x60;v_TzD19aeNiqGc9LWciMWknyEZT8IW7u4u&#x60;. | 
 **vouchers_balance_update_request_body** | [**VouchersBalanceUpdateRequestBody**](VouchersBalanceUpdateRequestBody.md)| Provide the amount to be added to/subtracted from the voucher. | 

### Return type

[**VouchersBalanceUpdateResponseBody**](VouchersBalanceUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a balance object if the operation succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

