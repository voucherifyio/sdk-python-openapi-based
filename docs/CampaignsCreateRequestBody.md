# CampaignsCreateRequestBody

Request body schema for **POST** `/campaigns`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Campaign name. | [optional] 
**description** | **str** | An optional field to keep any extra textual information about the campaign such as a campaign description and details. | [optional] 
**type** | **str** | Defines whether the campaign can be updated with new vouchers after campaign creation.      - &#x60;AUTO_UPDATE&#x60;: By choosing the auto update option you will create a campaign that can be enhanced by new vouchers after the time of creation (e.g. by publish vouchers method).     -  &#x60;STATIC&#x60;: vouchers need to be manually published. | [optional] 
**join_once** | **bool** | If this value is set to &#x60;true&#x60;, customers will be able to join the campaign only once. | [optional] 
**auto_join** | **bool** | Indicates whether customers will be able to auto-join a loyalty campaign if any earning rule is fulfilled. | [optional] 
**use_voucher_metadata_schema** | **bool** | Flag indicating whether the campaign is to use the voucher&#39;s metadata schema instead of the campaign metadata schema. | [optional] 
**vouchers_count** | **int** | Total number of unique vouchers in campaign (size of campaign). | [optional] 
**start_date** | **datetime** | Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date.  | [optional] 
**expiration_date** | **datetime** | Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date. | [optional] 
**validity_timeframe** | [**CampaignBaseValidityTimeframe**](CampaignBaseValidityTimeframe.md) |  | [optional] 
**validity_day_of_week** | **List[int]** | Integer array corresponding to the particular days of the week in which the campaign is valid.  - &#x60;0&#x60;  Sunday   - &#x60;1&#x60;  Monday   - &#x60;2&#x60;  Tuesday   - &#x60;3&#x60;  Wednesday   - &#x60;4&#x60;  Thursday   - &#x60;5&#x60;  Friday   - &#x60;6&#x60;  Saturday   | [optional] 
**activity_duration_after_publishing** | **str** | Defines the amount of time the campaign will be active in ISO 8601 format after publishing. For example, a campaign with a &#x60;duration&#x60; of &#x60;P24D&#x60; will be valid for a duration of 24 days. | [optional] 
**validation_rules** | **List[str]** | Array containing the ID of the validation rule associated with the promotion tier. | [optional] 
**category_id** | **str** | Unique category ID that this campaign belongs to. Either pass this parameter OR the &#x60;category&#x60;. | [optional] 
**category** | **str** | The category assigned to the campaign. Either pass this parameter OR the &#x60;category_id&#x60;. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the campaign. A set of key/value pairs that you can attach to a campaign object. It can be useful for storing additional information about the campaign in a structured format. | [optional] 
**campaign_type** | **str** | Type of campaign. | [optional] [default to 'LUCKY_DRAW']
**voucher** | [**GiveawayCampaignVoucher**](GiveawayCampaignVoucher.md) |  | [optional] 
**referral_program** | [**ReferralProgram**](ReferralProgram.md) |  | [optional] 
**promotion** | [**SchemaThatContainsUniquePropertiesForPromotionCampaignPromotion**](SchemaThatContainsUniquePropertiesForPromotionCampaignPromotion.md) |  | [optional] 
**lucky_draw** | [**LuckyDraw**](LuckyDraw.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

