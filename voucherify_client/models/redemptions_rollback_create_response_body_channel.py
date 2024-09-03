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

class RedemptionsRollbackCreateResponseBodyChannel(BaseModel):
    """
    Defines the details of the channel through which the redemption was issued.  # noqa: E501
    """
    channel_id: Optional[StrictStr] = Field(None, description="Unique identifier of the channel which was used by the user performing the redemption rollback. This is either a user ID from the user using the Voucherify Dashboard or an X-APP-Id of a user using the API.")
    channel_type: Optional[StrictStr] = Field(None, description="The source of the channel for the redemption. A `USER` corresponds to the Voucherify Dashboard and an `API` corresponds to the API.")
    __properties = ["channel_id", "channel_type"]

    @validator('channel_type')
    def channel_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('USER', 'API',):
            raise ValueError("must be one of enum values ('USER', 'API')")
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
    def from_json(cls, json_str: str) -> RedemptionsRollbackCreateResponseBodyChannel:
        """Create an instance of RedemptionsRollbackCreateResponseBodyChannel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if channel_id (nullable) is None
        # and __fields_set__ contains the field
        if self.channel_id is None and "channel_id" in self.__fields_set__:
            _dict['channel_id'] = None

        # set to None if channel_type (nullable) is None
        # and __fields_set__ contains the field
        if self.channel_type is None and "channel_type" in self.__fields_set__:
            _dict['channel_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionsRollbackCreateResponseBodyChannel:
        """Create an instance of RedemptionsRollbackCreateResponseBodyChannel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionsRollbackCreateResponseBodyChannel.parse_obj(obj)

        _obj = RedemptionsRollbackCreateResponseBodyChannel.parse_obj({
            "channel_id": obj.get("channel_id"),
            "channel_type": obj.get("channel_type")
        })
        return _obj

