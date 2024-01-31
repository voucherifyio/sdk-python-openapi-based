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





class ExportPublicationFields(str, Enum):
    """
    ExportPublicationFields
    """

    """
    allowed enum values
    """
    VOUCHER_CODE = 'voucher_code'
    CUSTOMER_ID = 'customer_id'
    CUSTOMER_SOURCE_ID = 'customer_source_id'
    DATE = 'date'
    CHANNEL = 'channel'
    CAMPAIGN = 'campaign'
    IS_WINNER = 'is_winner'
    METADATA = 'metadata'

    @classmethod
    def from_json(cls, json_str: str) -> ExportPublicationFields:
        """Create an instance of ExportPublicationFields from a JSON string"""
        return ExportPublicationFields(json.loads(json_str))


