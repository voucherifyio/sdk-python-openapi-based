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

class VoucherPublish(BaseModel):
    """
    Stores a summary of publication events: an event counter and endpoint to return details of each event. Publication is an assignment of a code to a customer, e.g. through a distribution.  # noqa: E501
    """
    object: Optional[StrictStr] = Field('list', description="The type of the object represented is by default `list`. To get this list, you need to make a call to the endpoint returned in the `url` attribute.")
    count: Optional[StrictInt] = Field(None, description="Publication events counter.")
    url: Optional[StrictStr] = Field(None, description="The endpoint where this list of publications can be accessed using a GET method. `/v1/vouchers/{voucher_code}/publications`")
    __properties = ["object", "count", "url"]

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
    def from_json(cls, json_str: str) -> VoucherPublish:
        """Create an instance of VoucherPublish from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if count (nullable) is None
        # and __fields_set__ contains the field
        if self.count is None and "count" in self.__fields_set__:
            _dict['count'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VoucherPublish:
        """Create an instance of VoucherPublish from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VoucherPublish.parse_obj(obj)

        _obj = VoucherPublish.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "count": obj.get("count"),
            "url": obj.get("url")
        })
        return _obj


