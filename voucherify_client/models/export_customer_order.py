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





class ExportCustomerOrder(str, Enum):
    """
    ExportCustomerOrder
    """

    """
    allowed enum values
    """
    MINUS_NAME = '-name'
    NAME = 'name'
    MINUS_ID = '-id'
    ID = 'id'
    MINUS_EMAIL = '-email'
    EMAIL = 'email'
    MINUS_SOURCE_ID = '-source_id'
    SOURCE_ID = 'source_id'
    MINUS_CREATED_AT = '-created_at'
    CREATED_AT = 'created_at'
    MINUS_UPDATED_AT = '-updated_at'
    UPDATED_AT = 'updated_at'

    @classmethod
    def from_json(cls, json_str: str) -> ExportCustomerOrder:
        """Create an instance of ExportCustomerOrder from a JSON string"""
        return ExportCustomerOrder(json.loads(json_str))


