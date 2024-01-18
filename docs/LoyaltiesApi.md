# voucherify_client.LoyaltiesApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_in_bulk_loyalty_tiers**](LoyaltiesApi.md#create_in_bulk_loyalty_tiers) | **POST** /v1/loyalties/{campaignId}/tiers | Create loyalty tiers
[**delete_earning_rule**](LoyaltiesApi.md#delete_earning_rule) | **DELETE** /v1/loyalties/{campaignId}/earning-rules/{earningRuleId} | Delete Earning Rule
[**delete_loyalty_program**](LoyaltiesApi.md#delete_loyalty_program) | **DELETE** /v1/loyalties/{campaignId} | Delete Loyalty Campaign
[**delete_reward_assignment1**](LoyaltiesApi.md#delete_reward_assignment1) | **DELETE** /v1/loyalties/{campaignId}/rewards/{assignmentId} | Delete Reward Assignment
[**disable_earning_rule**](LoyaltiesApi.md#disable_earning_rule) | **POST** /v1/loyalties/{campaignId}/earning-rules/{earningRuleId}/disable | Disable Earning Rule
[**enable_earning_rule**](LoyaltiesApi.md#enable_earning_rule) | **POST** /v1/loyalties/{campaignId}/earning-rules/{earningRuleId}/enable | Enable Earning Rule
[**export_loyalty_card_transactions**](LoyaltiesApi.md#export_loyalty_card_transactions) | **POST** /v1/loyalties/members/{memberId}/transactions/export | Export Loyalty Card Transactions
[**export_loyalty_card_transactions1**](LoyaltiesApi.md#export_loyalty_card_transactions1) | **POST** /v1/loyalties/{campaignId}/members/{memberId}/transactions/export | Export Loyalty Card Transactions
[**get_earning_rule**](LoyaltiesApi.md#get_earning_rule) | **GET** /v1/loyalties/{campaignId}/earning-rules/{earningRuleId} | Get Earning Rule
[**get_loyalty_tier**](LoyaltiesApi.md#get_loyalty_tier) | **GET** /v1/loyalties/{campaignId}/tiers/{loyaltyTierId} | Get Loyalty Tier
[**get_reward_assignment1**](LoyaltiesApi.md#get_reward_assignment1) | **GET** /v1/loyalties/{campaignId}/reward-assignments/{assignmentId} | Get Reward Assignment
[**get_reward_assignment2**](LoyaltiesApi.md#get_reward_assignment2) | **GET** /v1/loyalties/{campaignId}/rewards/{assignmentId} | Get Reward Assignment
[**get_reward_details**](LoyaltiesApi.md#get_reward_details) | **GET** /v1/loyalties/{campaignId}/reward-assignments/{assignmentId}/reward | Get Reward Details
[**list_loyalty_card_transactions**](LoyaltiesApi.md#list_loyalty_card_transactions) | **GET** /v1/loyalties/members/{memberId}/transactions | List Loyalty Card Transactions
[**list_loyalty_card_transactions1**](LoyaltiesApi.md#list_loyalty_card_transactions1) | **GET** /v1/loyalties/{campaignId}/members/{memberId}/transactions | List Loyalty Card Transactions
[**list_loyalty_tier_earning_rules**](LoyaltiesApi.md#list_loyalty_tier_earning_rules) | **GET** /v1/loyalties/{campaignId}/tiers/{loyaltyTierId}/earning-rules | List Loyalty Tier Earning Rules
[**list_loyalty_tier_rewards**](LoyaltiesApi.md#list_loyalty_tier_rewards) | **GET** /v1/loyalties/{campaignId}/tiers/{loyaltyTierId}/rewards | List Loyalty Tier Rewards
[**list_loyalty_tiers**](LoyaltiesApi.md#list_loyalty_tiers) | **GET** /v1/loyalties/{campaignId}/tiers | List Loyalty Tiers
[**list_member_loyalty_tier**](LoyaltiesApi.md#list_member_loyalty_tier) | **GET** /v1/loyalties/members/{memberId}/tiers | List Member&#39;s Loyalty Tiers
[**list_member_rewards**](LoyaltiesApi.md#list_member_rewards) | **GET** /v1/loyalties/members/{memberId}/rewards | List Member Rewards
[**list_points_expiration**](LoyaltiesApi.md#list_points_expiration) | **GET** /v1/loyalties/{campaignId}/members/{memberId}/points-expiration | Get Points Expiration
[**redeem_reward**](LoyaltiesApi.md#redeem_reward) | **POST** /v1/loyalties/members/{memberId}/redemption | Redeem Reward
[**redeem_reward1**](LoyaltiesApi.md#redeem_reward1) | **POST** /v1/loyalties/{campaignId}/members/{memberId}/redemption | Redeem Reward
[**transfer_points**](LoyaltiesApi.md#transfer_points) | **POST** /v1/loyalties/{campaignId}/members/{memberId}/transfers | Transfer Loyalty Points
[**update_loyalty_card_balance**](LoyaltiesApi.md#update_loyalty_card_balance) | **POST** /v1/loyalties/members/{memberId}/balance | Add or Remove Loyalty Card Balance
[**update_loyalty_card_balance1**](LoyaltiesApi.md#update_loyalty_card_balance1) | **POST** /v1/loyalties/{campaignId}/members/{memberId}/balance | Add or Remove Loyalty Card Balance


# **create_in_bulk_loyalty_tiers**
> List[LoyaltyTier] create_in_bulk_loyalty_tiers(campaign_id, loyalties_tiers_create_in_bulk_request_body_item=loyalties_tiers_create_in_bulk_request_body_item)

Create loyalty tiers

Creates loyalty tiers for desired campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_tiers_create_in_bulk_request_body_item import LoyaltiesTiersCreateInBulkRequestBodyItem
from voucherify_client.models.loyalty_tier import LoyaltyTier
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique loyalty campaign ID or name.
    loyalties_tiers_create_in_bulk_request_body_item = [voucherify_client.LoyaltiesTiersCreateInBulkRequestBodyItem()] # List[LoyaltiesTiersCreateInBulkRequestBodyItem] | Provide tier definitions you want to add to existing loyalty campaign. (optional)

    try:
        # Create loyalty tiers
        api_response = api_instance.create_in_bulk_loyalty_tiers(campaign_id, loyalties_tiers_create_in_bulk_request_body_item=loyalties_tiers_create_in_bulk_request_body_item)
        print("The response of LoyaltiesApi->create_in_bulk_loyalty_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->create_in_bulk_loyalty_tiers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique loyalty campaign ID or name. | 
 **loyalties_tiers_create_in_bulk_request_body_item** | [**List[LoyaltiesTiersCreateInBulkRequestBodyItem]**](LoyaltiesTiersCreateInBulkRequestBodyItem.md)| Provide tier definitions you want to add to existing loyalty campaign. | [optional] 

### Return type

[**List[LoyaltyTier]**](LoyaltyTier.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns created loyalty tiers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_earning_rule**
> delete_earning_rule(campaign_id, earning_rule_id)

Delete Earning Rule

This method deletes an earning rule for a specific loyalty campaign.

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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the `name` of the campaign as the path parameter value, e.g., `Loyalty%20Campaign`. 
    earning_rule_id = 'earning_rule_id_example' # str | A unique earning rule ID.

    try:
        # Delete Earning Rule
        api_instance.delete_earning_rule(campaign_id, earning_rule_id)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->delete_earning_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the &#x60;name&#x60; of the campaign as the path parameter value, e.g., &#x60;Loyalty%20Campaign&#x60;.  | 
 **earning_rule_id** | **str**| A unique earning rule ID. | 

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

# **delete_loyalty_program**
> LoyaltiesDeleteResponseBody delete_loyalty_program(campaign_id, force=force)

Delete Loyalty Campaign

This method permanently deletes a loyalty campaign and all related loyalty cards. This action cannot be undone. Also, it immediately removes any redemptions on loyalty cards.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_delete_response_body import LoyaltiesDeleteResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the `name` of the campaign as the path parameter value, e.g., `Loyalty%20Campaign`. 
    force = True # bool | If this flag is set to `true`, the campaign and related vouchers will be removed permanently. Going forward, the user will be able to create the next campaign with the same name. (optional)

    try:
        # Delete Loyalty Campaign
        api_response = api_instance.delete_loyalty_program(campaign_id, force=force)
        print("The response of LoyaltiesApi->delete_loyalty_program:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->delete_loyalty_program: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the &#x60;name&#x60; of the campaign as the path parameter value, e.g., &#x60;Loyalty%20Campaign&#x60;.  | 
 **force** | **bool**| If this flag is set to &#x60;true&#x60;, the campaign and related vouchers will be removed permanently. Going forward, the user will be able to create the next campaign with the same name. | [optional] 

### Return type

[**LoyaltiesDeleteResponseBody**](LoyaltiesDeleteResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the id of the scheduled asynchronous action, informing you that your request has been accepted and the loyalty campaign will be deleted from the repository asynchronously. To check the deletion status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reward_assignment1**
> delete_reward_assignment1(campaign_id, assignment_id)

Delete Reward Assignment

This method deletes a reward assignment for a particular loyalty campaign.

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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the `name` of the campaign as the path parameter value, e.g., `Loyalty%20Campaign`. 
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID.

    try:
        # Delete Reward Assignment
        api_instance.delete_reward_assignment1(campaign_id, assignment_id)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->delete_reward_assignment1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the &#x60;name&#x60; of the campaign as the path parameter value, e.g., &#x60;Loyalty%20Campaign&#x60;.  | 
 **assignment_id** | **str**| A unique reward assignment ID. | 

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

# **disable_earning_rule**
> LoyaltiesEarningRulesDisableResponseBody disable_earning_rule(campaign_id, earning_rule_id)

Disable Earning Rule

Disable an earning rule.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_earning_rules_disable_response_body import LoyaltiesEarningRulesDisableResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name.
    earning_rule_id = 'earning_rule_id_example' # str | Unique earning rule ID.

    try:
        # Disable Earning Rule
        api_response = api_instance.disable_earning_rule(campaign_id, earning_rule_id)
        print("The response of LoyaltiesApi->disable_earning_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->disable_earning_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name. | 
 **earning_rule_id** | **str**| Unique earning rule ID. | 

### Return type

[**LoyaltiesEarningRulesDisableResponseBody**](LoyaltiesEarningRulesDisableResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an earning rule object with the &#x60;active&#x60; parameter set to &#x60;false&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_earning_rule**
> LoyaltiesEarningRulesEnableResponseBody enable_earning_rule(campaign_id, earning_rule_id)

Enable Earning Rule

Enable an earning rule.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_earning_rules_enable_response_body import LoyaltiesEarningRulesEnableResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name.
    earning_rule_id = 'earning_rule_id_example' # str | Unique earning rule ID.

    try:
        # Enable Earning Rule
        api_response = api_instance.enable_earning_rule(campaign_id, earning_rule_id)
        print("The response of LoyaltiesApi->enable_earning_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->enable_earning_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name. | 
 **earning_rule_id** | **str**| Unique earning rule ID. | 

### Return type

[**LoyaltiesEarningRulesEnableResponseBody**](LoyaltiesEarningRulesEnableResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an earning rule object with the &#x60;active&#x60; parameter set to &#x60;true&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_card_transactions**
> LoyaltiesMembersTransactionsExportCreateResponseBody export_loyalty_card_transactions(member_id, loyalties_members_transactions_export_create_request_body=loyalties_members_transactions_export_create_request_body)

Export Loyalty Card Transactions

Export transactions that are associated with point movements on a loyalty card.  | **Field** | **Definition** | **Example Export** | |:---|:---|:---| | id | Unique transaction ID assigned by Voucherify. | vtx_0cb7811f1c07765800 | | type | Transaction type. | - `POINTS_EXPIRATION` <br> - `POINTS_ADDITION` <br> - `POINTS_REMOVAL` <br> - `POINTS_TRANSFER_OUT` <br> - `POINTS_ACCRUAL` <br> - `POINTS_REFUND` <br> - `POINTS_REDEMPTION` | | source_id | Custom source ID of the transaction if one was included originally. | source_id_custom | | reason | Contains the reason for the transaction if one was included originally. |  | | balance | The loyalty card balance after the transaction. |  | | amount | The amount of loyalty points being allocated during the transaction. This value can either be negative or positive depending on the nature of the transaction. |  | | created_at | Timestamp in ISO 8601 format representing the date and time when the transaction was created. | 2022-03-09T09:16:32.521Z  | | voucher_id | Unique Voucher ID. | v_dky7ksKfPX50Wb2Bxvcoeb1xT20b6tcp | | campaign_id | Parent campaign ID. | camp_FNYR4jhqZBM9xTptxDGgeNBV | | source|  Channel through which the transaction was initiated. | - `API` <br> - `voucherify-web-ui` <br> - `Automation` | | details | More detailed information stored in the form of a JSON. | Provides more details related to the transaction in the form of an object. | | related_transaction_id | Unique transaction ID related to a receiver/donor card in the case of a points transfer from/to another card. | vtx_0c9afe802593b34b80 |

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_transactions_export_create_request_body import LoyaltiesMembersTransactionsExportCreateRequestBody
from voucherify_client.models.loyalties_members_transactions_export_create_response_body import LoyaltiesMembersTransactionsExportCreateResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | A unique code identifying the loyalty card that you are looking to export transaction data for.
    loyalties_members_transactions_export_create_request_body = {"parameters":{"order":"-created_at","fields":["id","type","source_id","reason","balance","amount","created_at","voucher_id","campaign_id","details","related_transaction_id"]}} # LoyaltiesMembersTransactionsExportCreateRequestBody | Specify the parameters and filters for the transaction export. (optional)

    try:
        # Export Loyalty Card Transactions
        api_response = api_instance.export_loyalty_card_transactions(member_id, loyalties_members_transactions_export_create_request_body=loyalties_members_transactions_export_create_request_body)
        print("The response of LoyaltiesApi->export_loyalty_card_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->export_loyalty_card_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| A unique code identifying the loyalty card that you are looking to export transaction data for. | 
 **loyalties_members_transactions_export_create_request_body** | [**LoyaltiesMembersTransactionsExportCreateRequestBody**](LoyaltiesMembersTransactionsExportCreateRequestBody.md)| Specify the parameters and filters for the transaction export. | [optional] 

### Return type

[**LoyaltiesMembersTransactionsExportCreateResponseBody**](LoyaltiesMembersTransactionsExportCreateResponseBody.md)

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

# **export_loyalty_card_transactions1**
> LoyaltiesMembersTransactionsExportCreateResponseBody export_loyalty_card_transactions1(campaign_id, member_id, loyalties_members_transactions_export_create_request_body=loyalties_members_transactions_export_create_request_body)

Export Loyalty Card Transactions

Export transactions that are associated with point movements on a loyalty card.  | **Field** | **Definition** | **Example Export** | |:---|:---|:---| | id | Unique transaction ID assigned by Voucherify. | vtx_0cb7811f1c07765800 | | type | Transaction type. | - `POINTS_EXPIRATION` <br> - `POINTS_ADDITION` <br> - `POINTS_REMOVAL` <br> - `POINTS_TRANSFER_OUT` <br> - `POINTS_ACCRUAL` <br> - `POINTS_REFUND` <br> - `POINTS_REDEMPTION` | | source_id | Custom source ID of the transaction if one was included originally. | source_id_custom | | reason | Contains the reason for the transaction if one was included originally. |  | | balance | The loyalty card balance after the transaction. |  | | amount | The amount of loyalty points being allocated during the transaction. This value can either be negative or positive depending on the nature of the transaction. |  | | created_at | Timestamp in ISO 8601 format representing the date and time when the transaction was created. | 2022-03-09T09:16:32.521Z  | | voucher_id | Unique Voucher ID. | v_dky7ksKfPX50Wb2Bxvcoeb1xT20b6tcp | | campaign_id | Parent campaign ID. | camp_FNYR4jhqZBM9xTptxDGgeNBV | | source|  Channel through which the transaction was initiated. | - `API` <br> - `voucherify-web-ui` <br> - `Automation` | | details | More detailed information stored in the form of a JSON. | Provides more details related to the transaction in the form of an object. | | related_transaction_id | Unique transaction ID related to a receiver/donor card in the case of a points transfer from/to another card. | vtx_0c9afe802593b34b80 |

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_transactions_export_create_request_body import LoyaltiesMembersTransactionsExportCreateRequestBody
from voucherify_client.models.loyalties_members_transactions_export_create_response_body import LoyaltiesMembersTransactionsExportCreateResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | A unique identifier of the loyalty campaign containing the voucher whose transactions you would like to export.
    member_id = 'member_id_example' # str | A unique code identifying the loyalty card that you are looking to export transaction data for.
    loyalties_members_transactions_export_create_request_body = {"parameters":{"order":"-created_at","fields":["id","type","source_id","reason","balance","amount","created_at","voucher_id","campaign_id","details","related_transaction_id"]}} # LoyaltiesMembersTransactionsExportCreateRequestBody | Specify the parameters and filters for the transaction export. (optional)

    try:
        # Export Loyalty Card Transactions
        api_response = api_instance.export_loyalty_card_transactions1(campaign_id, member_id, loyalties_members_transactions_export_create_request_body=loyalties_members_transactions_export_create_request_body)
        print("The response of LoyaltiesApi->export_loyalty_card_transactions1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->export_loyalty_card_transactions1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| A unique identifier of the loyalty campaign containing the voucher whose transactions you would like to export. | 
 **member_id** | **str**| A unique code identifying the loyalty card that you are looking to export transaction data for. | 
 **loyalties_members_transactions_export_create_request_body** | [**LoyaltiesMembersTransactionsExportCreateRequestBody**](LoyaltiesMembersTransactionsExportCreateRequestBody.md)| Specify the parameters and filters for the transaction export. | [optional] 

### Return type

[**LoyaltiesMembersTransactionsExportCreateResponseBody**](LoyaltiesMembersTransactionsExportCreateResponseBody.md)

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

# **get_earning_rule**
> LoyaltiesEarningRulesGetResponseBody get_earning_rule(campaign_id, earning_rule_id)

Get Earning Rule

Retrieves an earning rule assigned to a campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_earning_rules_get_response_body import LoyaltiesEarningRulesGetResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the `name` of the campaign as the path parameter value, e.g., `Loyalty%20Campaign`. 
    earning_rule_id = 'earning_rule_id_example' # str | A unique earning rule ID.

    try:
        # Get Earning Rule
        api_response = api_instance.get_earning_rule(campaign_id, earning_rule_id)
        print("The response of LoyaltiesApi->get_earning_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_earning_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the &#x60;name&#x60; of the campaign as the path parameter value, e.g., &#x60;Loyalty%20Campaign&#x60;.  | 
 **earning_rule_id** | **str**| A unique earning rule ID. | 

### Return type

[**LoyaltiesEarningRulesGetResponseBody**](LoyaltiesEarningRulesGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an earning rule object with the earning rule details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_tier**
> LoyaltiesTiersGetResponseBody get_loyalty_tier(campaign_id, loyalty_tier_id)

Get Loyalty Tier

Retrieve a loyalty tier from a loyalty campaign by the loyalty tier ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_tiers_get_response_body import LoyaltiesTiersGetResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique loyalty campaign ID or name.
    loyalty_tier_id = 'loyalty_tier_id_example' # str | Unique loyalty tier ID.

    try:
        # Get Loyalty Tier
        api_response = api_instance.get_loyalty_tier(campaign_id, loyalty_tier_id)
        print("The response of LoyaltiesApi->get_loyalty_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_loyalty_tier: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique loyalty campaign ID or name. | 
 **loyalty_tier_id** | **str**| Unique loyalty tier ID. | 

### Return type

[**LoyaltiesTiersGetResponseBody**](LoyaltiesTiersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a loyalty tier object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward_assignment1**
> LoyaltiesRewardAssignmentsGetResponseBody get_reward_assignment1(campaign_id, assignment_id)

Get Reward Assignment

Retrieve specific reward assignment.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_reward_assignments_get_response_body import LoyaltiesRewardAssignmentsGetResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the `name` of the campaign as the path parameter value, e.g., `Loyalty%20Campaign`. 
    assignment_id = 'assignment_id_example' # str | Unique reward assignment ID.

    try:
        # Get Reward Assignment
        api_response = api_instance.get_reward_assignment1(campaign_id, assignment_id)
        print("The response of LoyaltiesApi->get_reward_assignment1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_reward_assignment1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the &#x60;name&#x60; of the campaign as the path parameter value, e.g., &#x60;Loyalty%20Campaign&#x60;.  | 
 **assignment_id** | **str**| Unique reward assignment ID. | 

### Return type

[**LoyaltiesRewardAssignmentsGetResponseBody**](LoyaltiesRewardAssignmentsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns specific reward assignment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward_assignment2**
> LoyaltiesRewardsGetResponseBody get_reward_assignment2(campaign_id, assignment_id)

Get Reward Assignment

Retrieve specific reward assignment.  > 📘 Alternative endpoint > > This endpoint is an alternative to this [endpoint](ref:get-reward-assignment-2). 

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_rewards_get_response_body import LoyaltiesRewardsGetResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the `name` of the campaign as the path parameter value, e.g., `Loyalty%20Campaign`. 
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID.

    try:
        # Get Reward Assignment
        api_response = api_instance.get_reward_assignment2(campaign_id, assignment_id)
        print("The response of LoyaltiesApi->get_reward_assignment2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_reward_assignment2: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the &#x60;name&#x60; of the campaign as the path parameter value, e.g., &#x60;Loyalty%20Campaign&#x60;.  | 
 **assignment_id** | **str**| A unique reward assignment ID. | 

### Return type

[**LoyaltiesRewardsGetResponseBody**](LoyaltiesRewardsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns specific reward assignment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward_details**
> LoyaltiesRewardAssignmentsRewardGetResponseBody get_reward_details(campaign_id, assignment_id)

Get Reward Details

Get reward details in the context of a loyalty campaign and reward assignment ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_reward_assignments_reward_get_response_body import LoyaltiesRewardAssignmentsRewardGetResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the `name` of the campaign as the path parameter value, e.g., `Loyalty%20Campaign`. 
    assignment_id = 'assignment_id_example' # str | Unique reward assignment ID.

    try:
        # Get Reward Details
        api_response = api_instance.get_reward_details(campaign_id, assignment_id)
        print("The response of LoyaltiesApi->get_reward_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_reward_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the &#x60;name&#x60; of the campaign as the path parameter value, e.g., &#x60;Loyalty%20Campaign&#x60;.  | 
 **assignment_id** | **str**| Unique reward assignment ID. | 

### Return type

[**LoyaltiesRewardAssignmentsRewardGetResponseBody**](LoyaltiesRewardAssignmentsRewardGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns reward details in the context of a loyalty *campaign* and reward assignment ID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_card_transactions**
> LoyaltiesMembersTransactionsListResponseBody list_loyalty_card_transactions(member_id, limit=limit, page=page)

List Loyalty Card Transactions

Retrieve transaction data related to point movements for a specific loyalty card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_transactions_list_response_body import LoyaltiesMembersTransactionsListResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | A unique code identifying the loyalty card that you are looking to retrieve transaction data for.
    limit = 56 # int | A limit on the number of objects to be returned. Limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. (optional)

    try:
        # List Loyalty Card Transactions
        api_response = api_instance.list_loyalty_card_transactions(member_id, limit=limit, page=page)
        print("The response of LoyaltiesApi->list_loyalty_card_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_card_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| A unique code identifying the loyalty card that you are looking to retrieve transaction data for. | 
 **limit** | **int**| A limit on the number of objects to be returned. Limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. | [optional] 

### Return type

[**LoyaltiesMembersTransactionsListResponseBody**](LoyaltiesMembersTransactionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a dictionary of loyalty card transaction objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_card_transactions1**
> LoyaltiesMembersTransactionsListResponseBody list_loyalty_card_transactions1(campaign_id, member_id, limit=limit, page=page)

List Loyalty Card Transactions

Retrieve transaction data related to point movements for a specific loyalty card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_transactions_list_response_body import LoyaltiesMembersTransactionsListResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | A unique identifier of the loyalty campaign containing the voucher whose transactions you would like to return.
    member_id = 'member_id_example' # str | A unique code identifying the loyalty card that you are looking to retrieve transaction data for.
    limit = 56 # int | A limit on the number of objects to be returned. Limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. (optional)

    try:
        # List Loyalty Card Transactions
        api_response = api_instance.list_loyalty_card_transactions1(campaign_id, member_id, limit=limit, page=page)
        print("The response of LoyaltiesApi->list_loyalty_card_transactions1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_card_transactions1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| A unique identifier of the loyalty campaign containing the voucher whose transactions you would like to return. | 
 **member_id** | **str**| A unique code identifying the loyalty card that you are looking to retrieve transaction data for. | 
 **limit** | **int**| A limit on the number of objects to be returned. Limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. | [optional] 

### Return type

[**LoyaltiesMembersTransactionsListResponseBody**](LoyaltiesMembersTransactionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a dictionary of loyalty card transaction objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_tier_earning_rules**
> LoyaltiesTiersEarningRulesListResponseBody list_loyalty_tier_earning_rules(campaign_id, loyalty_tier_id, limit=limit, page=page)

List Loyalty Tier Earning Rules

Retrieve available earning rules for a given tier and the calculation method for earning points.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_tiers_earning_rules_list_response_body import LoyaltiesTiersEarningRulesListResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name.
    loyalty_tier_id = 'loyalty_tier_id_example' # str | Unique loyalty tier ID.
    limit = 56 # int | A limit on the number of objects to be returned. Limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. (optional)

    try:
        # List Loyalty Tier Earning Rules
        api_response = api_instance.list_loyalty_tier_earning_rules(campaign_id, loyalty_tier_id, limit=limit, page=page)
        print("The response of LoyaltiesApi->list_loyalty_tier_earning_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_tier_earning_rules: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name. | 
 **loyalty_tier_id** | **str**| Unique loyalty tier ID. | 
 **limit** | **int**| A limit on the number of objects to be returned. Limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. | [optional] 

### Return type

[**LoyaltiesTiersEarningRulesListResponseBody**](LoyaltiesTiersEarningRulesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of earning rules for a given tier. The object for each earning rule also contains information about how the points are calculated; this includes mapping. If a specific multiplier was used to calculate points for a given tier, then the &#x60;loyalty.points&#x60; parameter will account for this calculation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_tier_rewards**
> LoyaltiesTiersRewardsListResponseBody list_loyalty_tier_rewards(campaign_id, loyalty_tier_id)

List Loyalty Tier Rewards

Get available rewards for a given tier.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_tiers_rewards_list_response_body import LoyaltiesTiersRewardsListResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name.
    loyalty_tier_id = 'loyalty_tier_id_example' # str | Unique loyalty tier ID.

    try:
        # List Loyalty Tier Rewards
        api_response = api_instance.list_loyalty_tier_rewards(campaign_id, loyalty_tier_id)
        print("The response of LoyaltiesApi->list_loyalty_tier_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_tier_rewards: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name. | 
 **loyalty_tier_id** | **str**| Unique loyalty tier ID. | 

### Return type

[**LoyaltiesTiersRewardsListResponseBody**](LoyaltiesTiersRewardsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a dictionary of loyalty tier reward objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_tiers**
> LoyaltiesTiersListResponseBody list_loyalty_tiers(campaign_id, limit=limit, order=order)

List Loyalty Tiers

Retrieve a list of loyalty tiers which were added to the loyalty program.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_tiers_list_response_body import LoyaltiesTiersListResponseBody
from voucherify_client.models.parameter_order_list_loyalty_tiers import ParameterOrderListLoyaltyTiers
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique loyalty campaign ID or name.
    limit = 56 # int | A limit on the number of objects to be returned. Limit can range between 1 and 100 items. (optional)
    order = voucherify_client.ParameterOrderListLoyaltyTiers() # ParameterOrderListLoyaltyTiers | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Loyalty Tiers
        api_response = api_instance.list_loyalty_tiers(campaign_id, limit=limit, order=order)
        print("The response of LoyaltiesApi->list_loyalty_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_tiers: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique loyalty campaign ID or name. | 
 **limit** | **int**| A limit on the number of objects to be returned. Limit can range between 1 and 100 items. | [optional] 
 **order** | [**ParameterOrderListLoyaltyTiers**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**LoyaltiesTiersListResponseBody**](LoyaltiesTiersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of loyalty tier objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_loyalty_tier**
> LoyaltiesMembersTiersListResponseBody list_member_loyalty_tier(member_id)

List Member's Loyalty Tiers

Retrieve member tiers using the loyalty card ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_tiers_list_response_body import LoyaltiesMembersTiersListResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | Unique loyalty card assigned to a particular customer.

    try:
        # List Member's Loyalty Tiers
        api_response = api_instance.list_member_loyalty_tier(member_id)
        print("The response of LoyaltiesApi->list_member_loyalty_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_member_loyalty_tier: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique loyalty card assigned to a particular customer. | 

### Return type

[**LoyaltiesMembersTiersListResponseBody**](LoyaltiesMembersTiersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a data array containing the member&#39;s loyalty tiers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_rewards**
> LoyaltiesMembersRewardsListResponseBody list_member_rewards(member_id, affordable_only=affordable_only)

List Member Rewards

Retrieves the list of rewards that the given customer (identified by `member_id`, which is a loyalty card assigned to a particular customer) **can get in exchange for loyalty points**.    You can use the `affordable_only` parameter to limit the results to rewards that the customer can actually afford (only rewards whose price in points is not higher than the loyalty points balance on a loyalty card).    Please note that rewards that are disabled (i.e. set to `Not Available` in the Dashboard) for a given loyalty tier reward mapping will not be returned in this endpoint.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_rewards_list_response_body import LoyaltiesMembersRewardsListResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | Unique loyalty card assigned to a particular customer.
    affordable_only = True # bool | Limit the results to rewards that the customer can actually afford (only rewards whose price in points is not higher than the loyalty points balance on a loyalty card). Set this flag to `true` to return rewards which the customer can actually afford. (optional)

    try:
        # List Member Rewards
        api_response = api_instance.list_member_rewards(member_id, affordable_only=affordable_only)
        print("The response of LoyaltiesApi->list_member_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_member_rewards: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique loyalty card assigned to a particular customer. | 
 **affordable_only** | **bool**| Limit the results to rewards that the customer can actually afford (only rewards whose price in points is not higher than the loyalty points balance on a loyalty card). Set this flag to &#x60;true&#x60; to return rewards which the customer can actually afford. | [optional] 

### Return type

[**LoyaltiesMembersRewardsListResponseBody**](LoyaltiesMembersRewardsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of rewards for the given &#x60;member_id&#x60;. Returns a filtered list if the query parameter &#x60;affordable_only&#x60; is set to &#x60;true&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_points_expiration**
> LoyaltiesMembersPointsExpirationListResponseBody list_points_expiration(campaign_id, member_id, limit=limit, page=page)

Get Points Expiration

Retrieve loyalty point expiration buckets for a given loyalty card. Expired point buckets are not returned in this endpoint. You can use the [Exports API](ref:create-export) to retrieve a list of both `ACTIVE` and `EXPIRED` point buckets.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_points_expiration_list_response_body import LoyaltiesMembersPointsExpirationListResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the `name` of the campaign as the path parameter value, e.g., `Loyalty%20Campaign`. 
    member_id = 'member_id_example' # str | Loyalty card code.
    limit = 56 # int | A limit on the number of objects to be returned. Limit can range between 1 and 100 items. (optional)
    page = 56 # int | Which page of results to return. (optional)

    try:
        # Get Points Expiration
        api_response = api_instance.list_points_expiration(campaign_id, member_id, limit=limit, page=page)
        print("The response of LoyaltiesApi->list_points_expiration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_points_expiration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the &#x60;name&#x60; of the campaign as the path parameter value, e.g., &#x60;Loyalty%20Campaign&#x60;.  | 
 **member_id** | **str**| Loyalty card code. | 
 **limit** | **int**| A limit on the number of objects to be returned. Limit can range between 1 and 100 items. | [optional] 
 **page** | **int**| Which page of results to return. | [optional] 

### Return type

[**LoyaltiesMembersPointsExpirationListResponseBody**](LoyaltiesMembersPointsExpirationListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of loyalty points expiration buckets along with an expiration date if the points are due to expire. No expiration date parameter is returned if the loyalty points bucket does not expire. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_reward**
> LoyaltiesMembersRedemptionRedeemResponseBody redeem_reward(member_id, loyalties_members_redemption_redeem_request_body=loyalties_members_redemption_redeem_request_body)

Redeem Reward

<!-- theme: info --> > 📘 Alternative endpoint > > This endpoint is an alternative to this <!-- [endpoint](OpenAPI.json/paths/~1loyalties~1{campaignId}~1members~1{memberId}~1redemption) -->[endpoint](ref:redeem-reward-1). The URL was re-designed to allow you to redeem a reward without having to provide the `campaignId` as a path parameter.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_redemption_redeem_request_body import LoyaltiesMembersRedemptionRedeemRequestBody
from voucherify_client.models.loyalties_members_redemption_redeem_response_body import LoyaltiesMembersRedemptionRedeemResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | Unique loyalty card assigned to a particular customer.
    loyalties_members_redemption_redeem_request_body = {"reward":{"id":"rew_INt3fGH3n7xIr3ZQcq4kkUZ1","points":100},"order":{"items":[{"product_id":"prod_0c5d6689b39320059b","quantity":"1"},{"product_id":"prod_0b2c36568000039138","quantity":"2"}]}} # LoyaltiesMembersRedemptionRedeemRequestBody | Specify the reward to be redeemed. In case of a pay with points reward, specify the order and the number of points to be applied to the order. Please note that if you do not specify the amount of points, the application will default to applying the number of points to pay for the remainder of the order. If the limit of available points on the card is reached, then only the available points on the card will be applied to the order. (optional)

    try:
        # Redeem Reward
        api_response = api_instance.redeem_reward(member_id, loyalties_members_redemption_redeem_request_body=loyalties_members_redemption_redeem_request_body)
        print("The response of LoyaltiesApi->redeem_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->redeem_reward: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique loyalty card assigned to a particular customer. | 
 **loyalties_members_redemption_redeem_request_body** | [**LoyaltiesMembersRedemptionRedeemRequestBody**](LoyaltiesMembersRedemptionRedeemRequestBody.md)| Specify the reward to be redeemed. In case of a pay with points reward, specify the order and the number of points to be applied to the order. Please note that if you do not specify the amount of points, the application will default to applying the number of points to pay for the remainder of the order. If the limit of available points on the card is reached, then only the available points on the card will be applied to the order. | [optional] 

### Return type

[**LoyaltiesMembersRedemptionRedeemResponseBody**](LoyaltiesMembersRedemptionRedeemResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a redemption object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_reward1**
> LoyaltiesMembersRedemptionRedeemResponseBody redeem_reward1(campaign_id, member_id, loyalties_members_redemption_redeem_request_body=loyalties_members_redemption_redeem_request_body)

Redeem Reward

Exchange points from a loyalty card for a specified reward. This API method returns an assigned award in the response. It means that if a requesting customer gets a coupon code with a discount for the next order, that discount code will be visible in response as part of the reward object definition.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_redemption_redeem_request_body import LoyaltiesMembersRedemptionRedeemRequestBody
from voucherify_client.models.loyalties_members_redemption_redeem_response_body import LoyaltiesMembersRedemptionRedeemResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID.
    member_id = 'member_id_example' # str | A code that identifies the loyalty card.
    loyalties_members_redemption_redeem_request_body = {"reward":{"id":"rew_INt3fGH3n7xIr3ZQcq4kkUZ1","points":100},"order":{"items":[{"product_id":"prod_0c5d6689b39320059b","quantity":"1"},{"product_id":"prod_0b2c36568000039138","quantity":"2"}]}} # LoyaltiesMembersRedemptionRedeemRequestBody | Specify the reward to be redeemed. In case of a pay with points reward, specify the order and the number of points to be applied to the order. Please note that if you do not specify the amount of points, the application will default to applying the number of points to pay for the remainder of the order. If the limit of available points on the card is reached, then only the available points on the card will be applied to the order. (optional)

    try:
        # Redeem Reward
        api_response = api_instance.redeem_reward1(campaign_id, member_id, loyalties_members_redemption_redeem_request_body=loyalties_members_redemption_redeem_request_body)
        print("The response of LoyaltiesApi->redeem_reward1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->redeem_reward1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID. | 
 **member_id** | **str**| A code that identifies the loyalty card. | 
 **loyalties_members_redemption_redeem_request_body** | [**LoyaltiesMembersRedemptionRedeemRequestBody**](LoyaltiesMembersRedemptionRedeemRequestBody.md)| Specify the reward to be redeemed. In case of a pay with points reward, specify the order and the number of points to be applied to the order. Please note that if you do not specify the amount of points, the application will default to applying the number of points to pay for the remainder of the order. If the limit of available points on the card is reached, then only the available points on the card will be applied to the order. | [optional] 

### Return type

[**LoyaltiesMembersRedemptionRedeemResponseBody**](LoyaltiesMembersRedemptionRedeemResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a redemption object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_points**
> LoyaltiesMembersTransfersCreateResponseBody transfer_points(campaign_id, member_id, loyalties_transfer_points=loyalties_transfer_points)

Transfer Loyalty Points

Transfer points between different loyalty cards. You need to provide the campaign ID and the loyalty card ID you want the points to be transferred to as path parameters in the URL. In the request body, you provide the loyalty cards you want the points to be transferred from and the number of points to transfer from each card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_transfers_create_response_body import LoyaltiesMembersTransfersCreateResponseBody
from voucherify_client.models.loyalties_transfer_points import LoyaltiesTransferPoints
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | A unique identifier of the loyalty campaign containing the voucher to which the loyalty points will be sent (destination).
    member_id = 'member_id_example' # str | A unique code identifying the loyalty card to which the user wants to transfer loyalty points (destination).
    loyalties_transfer_points = [{"code":"0PmQ7JQI","points":1},{"code":"kCeufB8i","points":1}] # List[LoyaltiesTransferPoints] | Provide the loyalty cards you want the points to be transferred from and the number of points to transfer from each card. (optional)

    try:
        # Transfer Loyalty Points
        api_response = api_instance.transfer_points(campaign_id, member_id, loyalties_transfer_points=loyalties_transfer_points)
        print("The response of LoyaltiesApi->transfer_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->transfer_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| A unique identifier of the loyalty campaign containing the voucher to which the loyalty points will be sent (destination). | 
 **member_id** | **str**| A unique code identifying the loyalty card to which the user wants to transfer loyalty points (destination). | 
 **loyalties_transfer_points** | [**List[LoyaltiesTransferPoints]**](LoyaltiesTransferPoints.md)| Provide the loyalty cards you want the points to be transferred from and the number of points to transfer from each card. | [optional] 

### Return type

[**LoyaltiesMembersTransfersCreateResponseBody**](LoyaltiesMembersTransfersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a loyalty card object for the loaded loyalty card, ie. the one that that points were transferred to from the other cards(s). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loyalty_card_balance**
> LoyaltiesMembersBalanceUpdateResponseBody update_loyalty_card_balance(member_id, loyalties_members_balance_update_request_body=loyalties_members_balance_update_request_body)

Add or Remove Loyalty Card Balance

This method gives adds or removes balance to an existing loyalty card. The removal of points will consume the points that expire the soonest.   <!-- theme: info --> > 📘 Alternative endpoint > This endpoint is an alternative to this <!-- [endpoint](OpenAPI.json/paths/~1loyalties~1{campaignId}~1members~1{memberId}~1balance) -->[endpoint](ref:update-loyalty-card-balance-1). The URL was re-designed to allow you to add or remove loyalty card balance without having to provide the `campaignId` as a path parameter.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_balance_update_request_body import LoyaltiesMembersBalanceUpdateRequestBody
from voucherify_client.models.loyalties_members_balance_update_response_body import LoyaltiesMembersBalanceUpdateResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | Unique loyalty card assigned to a particular customer.
    loyalties_members_balance_update_request_body = {"points":-100} # LoyaltiesMembersBalanceUpdateRequestBody | Specify the point adjustment along with the expiration mechanism. (optional)

    try:
        # Add or Remove Loyalty Card Balance
        api_response = api_instance.update_loyalty_card_balance(member_id, loyalties_members_balance_update_request_body=loyalties_members_balance_update_request_body)
        print("The response of LoyaltiesApi->update_loyalty_card_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->update_loyalty_card_balance: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique loyalty card assigned to a particular customer. | 
 **loyalties_members_balance_update_request_body** | [**LoyaltiesMembersBalanceUpdateRequestBody**](LoyaltiesMembersBalanceUpdateRequestBody.md)| Specify the point adjustment along with the expiration mechanism. | [optional] 

### Return type

[**LoyaltiesMembersBalanceUpdateResponseBody**](LoyaltiesMembersBalanceUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a balance object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loyalty_card_balance1**
> LoyaltiesMembersBalanceUpdateResponseBody update_loyalty_card_balance1(campaign_id, member_id, loyalties_members_balance_update_request_body=loyalties_members_balance_update_request_body)

Add or Remove Loyalty Card Balance

This method adds or removes balance to an existing loyalty card. The removal of points will consume the points that expire the soonest.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):
```python
import time
import os
import voucherify_client
from voucherify_client.models.loyalties_members_balance_update_request_body import LoyaltiesMembersBalanceUpdateRequestBody
from voucherify_client.models.loyalties_members_balance_update_response_body import LoyaltiesMembersBalanceUpdateResponseBody
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
    api_instance = voucherify_client.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID.
    member_id = 'member_id_example' # str | A code that identifies the loyalty card.
    loyalties_members_balance_update_request_body = {"points":100,"expiration_type":"CUSTOM_DATE","expiration_date":"2023-05-30"} # LoyaltiesMembersBalanceUpdateRequestBody | Specify the point adjustment along with the expiration mechanism. (optional)

    try:
        # Add or Remove Loyalty Card Balance
        api_response = api_instance.update_loyalty_card_balance1(campaign_id, member_id, loyalties_members_balance_update_request_body=loyalties_members_balance_update_request_body)
        print("The response of LoyaltiesApi->update_loyalty_card_balance1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->update_loyalty_card_balance1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID. | 
 **member_id** | **str**| A code that identifies the loyalty card. | 
 **loyalties_members_balance_update_request_body** | [**LoyaltiesMembersBalanceUpdateRequestBody**](LoyaltiesMembersBalanceUpdateRequestBody.md)| Specify the point adjustment along with the expiration mechanism. | [optional] 

### Return type

[**LoyaltiesMembersBalanceUpdateResponseBody**](LoyaltiesMembersBalanceUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a balance object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

