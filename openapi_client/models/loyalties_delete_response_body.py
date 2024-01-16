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



from pydantic import BaseModel, Field, StrictStr

class LoyaltiesDeleteResponseBody(BaseModel):
    """
    Response body schema for **DELETE** `/loyalties/{campaignId}`.  # noqa: E501
    """
    async_action_id: StrictStr = Field(..., description="The ID of the scheduled asynchronous action.")
    __properties = ["async_action_id"]

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
    def from_json(cls, json_str: str) -> LoyaltiesDeleteResponseBody:
        """Create an instance of LoyaltiesDeleteResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesDeleteResponseBody:
        """Create an instance of LoyaltiesDeleteResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesDeleteResponseBody.parse_obj(obj)

        _obj = LoyaltiesDeleteResponseBody.parse_obj({
            "async_action_id": obj.get("async_action_id")
        })
        return _obj


