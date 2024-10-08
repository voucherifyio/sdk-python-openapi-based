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


from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class QualificationsFiltersCondition(BaseModel):
    """
    QualificationsFiltersCondition
    """
    var_is: Optional[conlist(StrictStr)] = Field(None, alias="$is")
    is_not: Optional[conlist(StrictStr)] = Field(None, alias="$is_not")
    has_value: Optional[Any] = Field(None, alias="$has_value")
    is_unknown: Optional[Any] = Field(None, alias="$is_unknown")
    var_in: Optional[conlist(StrictStr)] = Field(None, alias="$in")
    not_in: Optional[conlist(StrictStr)] = Field(None, alias="$not_in")
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
        # set to None if var_is (nullable) is None
        # and __fields_set__ contains the field
        if self.var_is is None and "var_is" in self.__fields_set__:
            _dict['$is'] = None

        # set to None if is_not (nullable) is None
        # and __fields_set__ contains the field
        if self.is_not is None and "is_not" in self.__fields_set__:
            _dict['$is_not'] = None

        # set to None if has_value (nullable) is None
        # and __fields_set__ contains the field
        if self.has_value is None and "has_value" in self.__fields_set__:
            _dict['$has_value'] = None

        # set to None if is_unknown (nullable) is None
        # and __fields_set__ contains the field
        if self.is_unknown is None and "is_unknown" in self.__fields_set__:
            _dict['$is_unknown'] = None

        # set to None if var_in (nullable) is None
        # and __fields_set__ contains the field
        if self.var_in is None and "var_in" in self.__fields_set__:
            _dict['$in'] = None

        # set to None if not_in (nullable) is None
        # and __fields_set__ contains the field
        if self.not_in is None and "not_in" in self.__fields_set__:
            _dict['$not_in'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QualificationsFiltersCondition:
        """Create an instance of QualificationsFiltersCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QualificationsFiltersCondition.parse_obj(obj)

        _obj = QualificationsFiltersCondition.parse_obj({
            "var_is": obj.get("$is"),
            "is_not": obj.get("$is_not"),
            "has_value": obj.get("$has_value"),
            "is_unknown": obj.get("$is_unknown"),
            "var_in": obj.get("$in"),
            "not_in": obj.get("$not_in")
        })
        return _obj


