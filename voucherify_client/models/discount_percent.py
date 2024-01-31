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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator
from voucherify_client.models.discount_percent_vouchers_effect_types import DiscountPercentVouchersEffectTypes

class DiscountPercent(BaseModel):
    """
    DiscountPercent
    """
    type: StrictStr = Field(..., description="Defines the type of the voucher.")
    percent_off: Union[StrictFloat, StrictInt] = Field(..., description="The percent discount that the customer will receive.")
    percent_off_formula: Optional[StrictStr] = None
    amount_limit: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Upper limit allowed to be applied as a discount. Value is multiplied by 100 to precisely represent 2 decimal places. For example, a $6 maximum discount is written as 600.")
    aggregated_amount_limit: Optional[StrictInt] = Field(None, description="Maximum discount amount per order.")
    effect: Optional[DiscountPercentVouchersEffectTypes] = None
    is_dynamic: Optional[StrictBool] = Field(None, description="Flag indicating whether the discount was calculated using a formula.")
    __properties = ["type", "percent_off", "percent_off_formula", "amount_limit", "aggregated_amount_limit", "effect", "is_dynamic"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('PERCENT',):
            raise ValueError("must be one of enum values ('PERCENT')")
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
    def from_json(cls, json_str: str) -> DiscountPercent:
        """Create an instance of DiscountPercent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiscountPercent:
        """Create an instance of DiscountPercent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DiscountPercent.parse_obj(obj)

        _obj = DiscountPercent.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'PERCENT',
            "percent_off": obj.get("percent_off"),
            "percent_off_formula": obj.get("percent_off_formula"),
            "amount_limit": obj.get("amount_limit"),
            "aggregated_amount_limit": obj.get("aggregated_amount_limit"),
            "effect": obj.get("effect"),
            "is_dynamic": obj.get("is_dynamic")
        })
        return _obj


