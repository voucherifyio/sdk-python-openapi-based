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





class ParameterOrderListCustomers(str, Enum):
    """
    ParameterOrderListCustomers
    """

    """
    allowed enum values
    """
    CREATED_AT = 'created_at'
    MINUS_CREATED_AT = '-created_at'
    UPDATED_AT = 'updated_at'
    MINUS_UPDATED_AT = '-updated_at'
    SOURCE_ID = 'source_id'
    MINUS_SOURCE_ID = '-source_id'

    @classmethod
    def from_json(cls, json_str: str) -> ParameterOrderListCustomers:
        """Create an instance of ParameterOrderListCustomers from a JSON string"""
        return ParameterOrderListCustomers(json.loads(json_str))

