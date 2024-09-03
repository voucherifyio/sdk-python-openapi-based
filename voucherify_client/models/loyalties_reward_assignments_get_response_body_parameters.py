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
from pydantic import BaseModel
from voucherify_client.models.loyalties_reward_assignments_get_response_body_parameters_loyalty import LoyaltiesRewardAssignmentsGetResponseBodyParametersLoyalty

class LoyaltiesRewardAssignmentsGetResponseBodyParameters(BaseModel):
    """
    Defines the cost of the reward.  # noqa: E501
    """
    loyalty: Optional[LoyaltiesRewardAssignmentsGetResponseBodyParametersLoyalty] = None
    __properties = ["loyalty"]

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
    def from_json(cls, json_str: str) -> LoyaltiesRewardAssignmentsGetResponseBodyParameters:
        """Create an instance of LoyaltiesRewardAssignmentsGetResponseBodyParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of loyalty
        if self.loyalty:
            _dict['loyalty'] = self.loyalty.to_dict()
        # set to None if loyalty (nullable) is None
        # and __fields_set__ contains the field
        if self.loyalty is None and "loyalty" in self.__fields_set__:
            _dict['loyalty'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesRewardAssignmentsGetResponseBodyParameters:
        """Create an instance of LoyaltiesRewardAssignmentsGetResponseBodyParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesRewardAssignmentsGetResponseBodyParameters.parse_obj(obj)

        _obj = LoyaltiesRewardAssignmentsGetResponseBodyParameters.parse_obj({
            "loyalty": LoyaltiesRewardAssignmentsGetResponseBodyParametersLoyalty.from_dict(obj.get("loyalty")) if obj.get("loyalty") is not None else None
        })
        return _obj


