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

class ValidationsRedeemableInapplicableResultDetails(BaseModel):
    """
    Provides details about the reason why the redeemable is inapplicable.  # noqa: E501
    """
    message: Optional[StrictStr] = Field(None, description="Generic message from the `message` string shown in the `error` object or the message configured in a validation rule.")
    key: Optional[StrictStr] = Field(None, description="Generic message from the `key` string shown in the `error` object.")
    __properties = ["message", "key"]

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
    def from_json(cls, json_str: str) -> ValidationsRedeemableInapplicableResultDetails:
        """Create an instance of ValidationsRedeemableInapplicableResultDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if message (nullable) is None
        # and __fields_set__ contains the field
        if self.message is None and "message" in self.__fields_set__:
            _dict['message'] = None

        # set to None if key (nullable) is None
        # and __fields_set__ contains the field
        if self.key is None and "key" in self.__fields_set__:
            _dict['key'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidationsRedeemableInapplicableResultDetails:
        """Create an instance of ValidationsRedeemableInapplicableResultDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidationsRedeemableInapplicableResultDetails.parse_obj(obj)

        _obj = ValidationsRedeemableInapplicableResultDetails.parse_obj({
            "message": obj.get("message"),
            "key": obj.get("key")
        })
        return _obj


