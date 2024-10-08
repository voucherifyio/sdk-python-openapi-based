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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from voucherify_client.models.customer_redeemable import CustomerRedeemable

class CustomersRedeemablesListResponseBody(BaseModel):
    """
    Response body schema for **GET** `v1/customers/{customerId}/redeemables`.  # noqa: E501
    """
    object: Optional[StrictStr] = Field('list', description="The type of the object represented by JSON. This object stores information about customer redeemables.")
    data_ref: Optional[StrictStr] = Field('data', description="Identifies the name of the JSON property that contains the array of redeemables.")
    data: Optional[conlist(CustomerRedeemable)] = Field(None, description="A dictionary that contains an array of redeemables.")
    total: Optional[StrictInt] = Field(None, description="Total number of results returned.")
    has_more: Optional[StrictBool] = Field(None, description="As query results are always limited (by the limit parameter), the `has_more` flag indicates if there are more records for given filter parameters. This lets you know if you can run another request with a `starting_after_id` query or a different limit to get more records returned in the results.")
    more_starting_after: Optional[StrictStr] = Field(None, description="Returns an ID that can be used to return another page of results. Use the ID in the `starting_after_id` query parameter to display another page of the results occuring after the field with that ID.")
    __properties = ["object", "data_ref", "data", "total", "has_more", "more_starting_after"]

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
    def from_json(cls, json_str: str) -> CustomersRedeemablesListResponseBody:
        """Create an instance of CustomersRedeemablesListResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if data_ref (nullable) is None
        # and __fields_set__ contains the field
        if self.data_ref is None and "data_ref" in self.__fields_set__:
            _dict['data_ref'] = None

        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        # set to None if has_more (nullable) is None
        # and __fields_set__ contains the field
        if self.has_more is None and "has_more" in self.__fields_set__:
            _dict['has_more'] = None

        # set to None if more_starting_after (nullable) is None
        # and __fields_set__ contains the field
        if self.more_starting_after is None and "more_starting_after" in self.__fields_set__:
            _dict['more_starting_after'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomersRedeemablesListResponseBody:
        """Create an instance of CustomersRedeemablesListResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomersRedeemablesListResponseBody.parse_obj(obj)

        _obj = CustomersRedeemablesListResponseBody.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'data',
            "data": [CustomerRedeemable.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "total": obj.get("total"),
            "has_more": obj.get("has_more"),
            "more_starting_after": obj.get("more_starting_after")
        })
        return _obj


