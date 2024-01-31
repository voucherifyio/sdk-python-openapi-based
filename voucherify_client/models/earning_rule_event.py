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





class EarningRuleEvent(str, Enum):
    """
    EarningRuleEvent
    """

    """
    allowed enum values
    """
    ORDER_DOT_PAID = 'order.paid'
    CUSTOMER_DOT_SEGMENT_DOT_ENTERED = 'customer.segment.entered'
    CUSTOM_EVENT = 'custom_event'
    CUSTOMER_DOT_LOYALTY_DOT_TIER_DOT_UPGRADED = 'customer.loyalty.tier.upgraded'
    CUSTOMER_DOT_LOYALTY_DOT_TIER_DOT_DOWNGRADED = 'customer.loyalty.tier.downgraded'
    CUSTOMER_DOT_LOYALTY_DOT_TIER_DOT_PROLONGED = 'customer.loyalty.tier.prolonged'
    CUSTOMER_DOT_LOYALTY_DOT_TIER_DOT_JOINED = 'customer.loyalty.tier.joined'
    CUSTOMER_DOT_LOYALTY_DOT_TIER_DOT_LEFT = 'customer.loyalty.tier.left'

    @classmethod
    def from_json(cls, json_str: str) -> EarningRuleEvent:
        """Create an instance of EarningRuleEvent from a JSON string"""
        return EarningRuleEvent(json.loads(json_str))


