# VouchersRedemptionGetResponseBody

Response body schema for **GET** `/vouchers/{code}/redemption`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The maximum number of times a voucher can be redeemed. | [optional] 
**redeemed_quantity** | **int** | The number of times the voucher was redeemed successfully. | 
**object** | **str** | The type of object represented by JSON. This object stores information about redemptions in a dictionary. | [default to 'list']
**url** | **str** | URL | 
**data_ref** | **str** | Identifies the name of the attribute that contains the array of &#x60;redemption_entries&#x60;. | [default to 'redemption_entries']
**total** | **int** | Total number of redemption objects. | 
**redemption_entries** | [**List[VouchersRedemptionGetResponseBodyRedemptionEntriesItem]**](VouchersRedemptionGetResponseBodyRedemptionEntriesItem.md) | Contains the array of successful and failed redemption objects. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


