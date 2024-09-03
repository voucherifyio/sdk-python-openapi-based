# LoyaltiesMembersCreateResponseBody

Respone body schema for assigning a loyalty card to a customer using **POST** `/loyalties/{campaignId}/members`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Assigned by the Voucherify API, identifies the voucher. | [optional] 
**code** | **str** | A code that identifies a voucher. Pattern can use all letters of the English alphabet, Arabic numerals, and special characters. | [optional] 
**campaign** | **str** | A unique campaign name, identifies the voucher&#39;s parent campaign. | [optional] 
**campaign_id** | **str** | Assigned by the Voucherify API, identifies the voucher&#39;s parent campaign. | [optional] 
**category** | **str** | Tag defining the category that this voucher belongs to. | [optional] 
**category_id** | **str** | Unique category ID assigned by Voucherify. | [optional] 
**type** | **str** | Defines the type of the voucher.  | [optional] [default to 'LOYALTY_CARD']
**discount** | **object** |  | [optional] 
**gift** | **object** |  | [optional] 
**loyalty_card** | [**LoyaltiesMembersCreateResponseBodyLoyaltyCard**](LoyaltiesMembersCreateResponseBodyLoyaltyCard.md) |  | [optional] 
**start_date** | **datetime** | Activation timestamp defines when the code starts to be active in ISO 8601 format. Voucher is *inactive before* this date.  | [optional] 
**expiration_date** | **datetime** | Expiration timestamp defines when the code expires in ISO 8601 format.  Voucher is *inactive after* this date. | [optional] 
**validity_timeframe** | [**ValidityTimeframe**](ValidityTimeframe.md) |  | [optional] 
**validity_day_of_week** | **List[int]** | Integer array corresponding to the particular days of the week in which the voucher is valid.  - &#x60;0&#x60; Sunday - &#x60;1&#x60; Monday - &#x60;2&#x60; Tuesday - &#x60;3&#x60; Wednesday - &#x60;4&#x60; Thursday - &#x60;5&#x60; Friday - &#x60;6&#x60; Saturday | [optional] 
**validity_hours** | [**ValidityHours**](ValidityHours.md) |  | [optional] 
**active** | **bool** | A flag to toggle the voucher on or off. You can disable a voucher even though it&#39;s within the active period defined by the &#x60;start_date&#x60; and &#x60;expiration_date&#x60;.    - &#x60;true&#x60; indicates an *active* voucher - &#x60;false&#x60; indicates an *inactive* voucher | [optional] 
**additional_info** | **str** | An optional field to keep any extra textual information about the code such as a code description and details. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the code. A set of key/value pairs that you can attach to a voucher object. It can be useful for storing additional information about the voucher in a structured format. | [optional] 
**assets** | [**VoucherAssets**](VoucherAssets.md) |  | [optional] 
**is_referral_code** | **bool** | This is always false for loyalty members. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the voucher was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the voucher was last updated in ISO 8601 format. | [optional] 
**holder_id** | **str** | Unique identifier of the customer who owns the voucher. | [optional] 
**object** | **str** | The type of the object represented by JSON. Default is &#x60;voucher&#x60;. | [optional] [default to 'voucher']
**publish** | [**LoyaltiesMembersCreateResponseBodyPublish**](LoyaltiesMembersCreateResponseBodyPublish.md) |  | [optional] 
**redemption** | [**LoyaltiesMembersCreateResponseBodyRedemption**](LoyaltiesMembersCreateResponseBodyRedemption.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

