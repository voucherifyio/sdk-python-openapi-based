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
from openapi_client.models.redemption_reward_result_parameters_campaign import RedemptionRewardResultParametersCampaign
from openapi_client.models.redemption_reward_result_parameters_coin import RedemptionRewardResultParametersCoin
from openapi_client.models.redemption_reward_result_parameters_product import RedemptionRewardResultParametersProduct

class RedemptionRewardResultParameters(BaseModel):
    """
    These are parameters representing a material reward.  # noqa: E501
    """
    campaign: Optional[RedemptionRewardResultParametersCampaign] = None
    product: Optional[RedemptionRewardResultParametersProduct] = None
    coin: Optional[RedemptionRewardResultParametersCoin] = None
    __properties = ["campaign", "product", "coin"]

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
    def from_json(cls, json_str: str) -> RedemptionRewardResultParameters:
        """Create an instance of RedemptionRewardResultParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of coin
        if self.coin:
            _dict['coin'] = self.coin.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionRewardResultParameters:
        """Create an instance of RedemptionRewardResultParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionRewardResultParameters.parse_obj(obj)

        _obj = RedemptionRewardResultParameters.parse_obj({
            "campaign": RedemptionRewardResultParametersCampaign.from_dict(obj.get("campaign")) if obj.get("campaign") is not None else None,
            "product": RedemptionRewardResultParametersProduct.from_dict(obj.get("product")) if obj.get("product") is not None else None,
            "coin": RedemptionRewardResultParametersCoin.from_dict(obj.get("coin")) if obj.get("coin") is not None else None
        })
        return _obj

