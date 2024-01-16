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



from pydantic import BaseModel, Field, StrictStr

class EarningRuleBaseValidityTimeframe(BaseModel):
    """
    Set recurrent time periods when the earning rule is valid. For example, valid for 1 hour every other day.start_date required when including the `validity_timeframe`.  # noqa: E501
    """
    duration: StrictStr = Field(..., description="Defines the amount of time an earning rule will be active in ISO 8601 format. For example, an earning rule with a duration of PT1H will be valid for a duration of one hour.")
    interval: StrictStr = Field(..., description="Defines the intervening time between two time points in ISO 8601 format, expressed as a duration. For example, an earning rule with an interval of P2D will be valid every other day.")
    __properties = ["duration", "interval"]

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
    def from_json(cls, json_str: str) -> EarningRuleBaseValidityTimeframe:
        """Create an instance of EarningRuleBaseValidityTimeframe from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EarningRuleBaseValidityTimeframe:
        """Create an instance of EarningRuleBaseValidityTimeframe from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EarningRuleBaseValidityTimeframe.parse_obj(obj)

        _obj = EarningRuleBaseValidityTimeframe.parse_obj({
            "duration": obj.get("duration"),
            "interval": obj.get("interval")
        })
        return _obj

