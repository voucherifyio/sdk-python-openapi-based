# coding: utf-8

"""
    Voucherify API

    Voucherify promotion engine REST API. Please see https://docs.voucherify.io/docs for more details.

    The version of the OpenAPI document: v2018-08-01
    Contact: support@voucherify.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ParameterCampaignType(str, Enum):
    """
    ParameterCampaignType
    """

    """
    allowed enum values
    """
    PROMOTION = 'PROMOTION'
    GIFT_VOUCHERS = 'GIFT_VOUCHERS'
    REFERRAL_PROGRAM = 'REFERRAL_PROGRAM'
    DISCOUNT_COUPONS = 'DISCOUNT_COUPONS'
    LOYALTY_PROGRAM = 'LOYALTY_PROGRAM'
    LUCKY_DRAW = 'LUCKY_DRAW'

    @classmethod
    def from_json(cls, json_str: str) -> ParameterCampaignType:
        """Create an instance of ParameterCampaignType from a JSON string"""
        return ParameterCampaignType(json.loads(json_str))


