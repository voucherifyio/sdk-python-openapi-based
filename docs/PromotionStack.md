# PromotionStack


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Promotion stack name. | 
**tiers** | [**PromotionStackBaseTiers**](PromotionStackBaseTiers.md) |  | 
**id** | **str** | Unique promotion stack ID. | 
**created_at** | **datetime** | Timestamp representing the date and time when the promotion stack was created in ISO 8601 format. | 
**updated_at** | **datetime** | Timestamp representing the date and time when the promotion stack was updated in ISO 8601 format. | [optional] 
**campaign_id** | **str** | Promotion stack&#39;s parent campaign&#39;s unique ID. | 
**object** | **str** | The type of object represented by JSON.  | [default to 'promotion_stack']
**category_id** | **str** | Promotion stack category ID. | [optional] 
**categories** | [**List[Category]**](Category.md) | Details about the category assigned to the promotion stack. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


