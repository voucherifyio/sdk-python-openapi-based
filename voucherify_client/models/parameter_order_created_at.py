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





class ParameterOrderCreatedAt(str, Enum):
    """
    ParameterOrderCreatedAt
    """

    """
    allowed enum values
    """
    CREATED_AT = 'created_at'
    MINUS_CREATED_AT = '-created_at'

    @classmethod
    def from_json(cls, json_str: str) -> ParameterOrderCreatedAt:
        """Create an instance of ParameterOrderCreatedAt from a JSON string"""
        return ParameterOrderCreatedAt(json.loads(json_str))


