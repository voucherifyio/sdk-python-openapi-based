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
from pydantic import BaseModel, Field, StrictInt

class RedemptionRollbackGift(BaseModel):
    """
    Contains the amount returned to the gift card in the redemption rollback. It is expressed as a negative integer.  # noqa: E501
    """
    amount: Optional[StrictInt] = Field(None, description="Amount returned to the gift card as a result of the redemption rollback and expressed as a negative integer. The amount is expressed as the smallest currency unit (e.g. -100 cents for $1.00 returned).")
    __properties = ["amount"]

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
    def from_json(cls, json_str: str) -> RedemptionRollbackGift:
        """Create an instance of RedemptionRollbackGift from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if amount (nullable) is None
        # and __fields_set__ contains the field
        if self.amount is None and "amount" in self.__fields_set__:
            _dict['amount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionRollbackGift:
        """Create an instance of RedemptionRollbackGift from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionRollbackGift.parse_obj(obj)

        _obj = RedemptionRollbackGift.parse_obj({
            "amount": obj.get("amount")
        })
        return _obj


