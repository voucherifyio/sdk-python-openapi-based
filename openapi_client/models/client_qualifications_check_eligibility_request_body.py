# coding: utf-8

"""
    Voucherify API

    Voucherify promotion engine REST API. Please see https://docs.voucherify.io/docs for more details.

    The version of the OpenAPI document: v2018-08-01
    Contact: support@voucherify.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.client_qualifications_check_eligibility_request_body_options import ClientQualificationsCheckEligibilityRequestBodyOptions
from openapi_client.models.customer import Customer
from openapi_client.models.order import Order

class ClientQualificationsCheckEligibilityRequestBody(BaseModel):
    """
    Request body schema for **POST** `/qualifications`.  # noqa: E501
    """
    customer: Optional[Customer] = None
    order: Optional[Order] = None
    mode: Optional[StrictStr] = Field(None, description="Defines which resources Voucherify will use. The `ADVANCED` mode is available after purchase only.")
    tracking_id: Optional[StrictStr] = Field(None, description="Is correspondent to Customer's source_id")
    scenario: Optional[StrictStr] = Field(None, description="Defines the scenario Voucherify should consider during the qualification process.  - `ALL` - Scenario that returns all redeemables available for the customer in one API request. This scenario is used by default when no value is selected. - `CUSTOMER_WALLET` - returns vouchers applicable to the customer’s cart based on the vouchers assigned to the customer’s profile. - `AUDIENCE_ONLY` - returns all vouchers, promotion tiers, and campaigns available to the customer. Voucherify validates the rules based on the customer profile only. - `PRODUCTS` - returns all promotions available for the products (when a discount is defined to be applied to the item or when the item is required in the validation rule). - `PRODUCTS_DISCOUNT` - returns all promotions available for products when a discount is defined as applicable to specific item(s). - `PROMOTION_STACKS` - returns the applicable promotion stacks. - `PRODUCTS_BY_CUSTOMER` - returns all promotions available for a customer for the products (when a discount is defined to be applied to the item or when the item is required in the validation rule). - `PRODUCTS_DISCOUNT_BY_CUSTOMER` - returns all promotions available for a customer for products when a discount is defined as applicable to specific item(s).")
    options: Optional[ClientQualificationsCheckEligibilityRequestBodyOptions] = None
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of key/value pairs that you can send in the request body to check against redeemables requiring **redemption** metadata validation rules to be satisfied. The validation runs against rules that are defined through the <!-- [Create Validation Rules](https://docs.voucherify.io/reference/create-validation-rules) -->[Create Validation Rules](ref:create-validation-rules) endpoint or via the Dashboard; in the _Advanced Rule Builder_ &rarr; _Advanced_ &rarr; _Redemption metadata satisfy_ or _Basic Builder_ &rarr; _Attributes match_ &rarr; _REDEMPTION METADATA_. [Read more](https://support.voucherify.io/article/148-how-to-build-a-rule).")
    __properties = ["customer", "order", "mode", "tracking_id", "scenario", "options", "metadata"]

    @validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BASIC', 'ADVANCED',):
            raise ValueError("must be one of enum values ('BASIC', 'ADVANCED')")
        return value

    @validator('scenario')
    def scenario_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ALL', 'CUSTOMER_WALLET', 'AUDIENCE_ONLY', 'PRODUCTS', 'PRODUCTS_DISCOUNT', 'PROMOTION_STACKS', 'PRODUCTS_BY_CUSTOMER', 'PRODUCTS_DISCOUNT_BY_CUSTOMER',):
            raise ValueError("must be one of enum values ('ALL', 'CUSTOMER_WALLET', 'AUDIENCE_ONLY', 'PRODUCTS', 'PRODUCTS_DISCOUNT', 'PROMOTION_STACKS', 'PRODUCTS_BY_CUSTOMER', 'PRODUCTS_DISCOUNT_BY_CUSTOMER')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ClientQualificationsCheckEligibilityRequestBody:
        """Create an instance of ClientQualificationsCheckEligibilityRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClientQualificationsCheckEligibilityRequestBody:
        """Create an instance of ClientQualificationsCheckEligibilityRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClientQualificationsCheckEligibilityRequestBody.parse_obj(obj)

        _obj = ClientQualificationsCheckEligibilityRequestBody.parse_obj({
            "customer": Customer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "order": Order.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "mode": obj.get("mode"),
            "tracking_id": obj.get("tracking_id"),
            "scenario": obj.get("scenario"),
            "options": ClientQualificationsCheckEligibilityRequestBodyOptions.from_dict(obj.get("options")) if obj.get("options") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


