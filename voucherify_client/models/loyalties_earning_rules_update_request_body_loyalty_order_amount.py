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

class LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderAmount(BaseModel):
    """
    Defines the ratio based on the property defined in the calculation_type parameter. For every set of value (1, 10, etc) defined in the every parameter for the property defined in calculation_type, give the customer the number of points defined in the points parameter. In other words, for every calculation_type, give points.  # noqa: E501
    """
    every: Optional[StrictInt] = Field(None, description="Value is multiplied by 100 to precisely represent 2 decimal places. For example, a $10 order amount is written as 1000.")
    points: Optional[StrictInt] = Field(None, description="Number of points to be awarded, i.e. how many points to be added to the loyalty card.")
    __properties = ["every", "points"]

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
    def from_json(cls, json_str: str) -> LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderAmount:
        """Create an instance of LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderAmount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if every (nullable) is None
        # and __fields_set__ contains the field
        if self.every is None and "every" in self.__fields_set__:
            _dict['every'] = None

        # set to None if points (nullable) is None
        # and __fields_set__ contains the field
        if self.points is None and "points" in self.__fields_set__:
            _dict['points'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderAmount:
        """Create an instance of LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderAmount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderAmount.parse_obj(obj)

        _obj = LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderAmount.parse_obj({
            "every": obj.get("every"),
            "points": obj.get("points")
        })
        return _obj


