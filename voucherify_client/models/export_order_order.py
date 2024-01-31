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





class ExportOrderOrder(str, Enum):
    """
    ExportOrderOrder
    """

    """
    allowed enum values
    """
    MINUS_CREATED_AT = '-created_at'
    CREATED_AT = 'created_at'
    MINUS_UPDATED_AT = '-updated_at'
    UPDATED_AT = 'updated_at'
    MINUS_STATUS = '-status'
    STATUS = 'status'

    @classmethod
    def from_json(cls, json_str: str) -> ExportOrderOrder:
        """Create an instance of ExportOrderOrder from a JSON string"""
        return ExportOrderOrder(json.loads(json_str))


