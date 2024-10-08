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

class LoyaltiesRewardAssignmentsRewardGetResponseBodyAttributes(BaseModel):
    """
    These properties are configurable for **material rewards**.  # noqa: E501
    """
    image_url: Optional[StrictStr] = Field(None, description="The HTTPS URL pointing to the .png or .jpg file.")
    description: Optional[StrictStr] = Field(None, description="An arbitrary string that you can attach to a material reward.")
    __properties = ["image_url", "description"]

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
    def from_json(cls, json_str: str) -> LoyaltiesRewardAssignmentsRewardGetResponseBodyAttributes:
        """Create an instance of LoyaltiesRewardAssignmentsRewardGetResponseBodyAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.image_url is None and "image_url" in self.__fields_set__:
            _dict['image_url'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesRewardAssignmentsRewardGetResponseBodyAttributes:
        """Create an instance of LoyaltiesRewardAssignmentsRewardGetResponseBodyAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesRewardAssignmentsRewardGetResponseBodyAttributes.parse_obj(obj)

        _obj = LoyaltiesRewardAssignmentsRewardGetResponseBodyAttributes.parse_obj({
            "image_url": obj.get("image_url"),
            "description": obj.get("description")
        })
        return _obj


