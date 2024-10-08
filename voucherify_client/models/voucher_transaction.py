# coding: utf-8

"""
    Voucherify API

    Voucherify promotion engine REST API. Please see https://docs.voucherify.io/docs for more details.

    The version of the OpenAPI document: v2018-08-01
    Contact: support@voucherify.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from voucherify_client.models.loyalty_card_transactions_type import LoyaltyCardTransactionsType
from voucherify_client.models.voucher_transaction_details import VoucherTransactionDetails

class VoucherTransaction(BaseModel):
    """
    VoucherTransaction
    """
    id: Optional[StrictStr] = Field(None, description="Unique transaction ID.")
    source_id: Optional[StrictStr] = Field(None, description="The merchant's transaction ID if it is different from the Voucherify transaction ID. It is really useful in case of an integration between multiple systems. It can be a transaction ID from a CRM system, database or 3rd-party service. In case of a redemption, this value is null.")
    voucher_id: Optional[StrictStr] = Field(None, description="Unique voucher ID.")
    campaign_id: Optional[StrictStr] = Field(None, description="Unqiue campaign ID of the voucher's parent campaign if it is part of campaign that generates bulk codes.")
    source: Optional[StrictStr] = Field(None, description="The channel through which the transaction took place, whether through the API or the the Dashboard. In case of a redemption, this value is null.")
    reason: Optional[StrictStr] = Field(None, description="Reason why the transaction occurred. In case of a redemption, this value is null.")
    type: LoyaltyCardTransactionsType = Field(...)
    details: Optional[VoucherTransactionDetails] = None
    related_transaction_id: Optional[StrictStr] = Field(None, description="The related transaction ID on the receiving card.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the transaction was created. The value is shown in the ISO 8601 format.")
    __properties = ["id", "source_id", "voucher_id", "campaign_id", "source", "reason", "type", "details", "related_transaction_id", "created_at"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> VoucherTransaction:
        """Create an instance of VoucherTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict['details'] = self.details.to_dict()
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

        # set to None if voucher_id (nullable) is None
        # and __fields_set__ contains the field
        if self.voucher_id is None and "voucher_id" in self.__fields_set__:
            _dict['voucher_id'] = None

        # set to None if campaign_id (nullable) is None
        # and __fields_set__ contains the field
        if self.campaign_id is None and "campaign_id" in self.__fields_set__:
            _dict['campaign_id'] = None

        # set to None if source (nullable) is None
        # and __fields_set__ contains the field
        if self.source is None and "source" in self.__fields_set__:
            _dict['source'] = None

        # set to None if reason (nullable) is None
        # and __fields_set__ contains the field
        if self.reason is None and "reason" in self.__fields_set__:
            _dict['reason'] = None

        # set to None if details (nullable) is None
        # and __fields_set__ contains the field
        if self.details is None and "details" in self.__fields_set__:
            _dict['details'] = None

        # set to None if related_transaction_id (nullable) is None
        # and __fields_set__ contains the field
        if self.related_transaction_id is None and "related_transaction_id" in self.__fields_set__:
            _dict['related_transaction_id'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VoucherTransaction:
        """Create an instance of VoucherTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VoucherTransaction.parse_obj(obj)

        _obj = VoucherTransaction.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "voucher_id": obj.get("voucher_id"),
            "campaign_id": obj.get("campaign_id"),
            "source": obj.get("source"),
            "reason": obj.get("reason"),
            "type": obj.get("type"),
            "details": VoucherTransactionDetails.from_dict(obj.get("details")) if obj.get("details") is not None else None,
            "related_transaction_id": obj.get("related_transaction_id"),
            "created_at": obj.get("created_at")
        })
        return _obj


