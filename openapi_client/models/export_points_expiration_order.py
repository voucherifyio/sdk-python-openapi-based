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





class ExportPointsExpirationOrder(str, Enum):
    """
    ExportPointsExpirationOrder
    """

    """
    allowed enum values
    """
    ID = 'id'
    MINUS_ID = '-id'
    CAMPAIGN_ID = 'campaign_id'
    MINUS_CAMPAIGN_ID = '-campaign_id'
    VOUCHER_ID = 'voucher_id'
    MINUS_VOUCHER_ID = '-voucher_id'
    POINTS = 'points'
    MINUS_POINTS = '-points'
    STATUS = 'status'
    MINUS_STATUS = '-status'
    EXPIRES_AT = 'expires_at'
    MINUS_EXPIRES_AT = '-expires_at'

    @classmethod
    def from_json(cls, json_str: str) -> ExportPointsExpirationOrder:
        """Create an instance of ExportPointsExpirationOrder from a JSON string"""
        return ExportPointsExpirationOrder(json.loads(json_str))


