# LoyaltyTier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Loyalty Tier name. | 
**earning_rules** | **object** | Contains a list of earning rule IDs and their points mapping for the given earning rule. | [optional] 
**rewards** | **object** | Contains a list of reward IDs and their points mapping for the given reward. | [optional] 
**points** | [**LoyaltyTierBasePoints**](LoyaltyTierBasePoints.md) |  | 
**id** | **str** | Unique loyalty tier ID. | 
**campaign_id** | **str** | Unique parent campaign ID. | 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the loyalty tier. A set of key/value pairs that you can attach to a loyalty tier object. It can be useful for storing additional information about the loyalty tier in a structured format. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the loyalty tier was created in ISO 8601 format. | 
**updated_at** | **datetime** | Timestamp representing the date and time when the loyalty tier was updated in ISO 8601 format. | [optional] 
**config** | [**LoyaltyTierAllOfConfig**](LoyaltyTierAllOfConfig.md) |  | 
**expiration** | [**LoyaltyTierExpiration**](LoyaltyTierExpiration.md) |  | [optional] 
**object** | **str** | The type of object represented by JSON. This object stores information about the loyalty. | [default to 'loyalty_tier']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


