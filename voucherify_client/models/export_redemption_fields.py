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





class ExportRedemptionFields(str, Enum):
    """
    ExportRedemptionFields
    """

    """
    allowed enum values
    """
    ID = 'id'
    OBJECT = 'object'
    DATE = 'date'
    VOUCHER_CODE = 'voucher_code'
    CAMPAIGN = 'campaign'
    PROMOTION_TIER_ID = 'promotion_tier_id'
    CUSTOMER_ID = 'customer_id'
    CUSTOMER_SOURCE_ID = 'customer_source_id'
    CUSTOMER_NAME = 'customer_name'
    TRACKING_ID = 'tracking_id'
    ORDER_AMOUNT = 'order_amount'
    GIFT_AMOUNT = 'gift_amount'
    LOYALTY_POINTS = 'loyalty_points'
    RESULT = 'result'
    FAILURE_CODE = 'failure_code'
    FAILURE_MESSAGE = 'failure_message'
    METADATA = 'metadata'

    @classmethod
    def from_json(cls, json_str: str) -> ExportRedemptionFields:
        """Create an instance of ExportRedemptionFields from a JSON string"""
        return ExportRedemptionFields(json.loads(json_str))

