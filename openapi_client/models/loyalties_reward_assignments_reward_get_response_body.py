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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from openapi_client.models.reward_attributes import RewardAttributes
from openapi_client.models.reward_type import RewardType

class LoyaltiesRewardAssignmentsRewardGetResponseBody(BaseModel):
    """
    Response body schema for **GET** `/loyalties/{campaignId}/reward-assignments/{assignmentId}/reward`  # noqa: E501
    """
    id: StrictStr = Field(..., description="Unique reward ID, assigned by Voucherify.")
    name: StrictStr = Field(..., description="Reward name.")
    stock: Optional[StrictInt] = Field(None, description="Configurable for **material rewards**. The number of units of the product that you want to share as reward.")
    redeemed: Optional[StrictInt] = Field(None, description="Defines the number of already invoked (successful) reward redemptions. ")
    attributes: Optional[RewardAttributes] = None
    metadata: Dict[str, Any] = Field(..., description="The metadata object stores all custom attributes assigned to the reward. A set of key/value pairs that you can attach to a reward object. It can be useful for storing additional information about the reward in a structured format.")
    type: StrictStr = Field(..., description="Reward type.")
    parameters: Optional[RewardType] = None
    created_at: datetime = Field(..., description="Timestamp representing the date and time when the reward was created in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the reward was updated in ISO 8601 format.")
    object: StrictStr = Field(..., description="The type of object represented by the JSON. This object stores information about the reward.")
    __properties = ["id", "name", "stock", "redeemed", "attributes", "metadata", "type", "parameters", "created_at", "updated_at", "object"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CAMPAIGN', 'COIN', 'MATERIAL',):
            raise ValueError("must be one of enum values ('CAMPAIGN', 'COIN', 'MATERIAL')")
        return value

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('reward',):
            raise ValueError("must be one of enum values ('reward')")
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
    def from_json(cls, json_str: str) -> LoyaltiesRewardAssignmentsRewardGetResponseBody:
        """Create an instance of LoyaltiesRewardAssignmentsRewardGetResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        # set to None if stock (nullable) is None
        # and __fields_set__ contains the field
        if self.stock is None and "stock" in self.__fields_set__:
            _dict['stock'] = None

        # set to None if redeemed (nullable) is None
        # and __fields_set__ contains the field
        if self.redeemed is None and "redeemed" in self.__fields_set__:
            _dict['redeemed'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesRewardAssignmentsRewardGetResponseBody:
        """Create an instance of LoyaltiesRewardAssignmentsRewardGetResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesRewardAssignmentsRewardGetResponseBody.parse_obj(obj)

        _obj = LoyaltiesRewardAssignmentsRewardGetResponseBody.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "stock": obj.get("stock"),
            "redeemed": obj.get("redeemed"),
            "attributes": RewardAttributes.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None,
            "metadata": obj.get("metadata"),
            "type": obj.get("type"),
            "parameters": RewardType.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "object": obj.get("object") if obj.get("object") is not None else 'reward'
        })
        return _obj


