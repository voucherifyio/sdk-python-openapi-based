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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from voucherify_client.models.rewards_create_request_body_attributes import RewardsCreateRequestBodyAttributes
from voucherify_client.models.rewards_create_request_body_parameters import RewardsCreateRequestBodyParameters

class RewardsCreateRequestBody(BaseModel):
    """
    RewardsCreateRequestBody
    """
    name: Optional[StrictStr] = Field(None, description="Reward name.")
    parameters: Optional[RewardsCreateRequestBodyParameters] = None
    metadata: Optional[Dict[str, Any]] = None
    stock: Optional[StrictInt] = Field(None, description="The number of units of the product that you want to share as a reward.")
    attributes: Optional[RewardsCreateRequestBodyAttributes] = None
    __properties = ["name", "parameters", "metadata", "stock", "attributes"]

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
    def from_json(cls, json_str: str) -> RewardsCreateRequestBody:
        """Create an instance of RewardsCreateRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if parameters (nullable) is None
        # and __fields_set__ contains the field
        if self.parameters is None and "parameters" in self.__fields_set__:
            _dict['parameters'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if stock (nullable) is None
        # and __fields_set__ contains the field
        if self.stock is None and "stock" in self.__fields_set__:
            _dict['stock'] = None

        # set to None if attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.attributes is None and "attributes" in self.__fields_set__:
            _dict['attributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RewardsCreateRequestBody:
        """Create an instance of RewardsCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RewardsCreateRequestBody.parse_obj(obj)

        _obj = RewardsCreateRequestBody.parse_obj({
            "name": obj.get("name"),
            "parameters": RewardsCreateRequestBodyParameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None,
            "metadata": obj.get("metadata"),
            "stock": obj.get("stock"),
            "attributes": RewardsCreateRequestBodyAttributes.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None
        })
        return _obj


