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
from pydantic import BaseModel
from openapi_client.models.filter_conditions_string import FilterConditionsString
from openapi_client.models.junction import Junction

class ParameterFiltersListRedemptionsRelatedObjectId(BaseModel):
    """
    Unique related object ID, i.e. v_hS8JFl8S6lNcd1L69wLIoXgTio7eWEgk.  # noqa: E501
    """
    conditions: Optional[FilterConditionsString] = None
    junction: Optional[Junction] = None
    __properties = ["conditions", "junction"]

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
    def from_json(cls, json_str: str) -> ParameterFiltersListRedemptionsRelatedObjectId:
        """Create an instance of ParameterFiltersListRedemptionsRelatedObjectId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of conditions
        if self.conditions:
            _dict['conditions'] = self.conditions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParameterFiltersListRedemptionsRelatedObjectId:
        """Create an instance of ParameterFiltersListRedemptionsRelatedObjectId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ParameterFiltersListRedemptionsRelatedObjectId.parse_obj(obj)

        _obj = ParameterFiltersListRedemptionsRelatedObjectId.parse_obj({
            "conditions": FilterConditionsString.from_dict(obj.get("conditions")) if obj.get("conditions") is not None else None,
            "junction": obj.get("junction")
        })
        return _obj

