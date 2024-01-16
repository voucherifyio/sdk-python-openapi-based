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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from openapi_client.models.list_publications_item_invalid import ListPublicationsItemInvalid
from openapi_client.models.list_publications_item_valid_multiple_vouchers import ListPublicationsItemValidMultipleVouchers
from openapi_client.models.list_publications_item_valid_single_voucher import ListPublicationsItemValidSingleVoucher
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

PUBLICATIONS_LIST_RESPONSE_BODY_PUBLICATIONS_ITEM_ONE_OF_SCHEMAS = ["ListPublicationsItemInvalid", "ListPublicationsItemValidMultipleVouchers", "ListPublicationsItemValidSingleVoucher"]

class PublicationsListResponseBodyPublicationsItem(BaseModel):
    """
    Response schema model for publishing vouchers to a specific customer.
    """
    # data type: ListPublicationsItemValidSingleVoucher
    oneof_schema_1_validator: Optional[ListPublicationsItemValidSingleVoucher] = None
    # data type: ListPublicationsItemValidMultipleVouchers
    oneof_schema_2_validator: Optional[ListPublicationsItemValidMultipleVouchers] = None
    # data type: ListPublicationsItemInvalid
    oneof_schema_3_validator: Optional[ListPublicationsItemInvalid] = None
    if TYPE_CHECKING:
        actual_instance: Union[ListPublicationsItemInvalid, ListPublicationsItemValidMultipleVouchers, ListPublicationsItemValidSingleVoucher]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(PUBLICATIONS_LIST_RESPONSE_BODY_PUBLICATIONS_ITEM_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = PublicationsListResponseBodyPublicationsItem.construct()
        error_messages = []
        match = 0
        # validate data type: ListPublicationsItemValidSingleVoucher
        if not isinstance(v, ListPublicationsItemValidSingleVoucher):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListPublicationsItemValidSingleVoucher`")
        else:
            match += 1
        # validate data type: ListPublicationsItemValidMultipleVouchers
        if not isinstance(v, ListPublicationsItemValidMultipleVouchers):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListPublicationsItemValidMultipleVouchers`")
        else:
            match += 1
        # validate data type: ListPublicationsItemInvalid
        if not isinstance(v, ListPublicationsItemInvalid):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListPublicationsItemInvalid`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in PublicationsListResponseBodyPublicationsItem with oneOf schemas: ListPublicationsItemInvalid, ListPublicationsItemValidMultipleVouchers, ListPublicationsItemValidSingleVoucher. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in PublicationsListResponseBodyPublicationsItem with oneOf schemas: ListPublicationsItemInvalid, ListPublicationsItemValidMultipleVouchers, ListPublicationsItemValidSingleVoucher. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> PublicationsListResponseBodyPublicationsItem:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> PublicationsListResponseBodyPublicationsItem:
        """Returns the object represented by the json string"""
        instance = PublicationsListResponseBodyPublicationsItem.construct()
        error_messages = []
        match = 0

        # deserialize data into ListPublicationsItemValidSingleVoucher
        try:
            instance.actual_instance = ListPublicationsItemValidSingleVoucher.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListPublicationsItemValidMultipleVouchers
        try:
            instance.actual_instance = ListPublicationsItemValidMultipleVouchers.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListPublicationsItemInvalid
        try:
            instance.actual_instance = ListPublicationsItemInvalid.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into PublicationsListResponseBodyPublicationsItem with oneOf schemas: ListPublicationsItemInvalid, ListPublicationsItemValidMultipleVouchers, ListPublicationsItemValidSingleVoucher. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into PublicationsListResponseBodyPublicationsItem with oneOf schemas: ListPublicationsItemInvalid, ListPublicationsItemValidMultipleVouchers, ListPublicationsItemValidSingleVoucher. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

