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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class VoucherTransactionDetailsEarningRuleSource(BaseModel):
    """
    Contains the custom earning rule name.  # noqa: E501
    """
    banner: Optional[StrictStr] = Field(None, description="Name of the earning rule. This is displayed as a header for the earning rule in the Dashboard.")
    __properties = ["banner"]

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
    def from_json(cls, json_str: str) -> VoucherTransactionDetailsEarningRuleSource:
        """Create an instance of VoucherTransactionDetailsEarningRuleSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if banner (nullable) is None
        # and __fields_set__ contains the field
        if self.banner is None and "banner" in self.__fields_set__:
            _dict['banner'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VoucherTransactionDetailsEarningRuleSource:
        """Create an instance of VoucherTransactionDetailsEarningRuleSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VoucherTransactionDetailsEarningRuleSource.parse_obj(obj)

        _obj = VoucherTransactionDetailsEarningRuleSource.parse_obj({
            "banner": obj.get("banner")
        })
        return _obj


