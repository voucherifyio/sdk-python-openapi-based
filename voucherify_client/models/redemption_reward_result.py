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
from voucherify_client.models.product import Product
from voucherify_client.models.redemption_reward_result_parameters import RedemptionRewardResultParameters
from voucherify_client.models.simple_customer import SimpleCustomer
from voucherify_client.models.sku import Sku
from voucherify_client.models.voucher import Voucher

class RedemptionRewardResult(BaseModel):
    """
    RedemptionRewardResult
    """
    customer: Optional[SimpleCustomer] = None
    assignment_id: Optional[StrictStr] = Field(None, description="Unique reward assignment ID assigned by Voucherify.")
    voucher: Optional[Voucher] = None
    product: Optional[Product] = None
    sku: Optional[Sku] = None
    loyalty_tier_id: Optional[StrictStr] = Field(None, description="Unique loyalty tier ID assigned by Voucherify.")
    id: Optional[StrictStr] = Field(None, description="Unique reward ID.")
    name: Optional[StrictStr] = Field(None, description="Name of the reward.")
    object: Optional[StrictStr] = Field('reward', description="The type of the object represented by the JSON")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the redemption was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp in ISO 8601 format indicating when the reward was updated.")
    parameters: Optional[RedemptionRewardResultParameters] = None
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of custom key/value pairs that you can attach to a reward. The metadata object stores all custom attributes assigned to the reward.")
    type: Optional[StrictStr] = Field(None, description="Reward type.")
    __properties = ["customer", "assignment_id", "voucher", "product", "sku", "loyalty_tier_id", "id", "name", "object", "created_at", "updated_at", "parameters", "metadata", "type"]

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
    def from_json(cls, json_str: str) -> RedemptionRewardResult:
        """Create an instance of RedemptionRewardResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        # set to None if assignment_id (nullable) is None
        # and __fields_set__ contains the field
        if self.assignment_id is None and "assignment_id" in self.__fields_set__:
            _dict['assignment_id'] = None

        # set to None if loyalty_tier_id (nullable) is None
        # and __fields_set__ contains the field
        if self.loyalty_tier_id is None and "loyalty_tier_id" in self.__fields_set__:
            _dict['loyalty_tier_id'] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if parameters (nullable) is None
        # and __fields_set__ contains the field
        if self.parameters is None and "parameters" in self.__fields_set__:
            _dict['parameters'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionRewardResult:
        """Create an instance of RedemptionRewardResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionRewardResult.parse_obj(obj)

        _obj = RedemptionRewardResult.parse_obj({
            "customer": SimpleCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "assignment_id": obj.get("assignment_id"),
            "voucher": Voucher.from_dict(obj.get("voucher")) if obj.get("voucher") is not None else None,
            "product": Product.from_dict(obj.get("product")) if obj.get("product") is not None else None,
            "sku": Sku.from_dict(obj.get("sku")) if obj.get("sku") is not None else None,
            "loyalty_tier_id": obj.get("loyalty_tier_id"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "object": obj.get("object") if obj.get("object") is not None else 'reward',
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "parameters": RedemptionRewardResultParameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None,
            "metadata": obj.get("metadata"),
            "type": obj.get("type")
        })
        return _obj


