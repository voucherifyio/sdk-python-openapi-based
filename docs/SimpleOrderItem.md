# SimpleOrderItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of object represented by JSON. This object stores information about the &#x60;order_item&#x60;. | [optional] [default to 'order_item']
**source_id** | **str** | The merchant’s product/SKU ID (if it is different from the Voucherify product/SKU ID). It is useful in the integration between multiple systems. It can be an ID from an eCommerce site, a database, or a third-party service. | [optional] 
**related_object** | **str** | Used along with the source_id property, can be set to either sku or product. | [optional] 
**product_id** | **str** | A unique product ID assigned by Voucherify. | [optional] 
**sku_id** | **str** | A unique SKU ID assigned by Voucherify. | [optional] 
**quantity** | **int** | The quantity of the particular item in the cart. | [optional] 
**discount_quantity** | **int** | Number of dicounted items. | [optional] 
**amount** | **int** | The total amount of the order item (price * quantity). | [optional] 
**discount_amount** | **int** |  Sum of all order-item-level discounts applied to the order. | [optional] 
**applied_discount_amount** | **int** | This field shows the order-level discount applied. | [optional] 
**price** | **int** | Unit price of an item. Value is multiplied by 100 to precisely represent 2 decimal places. For example &#x60;10000 cents&#x60; for &#x60;$100.00&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


