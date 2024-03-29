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
from voucherify_client.models.reward_assignments_create_digital_or_material_reward_request_body_parameters import RewardAssignmentsCreateDigitalOrMaterialRewardRequestBodyParameters

class RewardAssignmentsCreateDigitalOrMaterialRewardRequestBody(BaseModel):
    """
    Request body schema for **POST** `/rewards/{rewardID}/assignments`.  # noqa: E501
    """
    campaign: StrictStr = Field(..., description="The campaign ID of the campaign to which the reward is to be assigned.")
    parameters: RewardAssignmentsCreateDigitalOrMaterialRewardRequestBodyParameters = Field(...)
    __properties = ["campaign", "parameters"]

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
    def from_json(cls, json_str: str) -> RewardAssignmentsCreateDigitalOrMaterialRewardRequestBody:
        """Create an instance of RewardAssignmentsCreateDigitalOrMaterialRewardRequestBody from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RewardAssignmentsCreateDigitalOrMaterialRewardRequestBody:
        """Create an instance of RewardAssignmentsCreateDigitalOrMaterialRewardRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RewardAssignmentsCreateDigitalOrMaterialRewardRequestBody.parse_obj(obj)

        _obj = RewardAssignmentsCreateDigitalOrMaterialRewardRequestBody.parse_obj({
            "campaign": obj.get("campaign"),
            "parameters": RewardAssignmentsCreateDigitalOrMaterialRewardRequestBodyParameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None
        })
        return _obj


