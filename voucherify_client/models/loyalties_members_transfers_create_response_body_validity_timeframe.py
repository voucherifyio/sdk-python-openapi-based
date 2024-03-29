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

class LoyaltiesMembersTransfersCreateResponseBodyValidityTimeframe(BaseModel):
    """
    Set recurrent time periods when the voucher is valid. For example, valid for 1 hour every other day.start_date required when including the validity_timeframe.  # noqa: E501
    """
    interval: Optional[StrictStr] = Field(None, description="Defines the amount of time the voucher will be active in ISO 8601 format. For example, a voucher with a duration of PT1H will be valid for a duration of one hour.")
    duration: Optional[StrictStr] = Field(None, description="Defines the intervening time between two time points in ISO 8601 format, expressed as a duration. For example, a voucher with an interval of P2D will be active every other day.")
    __properties = ["interval", "duration"]

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
    def from_json(cls, json_str: str) -> LoyaltiesMembersTransfersCreateResponseBodyValidityTimeframe:
        """Create an instance of LoyaltiesMembersTransfersCreateResponseBodyValidityTimeframe from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesMembersTransfersCreateResponseBodyValidityTimeframe:
        """Create an instance of LoyaltiesMembersTransfersCreateResponseBodyValidityTimeframe from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesMembersTransfersCreateResponseBodyValidityTimeframe.parse_obj(obj)

        _obj = LoyaltiesMembersTransfersCreateResponseBodyValidityTimeframe.parse_obj({
            "interval": obj.get("interval"),
            "duration": obj.get("duration")
        })
        return _obj


