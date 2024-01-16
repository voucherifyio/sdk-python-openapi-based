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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from openapi_client.models.customer_with_summary_loyalty_referrals import CustomerWithSummaryLoyaltyReferrals

class ListPublicationsItemBase(BaseModel):
    """
    ListPublicationsItemBase
    """
    id: StrictStr = Field(..., description="Unique publication ID, assigned by Voucherify.")
    object: StrictStr = Field(..., description="The type of object represented by the JSON. This object stores information about the `publication`.")
    created_at: datetime = Field(..., description="Timestamp representing the date and time when the publication was created in ISO 8601 format.")
    customer_id: StrictStr = Field(..., description="Unique customer ID of the customer receiving the publication.")
    tracking_id: Optional[StrictStr] = Field(None, description="Customer's `source_id`.")
    metadata: Dict[str, Any] = Field(..., description="The metadata object stores all custom attributes assigned to the publication. A set of key/value pairs that you can attach to a publication object. It can be useful for storing additional information about the publication in a structured format.")
    channel: StrictStr = Field(..., description="How the publication was originated. It can be your own custom channel or an example value provided here.")
    source_id: Optional[StrictStr] = Field(None, description="The merchant’s publication ID if it is different from the Voucherify publication ID. It's an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. ")
    customer: CustomerWithSummaryLoyaltyReferrals = Field(...)
    vouchers_id: conlist(StrictStr) = Field(..., description="Contains the unique internal voucher ID that was assigned by Voucherify.")
    __properties = ["id", "object", "created_at", "customer_id", "tracking_id", "metadata", "channel", "source_id", "customer", "vouchers_id"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('publication',):
            raise ValueError("must be one of enum values ('publication')")
        return value

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
    def from_json(cls, json_str: str) -> ListPublicationsItemBase:
        """Create an instance of ListPublicationsItemBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListPublicationsItemBase:
        """Create an instance of ListPublicationsItemBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListPublicationsItemBase.parse_obj(obj)

        _obj = ListPublicationsItemBase.parse_obj({
            "id": obj.get("id"),
            "object": obj.get("object") if obj.get("object") is not None else 'publication',
            "created_at": obj.get("created_at"),
            "customer_id": obj.get("customer_id"),
            "tracking_id": obj.get("tracking_id"),
            "metadata": obj.get("metadata"),
            "channel": obj.get("channel"),
            "source_id": obj.get("source_id"),
            "customer": CustomerWithSummaryLoyaltyReferrals.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "vouchers_id": obj.get("vouchers_id")
        })
        return _obj


