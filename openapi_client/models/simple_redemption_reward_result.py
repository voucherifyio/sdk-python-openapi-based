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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.simple_customer import SimpleCustomer
from openapi_client.models.simple_product import SimpleProduct
from openapi_client.models.simple_sku import SimpleSku
from openapi_client.models.simple_voucher import SimpleVoucher

class SimpleRedemptionRewardResult(BaseModel):
    """
    SimpleRedemptionRewardResult
    """
    customer: Optional[SimpleCustomer] = None
    assignment_id: Optional[StrictStr] = Field(None, description="Unique reward assignment ID assigned by Voucherify.")
    voucher: Optional[SimpleVoucher] = None
    product: Optional[SimpleProduct] = None
    sku: Optional[SimpleSku] = None
    loyalty_tier_id: Optional[StrictStr] = Field(None, description="Unique loyalty tier ID assigned by Voucherify.")
    id: Optional[StrictStr] = Field(None, description="Unique reward ID, assigned by Voucherify.")
    object: Optional[StrictStr] = Field('reward', description="The type of object represented by the JSON. This object stores information about the reward.")
    name: Optional[StrictStr] = Field(None, description="Reward name.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the reward was created in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the reward was updated in ISO 8601 format.")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Defines how the reward is generated.")
    type: Optional[StrictStr] = Field(None, description="Reward type.")
    __properties = ["customer", "assignment_id", "voucher", "product", "sku", "loyalty_tier_id", "id", "object", "name", "created_at", "updated_at", "parameters", "type"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('reward',):
            raise ValueError("must be one of enum values ('reward')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CAMPAIGN', 'COIN', 'MATERIAL',):
            raise ValueError("must be one of enum values ('CAMPAIGN', 'COIN', 'MATERIAL')")
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
    def from_json(cls, json_str: str) -> SimpleRedemptionRewardResult:
        """Create an instance of SimpleRedemptionRewardResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sku
        if self.sku:
            _dict['sku'] = self.sku.to_dict()
        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SimpleRedemptionRewardResult:
        """Create an instance of SimpleRedemptionRewardResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SimpleRedemptionRewardResult.parse_obj(obj)

        _obj = SimpleRedemptionRewardResult.parse_obj({
            "customer": SimpleCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "assignment_id": obj.get("assignment_id"),
            "voucher": SimpleVoucher.from_dict(obj.get("voucher")) if obj.get("voucher") is not None else None,
            "product": SimpleProduct.from_dict(obj.get("product")) if obj.get("product") is not None else None,
            "sku": SimpleSku.from_dict(obj.get("sku")) if obj.get("sku") is not None else None,
            "loyalty_tier_id": obj.get("loyalty_tier_id"),
            "id": obj.get("id"),
            "object": obj.get("object") if obj.get("object") is not None else 'reward',
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "parameters": obj.get("parameters"),
            "type": obj.get("type")
        })
        return _obj

