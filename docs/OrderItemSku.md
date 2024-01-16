# OrderItemSku

An object containing details of the related SKU.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier that represents the SKU and is assigned by Voucherify. | [optional] 
**source_id** | **str** | The merchant’s SKU ID (if it is different than Voucherify&#39;s SKU ID). It is really useful in case of integration between multiple systems. It can be an ID from an eCommerce site, a database or a 3rd party service. | [optional] 
**override** | **bool** | The override set to &#x60;true&#x60; is used to store the product information in the system. If the product does not exist, it will be created with a source_id; if it does exist, the provided values for the name, price, and metadata will replace those already stored in the system. | [optional] 
**sku** | **str** | The SKU name. | [optional] 
**price** | **float** | SKU price. A positive integer in the smallest currency unit (e.g. 100 cents for $1.00). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

