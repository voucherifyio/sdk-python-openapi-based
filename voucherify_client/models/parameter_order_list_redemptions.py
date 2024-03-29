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





class ParameterOrderListRedemptions(str, Enum):
    """
    ParameterOrderListRedemptions
    """

    """
    allowed enum values
    """
    CREATED_AT = 'created_at'
    MINUS_CREATED_AT = '-created_at'
    ID = 'id'
    MINUS_ID = '-id'
    VOUCHER_CODE = 'voucher_code'
    MINUS_VOUCHER_CODE = '-voucher_code'
    TRACKING_ID = 'tracking_id'
    MINUS_TRACKING_ID = '-tracking_id'
    CUSTOMER_ID = 'customer_id'
    MINUS_CUSTOMER_ID = '-customer_id'

    @classmethod
    def from_json(cls, json_str: str) -> ParameterOrderListRedemptions:
        """Create an instance of ParameterOrderListRedemptions from a JSON string"""
        return ParameterOrderListRedemptions(json.loads(json_str))


