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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, conlist
from voucherify_client.models.export_customer_fields import ExportCustomerFields
from voucherify_client.models.export_customer_order import ExportCustomerOrder

class ExportCustomerBaseParameters(BaseModel):
    """
    List of available fields and filters that can be exported with an order along with the sorting order of the returned data.  # noqa: E501
    """
    order: Optional[ExportCustomerOrder] = None
    fields: Optional[conlist(ExportCustomerFields)] = Field(None, description="Array of strings containing the data in the export. These fields define the headers in the CSV file.")
    filters: Optional[Dict[str, Any]] = Field(None, description="Allowed additional properties must start with \"metadata.\" or \"address.\" or \"summary.\" or \"loyalty.\" or \"loyalty_tier.\" or \"loyalty_points.\" or \"system_metadata.\"")
    __properties = ["order", "fields", "filters"]

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
    def from_json(cls, json_str: str) -> ExportCustomerBaseParameters:
        """Create an instance of ExportCustomerBaseParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportCustomerBaseParameters:
        """Create an instance of ExportCustomerBaseParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExportCustomerBaseParameters.parse_obj(obj)

        _obj = ExportCustomerBaseParameters.parse_obj({
            "order": obj.get("order"),
            "fields": obj.get("fields"),
            "filters": obj.get("filters")
        })
        return _obj


