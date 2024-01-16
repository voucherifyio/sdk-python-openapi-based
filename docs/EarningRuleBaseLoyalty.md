# EarningRuleBaseLoyalty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The number of points to be added to the loyalty card. | [default to 'FIXED']
**points** | **int** | Defines how the points will be added to the loyalty card. FIXED adds a fixed number of points. | [optional] 
**calculation_type** | **str** | CUSTOM_EVENT_METADATA: Custom event metadata (X points for every Y in metadata attribute). | [default to 'CUSTOM_EVENT_METADATA']
**order** | [**EarningRuleProportionalOrderMetadataOrder**](EarningRuleProportionalOrderMetadataOrder.md) |  | 
**order_items** | [**EarningRuleProportionalOrderItemsSubtotalAmountOrderItems**](EarningRuleProportionalOrderItemsSubtotalAmountOrderItems.md) |  | 
**customer** | [**EarningRuleProportionalCustomerMetadataCustomer**](EarningRuleProportionalCustomerMetadataCustomer.md) |  | 
**custom_event** | [**EarningRuleProportionalCustomEventCustomEvent**](EarningRuleProportionalCustomEventCustomEvent.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


