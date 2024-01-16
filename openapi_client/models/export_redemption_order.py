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





class ExportRedemptionOrder(str, Enum):
    """
    ExportRedemptionOrder
    """

    """
    allowed enum values
    """
    ID = 'id'
    MINUS_ID = '-id'
    OBJECT = 'object'
    MINUS_OBJECT = '-object'
    DATE = 'date'
    MINUS_DATE = '-date'
    VOUCHER_CODE = 'voucher_code'
    MINUS_VOUCHER_CODE = '-voucher_code'
    CAMPAIGN = 'campaign'
    MINUS_CAMPAIGN = '-campaign'
    PROMOTION_TIER_ID = 'promotion_tier_id'
    MINUS_PROMOTION_TIER_ID = '-promotion_tier_id'
    CUSTOMER_ID = 'customer_id'
    MINUS_CUSTOMER_ID = '-customer_id'
    CUSTOMER_SOURCE_ID = 'customer_source_id'
    MINUS_CUSTOMER_SOURCE_ID = '-customer_source_id'
    CUSTOMER_NAME = 'customer_name'
    MINUS_CUSTOMER_NAME = '-customer_name'
    TRACKING_ID = 'tracking_id'
    MINUS_TRACKING_ID = '-tracking_id'
    ORDER_AMOUNT = 'order_amount'
    MINUS_ORDER_AMOUNT = '-order_amount'
    GIFT_AMOUNT = 'gift_amount'
    MINUS_GIFT_AMOUNT = '-gift_amount'
    LOYALTY_POINTS = 'loyalty_points'
    MINUS_LOYALTY_POINTS = '-loyalty_points'
    RESULT = 'result'
    MINUS_RESULT = '-result'
    FAILURE_CODE = 'failure_code'
    MINUS_FAILURE_CODE = '-failure_code'
    FAILURE_MESSAGE = 'failure_message'
    MINUS_FAILURE_MESSAGE = '-failure_message'
    METADATA = 'metadata'
    MINUS_METADATA = '-metadata'

    @classmethod
    def from_json(cls, json_str: str) -> ExportRedemptionOrder:
        """Create an instance of ExportRedemptionOrder from a JSON string"""
        return ExportRedemptionOrder(json.loads(json_str))


