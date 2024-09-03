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
from pydantic import BaseModel, Field, StrictStr, validator

class LoyaltiesEarningRulesEnableResponseBodySource(BaseModel):
    """
    Contains the custom earning rule name and parent campaign.  # noqa: E501
    """
    banner: Optional[StrictStr] = Field(None, description="Name of the earning rule. This is displayed as a header for the earning rule in the Dashboard.")
    object_id: Optional[StrictStr] = Field(None, description="A unique campaign identifier assigned by the Voucherify API.")
    object_type: Optional[StrictStr] = Field('campaign', description="Defines the object associated with the earning rule. Defaults to `campaign`.")
    __properties = ["banner", "object_id", "object_type"]

    @validator('object_type')
    def object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('campaign',):
            raise ValueError("must be one of enum values ('campaign')")
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
    def from_json(cls, json_str: str) -> LoyaltiesEarningRulesEnableResponseBodySource:
        """Create an instance of LoyaltiesEarningRulesEnableResponseBodySource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if banner (nullable) is None
        # and __fields_set__ contains the field
        if self.banner is None and "banner" in self.__fields_set__:
            _dict['banner'] = None

        # set to None if object_id (nullable) is None
        # and __fields_set__ contains the field
        if self.object_id is None and "object_id" in self.__fields_set__:
            _dict['object_id'] = None

        # set to None if object_type (nullable) is None
        # and __fields_set__ contains the field
        if self.object_type is None and "object_type" in self.__fields_set__:
            _dict['object_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesEarningRulesEnableResponseBodySource:
        """Create an instance of LoyaltiesEarningRulesEnableResponseBodySource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesEarningRulesEnableResponseBodySource.parse_obj(obj)

        _obj = LoyaltiesEarningRulesEnableResponseBodySource.parse_obj({
            "banner": obj.get("banner"),
            "object_id": obj.get("object_id"),
            "object_type": obj.get("object_type") if obj.get("object_type") is not None else 'campaign'
        })
        return _obj


