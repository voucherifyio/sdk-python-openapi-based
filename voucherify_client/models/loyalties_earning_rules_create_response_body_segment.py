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

class LoyaltiesEarningRulesCreateResponseBodySegment(BaseModel):
    """
    Contains the ID of a customer segment. Required for the `customer.segment.entered` option in the event.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Contains a unique identifier of a customer segment. Assigned by the Voucherify API.")
    __properties = ["id"]

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
    def from_json(cls, json_str: str) -> LoyaltiesEarningRulesCreateResponseBodySegment:
        """Create an instance of LoyaltiesEarningRulesCreateResponseBodySegment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesEarningRulesCreateResponseBodySegment:
        """Create an instance of LoyaltiesEarningRulesCreateResponseBodySegment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesEarningRulesCreateResponseBodySegment.parse_obj(obj)

        _obj = LoyaltiesEarningRulesCreateResponseBodySegment.parse_obj({
            "id": obj.get("id")
        })
        return _obj


