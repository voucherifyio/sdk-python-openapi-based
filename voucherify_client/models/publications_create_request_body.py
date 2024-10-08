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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from voucherify_client.models.create_publication_campaign import CreatePublicationCampaign
from voucherify_client.models.publications_create_request_body_customer import PublicationsCreateRequestBodyCustomer

class PublicationsCreateRequestBody(BaseModel):
    """
    PublicationsCreateRequestBody
    """
    voucher: Optional[StrictStr] = Field(None, description="Code of the voucher being published.")
    source_id: Optional[StrictStr] = Field(None, description="The merchant's publication ID if it is different from the Voucherify publication ID. It's an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. If `source_id` is provided only 1 voucher can be published per request.")
    customer: Optional[PublicationsCreateRequestBodyCustomer] = None
    metadata: Optional[Dict[str, Any]] = None
    channel: Optional[StrictStr] = Field(None, description="Specify the distribution channel.")
    campaign: Optional[CreatePublicationCampaign] = None
    __properties = ["voucher", "source_id", "customer", "metadata", "channel", "campaign"]

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
    def from_json(cls, json_str: str) -> PublicationsCreateRequestBody:
        """Create an instance of PublicationsCreateRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        # set to None if voucher (nullable) is None
        # and __fields_set__ contains the field
        if self.voucher is None and "voucher" in self.__fields_set__:
            _dict['voucher'] = None

        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

        # set to None if customer (nullable) is None
        # and __fields_set__ contains the field
        if self.customer is None and "customer" in self.__fields_set__:
            _dict['customer'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if channel (nullable) is None
        # and __fields_set__ contains the field
        if self.channel is None and "channel" in self.__fields_set__:
            _dict['channel'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PublicationsCreateRequestBody:
        """Create an instance of PublicationsCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PublicationsCreateRequestBody.parse_obj(obj)

        _obj = PublicationsCreateRequestBody.parse_obj({
            "voucher": obj.get("voucher"),
            "source_id": obj.get("source_id"),
            "customer": PublicationsCreateRequestBodyCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "metadata": obj.get("metadata"),
            "channel": obj.get("channel"),
            "campaign": CreatePublicationCampaign.from_dict(obj.get("campaign")) if obj.get("campaign") is not None else None
        })
        return _obj


