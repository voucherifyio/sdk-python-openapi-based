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
    NAME = 'name'
    MINUS_NAME = '-name'
    ID = 'id'
    MINUS_ID = '-id'
    DESCRIPTION = 'description'
    MINUS_DESCRIPTION = '-description'
    EMAIL = 'email'
    MINUS_EMAIL = '-email'
    SOURCE_ID = 'source_id'
    MINUS_SOURCE_ID = '-source_id'
    CREATED_AT = 'created_at'
    MINUS_CREATED_AT = '-created_at'
    ADDRESS_CITY = 'address_city'
    MINUS_ADDRESS_CITY = '-address_city'
    ADDRESS_STATE = 'address_state'
    MINUS_ADDRESS_STATE = '-address_state'
    ADDRESS_LINE_1 = 'address_line_1'
    MINUS_ADDRESS_LINE_1 = '-address_line_1'
    ADDRESS_LINE_2 = 'address_line_2'
    MINUS_ADDRESS_LINE_2 = '-address_line_2'
    ADDRESS_COUNTRY = 'address_country'
    MINUS_ADDRESS_COUNTRY = '-address_country'
    ADDRESS_POSTAL_CODE = 'address_postal_code'
    MINUS_ADDRESS_POSTAL_CODE = '-address_postal_code'
    REDEMPTIONS_TOTAL_REDEEMED = 'redemptions_total_redeemed'
    MINUS_REDEMPTIONS_TOTAL_REDEEMED = '-redemptions_total_redeemed'
    REDEMPTIONS_TOTAL_FAILED = 'redemptions_total_failed'
    MINUS_REDEMPTIONS_TOTAL_FAILED = '-redemptions_total_failed'
    REDEMPTIONS_TOTAL_SUCCEEDED = 'redemptions_total_succeeded'
    MINUS_REDEMPTIONS_TOTAL_SUCCEEDED = '-redemptions_total_succeeded'
    REDEMPTIONS_TOTAL_ROLLED_BACK = 'redemptions_total_rolled_back'
    MINUS_REDEMPTIONS_TOTAL_ROLLED_BACK = '-redemptions_total_rolled_back'
    REDEMPTIONS_TOTAL_ROLLBACK_FAILED = 'redemptions_total_rollback_failed'
    MINUS_REDEMPTIONS_TOTAL_ROLLBACK_FAILED = '-redemptions_total_rollback_failed'
    REDEMPTIONS_TOTAL_ROLLBACK_SUCCEEDED = 'redemptions_total_rollback_succeeded'
    MINUS_REDEMPTIONS_TOTAL_ROLLBACK_SUCCEEDED = '-redemptions_total_rollback_succeeded'
    ORDERS_TOTAL_AMOUNT = 'orders_total_amount'
    MINUS_ORDERS_TOTAL_AMOUNT = '-orders_total_amount'
    ORDERS_TOTAL_COUNT = 'orders_total_count'
    MINUS_ORDERS_TOTAL_COUNT = '-orders_total_count'
    ORDERS_AVERAGE_AMOUNT = 'orders_average_amount'
    MINUS_ORDERS_AVERAGE_AMOUNT = '-orders_average_amount'
    ORDERS_LAST_ORDER_AMOUNT = 'orders_last_order_amount'
    MINUS_ORDERS_LAST_ORDER_AMOUNT = '-orders_last_order_amount'
    ORDERS_LAST_ORDER_DATE = 'orders_last_order_date'
    MINUS_ORDERS_LAST_ORDER_DATE = '-orders_last_order_date'
    LOYALTY_POINTS = 'loyalty_points'
    MINUS_LOYALTY_POINTS = '-loyalty_points'
    LOYALTY_REFERRED_CUSTOMERS = 'loyalty_referred_customers'
    MINUS_LOYALTY_REFERRED_CUSTOMERS = '-loyalty_referred_customers'
    UPDATED_AT = 'updated_at'
    MINUS_UPDATED_AT = '-updated_at'
    PHONE = 'phone'
    MINUS_PHONE = '-phone'
    BIRTHDAY = 'birthday'
    MINUS_BIRTHDAY = '-birthday'
    METADATA = 'metadata'
    MINUS_METADATA = '-metadata'
    BIRTHDATE = 'birthdate'
    MINUS_BIRTHDATE = '-birthdate'

    @classmethod
    def from_json(cls, json_str: str) -> ExportCustomerOrder:
        """Create an instance of ExportCustomerOrder from a JSON string"""
        return ExportCustomerOrder(json.loads(json_str))

