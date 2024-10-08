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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class Error(BaseModel):
    """
    Error details  # noqa: E501
    """
    code: Optional[StrictInt] = Field(None, description="Error's HTTP status code.")
    key: Optional[StrictStr] = Field(None, description="Short string describing the kind of error which occurred.")
    message: Optional[StrictStr] = Field(None, description="A human-readable message providing a short description about the error.")
    details: Optional[StrictStr] = Field(None, description="A human-readable message providing more details about the error.")
    request_id: Optional[StrictStr] = Field(None, description="This ID is useful when troubleshooting and/or finding the root cause of an error response by our support team.")
    resource_id: Optional[StrictStr] = Field(None, description="Unique resource ID that can be used in another endpoint to get more details.")
    resource_type: Optional[StrictStr] = Field(None, description="The resource type.")
    __properties = ["code", "key", "message", "details", "request_id", "resource_id", "resource_type"]

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
    def from_json(cls, json_str: str) -> Error:
        """Create an instance of Error from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if code (nullable) is None
        # and __fields_set__ contains the field
        if self.code is None and "code" in self.__fields_set__:
            _dict['code'] = None

        # set to None if key (nullable) is None
        # and __fields_set__ contains the field
        if self.key is None and "key" in self.__fields_set__:
            _dict['key'] = None

        # set to None if message (nullable) is None
        # and __fields_set__ contains the field
        if self.message is None and "message" in self.__fields_set__:
            _dict['message'] = None

        # set to None if details (nullable) is None
        # and __fields_set__ contains the field
        if self.details is None and "details" in self.__fields_set__:
            _dict['details'] = None

        # set to None if request_id (nullable) is None
        # and __fields_set__ contains the field
        if self.request_id is None and "request_id" in self.__fields_set__:
            _dict['request_id'] = None

        # set to None if resource_id (nullable) is None
        # and __fields_set__ contains the field
        if self.resource_id is None and "resource_id" in self.__fields_set__:
            _dict['resource_id'] = None

        # set to None if resource_type (nullable) is None
        # and __fields_set__ contains the field
        if self.resource_type is None and "resource_type" in self.__fields_set__:
            _dict['resource_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Error:
        """Create an instance of Error from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Error.parse_obj(obj)

        _obj = Error.parse_obj({
            "code": obj.get("code"),
            "key": obj.get("key"),
            "message": obj.get("message"),
            "details": obj.get("details"),
            "request_id": obj.get("request_id"),
            "resource_id": obj.get("resource_id"),
            "resource_type": obj.get("resource_type")
        })
        return _obj


