# SimpleCampaign

Request body schema for creating a discount voucher campaign using **POST** `/campaigns`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Campaign name. | [optional] 
**name** | **str** | Campaign name. | [optional] 
**campaign_type** | **str** | Type of campaign. | [optional] 
**type** | **str** | Defines whether the campaign can be updated with new vouchers after campaign creation. - &#x60;AUTO_UPDATE&#x60;: By choosing the auto update option you will create a campaign that can be enhanced by new vouchers after the time of creation (e.g. by publish vouchers method). -  &#x60;STATIC&#x60;: vouchers need to be manually published. | [optional] 
**is_referral_code** | **bool** | Flag indicating whether this voucher is a referral code; &#x60;true&#x60; for campaign type &#x60;REFERRAL_PROGRAM&#x60;. | [optional] 
**voucher** | **object** |  | [optional] 
**lucky_draw** | **object** |  | [optional] 
**referral_program** | [**ReferralProgram**](ReferralProgram.md) |  | [optional] 
**auto_join** | **bool** | Indicates whether customers will be able to auto-join a loyalty campaign if any earning rule is fulfilled. | [optional] 
**join_once** | **bool** | If this value is set to &#x60;true&#x60;, customers will be able to join the campaign only once. | [optional] 
**active** | **bool** | Indicates whether campaign is active | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the campaign was created in ISO 8601 format. | [optional] 
**object** | **str** | The type of object represented by JSON. This object stores information about the campaign. | [optional] [default to 'campaign']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


