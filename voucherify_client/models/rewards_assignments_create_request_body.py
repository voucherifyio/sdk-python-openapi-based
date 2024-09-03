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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from voucherify_client.models.rewards_assignments_create_request_body_parameters import RewardsAssignmentsCreateRequestBodyParameters

class RewardsAssignmentsCreateRequestBody(BaseModel):
    """
    RewardsAssignmentsCreateRequestBody
    """
    campaign: Optional[StrictStr] = Field(None, description="The campaign ID of the campaign to which the reward is to be assigned.")
    parameters: Optional[RewardsAssignmentsCreateRequestBodyParameters] = None
    validation_rules: Optional[conlist(StrictStr)] = None
    __properties = ["campaign", "parameters", "validation_rules"]

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
    def from_json(cls, json_str: str) -> RewardsAssignmentsCreateRequestBody:
        """Create an instance of RewardsAssignmentsCreateRequestBody from a JSON string"""
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
        # set to None if campaign (nullable) is None
        # and __fields_set__ contains the field
        if self.campaign is None and "campaign" in self.__fields_set__:
            _dict['campaign'] = None

        # set to None if parameters (nullable) is None
        # and __fields_set__ contains the field
        if self.parameters is None and "parameters" in self.__fields_set__:
            _dict['parameters'] = None

        # set to None if validation_rules (nullable) is None
        # and __fields_set__ contains the field
        if self.validation_rules is None and "validation_rules" in self.__fields_set__:
            _dict['validation_rules'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RewardsAssignmentsCreateRequestBody:
        """Create an instance of RewardsAssignmentsCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RewardsAssignmentsCreateRequestBody.parse_obj(obj)

        _obj = RewardsAssignmentsCreateRequestBody.parse_obj({
            "campaign": obj.get("campaign"),
            "parameters": RewardsAssignmentsCreateRequestBodyParameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None,
            "validation_rules": obj.get("validation_rules")
        })
        return _obj


