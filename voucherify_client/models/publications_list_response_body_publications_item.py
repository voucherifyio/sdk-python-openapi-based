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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from voucherify_client.models.customer_with_summary_loyalty_referrals import CustomerWithSummaryLoyaltyReferrals
from voucherify_client.models.list_publications_item_voucher import ListPublicationsItemVoucher
from voucherify_client.models.publications_list_response_body_publications_item_metadata import PublicationsListResponseBodyPublicationsItemMetadata

class PublicationsListResponseBodyPublicationsItem(BaseModel):
    """
    PublicationsListResponseBodyPublicationsItem
    """
    id: Optional[StrictStr] = Field(None, description="Unique publication ID, assigned by Voucherify.")
    object: Optional[StrictStr] = Field('publication', description="The type of the object represented by the JSON. This object stores information about the `publication`.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the publication was created. The value is shown in the ISO 8601 format.")
    customer_id: Optional[StrictStr] = Field(None, description="Unique customer ID of the customer receiving the publication.")
    tracking_id: Optional[StrictStr] = Field(None, description="Customer's `source_id`.")
    metadata: Optional[PublicationsListResponseBodyPublicationsItemMetadata] = None
    channel: Optional[StrictStr] = Field(None, description="How the publication was originated. It can be your own custom channel or an example value provided here.")
    source_id: Optional[StrictStr] = Field(None, description="The merchant's publication ID if it is different from the Voucherify publication ID. It's an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. ")
    customer: Optional[CustomerWithSummaryLoyaltyReferrals] = None
    vouchers: Optional[conlist(StrictStr)] = Field(None, description="Contains the voucher IDs that was assigned by Voucherify. and Contains the unique voucher codes that was assigned by Voucherify.")
    vouchers_id: Optional[conlist(StrictStr)] = Field(None, description="Contains the unique internal voucher IDs that was assigned by Voucherify.")
    result: Optional[StrictStr] = None
    voucher: Optional[ListPublicationsItemVoucher] = None
    failure_code: Optional[StrictStr] = Field(None, description="Generic reason as to why the create publication operation failed.")
    failure_message: Optional[StrictStr] = Field(None, description="This parameter will provide more expanded reason as to why the create publication operation failed.")
    __properties = ["id", "object", "created_at", "customer_id", "tracking_id", "metadata", "channel", "source_id", "customer", "vouchers", "vouchers_id", "result", "voucher", "failure_code", "failure_message"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('publication',):
            raise ValueError("must be one of enum values ('publication')")
        return value

    @validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUCCESS', 'FAILURE',):
            raise ValueError("must be one of enum values ('SUCCESS', 'FAILURE')")
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
    def from_json(cls, json_str: str) -> PublicationsListResponseBodyPublicationsItem:
        """Create an instance of PublicationsListResponseBodyPublicationsItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if customer_id (nullable) is None
        # and __fields_set__ contains the field
        if self.customer_id is None and "customer_id" in self.__fields_set__:
            _dict['customer_id'] = None

        # set to None if tracking_id (nullable) is None
        # and __fields_set__ contains the field
        if self.tracking_id is None and "tracking_id" in self.__fields_set__:
            _dict['tracking_id'] = None

        # set to None if channel (nullable) is None
        # and __fields_set__ contains the field
        if self.channel is None and "channel" in self.__fields_set__:
            _dict['channel'] = None

        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

        # set to None if vouchers_id (nullable) is None
        # and __fields_set__ contains the field
        if self.vouchers_id is None and "vouchers_id" in self.__fields_set__:
            _dict['vouchers_id'] = None

        # set to None if failure_code (nullable) is None
        # and __fields_set__ contains the field
        if self.failure_code is None and "failure_code" in self.__fields_set__:
            _dict['failure_code'] = None

        # set to None if failure_message (nullable) is None
        # and __fields_set__ contains the field
        if self.failure_message is None and "failure_message" in self.__fields_set__:
            _dict['failure_message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PublicationsListResponseBodyPublicationsItem:
        """Create an instance of PublicationsListResponseBodyPublicationsItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PublicationsListResponseBodyPublicationsItem.parse_obj(obj)

        _obj = PublicationsListResponseBodyPublicationsItem.parse_obj({
            "id": obj.get("id"),
            "object": obj.get("object") if obj.get("object") is not None else 'publication',
            "created_at": obj.get("created_at"),
            "customer_id": obj.get("customer_id"),
            "tracking_id": obj.get("tracking_id"),
            "metadata": PublicationsListResponseBodyPublicationsItemMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "channel": obj.get("channel"),
            "source_id": obj.get("source_id"),
            "customer": CustomerWithSummaryLoyaltyReferrals.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "vouchers": obj.get("vouchers"),
            "vouchers_id": obj.get("vouchers_id"),
            "result": obj.get("result"),
            "voucher": ListPublicationsItemVoucher.from_dict(obj.get("voucher")) if obj.get("voucher") is not None else None,
            "failure_code": obj.get("failure_code"),
            "failure_message": obj.get("failure_message")
        })
        return _obj


