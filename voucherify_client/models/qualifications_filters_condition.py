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
from pydantic import BaseModel, Field
from voucherify_client.models.any import Any

class QualificationsFiltersCondition(BaseModel):
    """
    QualificationsFiltersCondition
    """
    var_is: Optional[Any] = Field(None, alias="$is")
    is_not: Optional[Any] = Field(None, alias="$is_not")
    has_value: Optional[Any] = Field(None, alias="$has_value")
    is_unknown: Optional[Any] = Field(None, alias="$is_unknown")
    var_in: Optional[Any] = Field(None, alias="$in")
    not_in: Optional[Any] = Field(None, alias="$not_in")
    __properties = ["$is", "$is_not", "$has_value", "$is_unknown", "$in", "$not_in"]

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
    def from_json(cls, json_str: str) -> QualificationsFiltersCondition:
        """Create an instance of QualificationsFiltersCondition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_is
        if self.var_is:
            _dict['$is'] = self.var_is.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_not
        if self.is_not:
            _dict['$is_not'] = self.is_not.to_dict()
        # override the default output from pydantic by calling `to_dict()` of has_value
        if self.has_value:
            _dict['$has_value'] = self.has_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_unknown
        if self.is_unknown:
            _dict['$is_unknown'] = self.is_unknown.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_in
        if self.var_in:
            _dict['$in'] = self.var_in.to_dict()
        # override the default output from pydantic by calling `to_dict()` of not_in
        if self.not_in:
            _dict['$not_in'] = self.not_in.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QualificationsFiltersCondition:
        """Create an instance of QualificationsFiltersCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QualificationsFiltersCondition.parse_obj(obj)

        _obj = QualificationsFiltersCondition.parse_obj({
            "var_is": Any.from_dict(obj.get("$is")) if obj.get("$is") is not None else None,
            "is_not": Any.from_dict(obj.get("$is_not")) if obj.get("$is_not") is not None else None,
            "has_value": Any.from_dict(obj.get("$has_value")) if obj.get("$has_value") is not None else None,
            "is_unknown": Any.from_dict(obj.get("$is_unknown")) if obj.get("$is_unknown") is not None else None,
            "var_in": Any.from_dict(obj.get("$in")) if obj.get("$in") is not None else None,
            "not_in": Any.from_dict(obj.get("$not_in")) if obj.get("$not_in") is not None else None
        })
        return _obj

