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
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from voucherify_client.models.loyalties_points_expiration_export_create_response_body_parameters_filters import LoyaltiesPointsExpirationExportCreateResponseBodyParametersFilters

class LoyaltiesPointsExpirationExportCreateResponseBodyParameters(BaseModel):
    """
    List of fields and filters that were passed in the request body to create the export.  # noqa: E501
    """
    order: Optional[StrictStr] = Field(None, description="How the export is filtered, where the dash `-` preceding a sorting option means sorting in a descending order.")
    fields: Optional[conlist(StrictStr)] = Field(None, description="Array of strings containing the data that was exported. These fields define the headers in the CSV file.    The array can be a combination of any of the following available fields:    | **Field** | **Definition** | **Example Export** | |:---|:---|:---| | id | Loyalty points bucket ID. | lopb_Wl1o3EjJIHSNjvO5BDLy4z1n | | campaign_id | Campaign ID of the parent loyalty campaign. | camp_7s3uXI44aKfIk5IhmeOPr6ic | | voucher_id | Voucher ID of the parent loyalty card. | v_YLn0WVWXSXbUfDvxgrgUbtfJ3SQIY655 | | status | Status of the loyalty points bucket. | `ACTIVE` or `INACTIVE` | | expires_at | Timestamp in ISO 8601 format representing the date when the points expire. | 2022-06-30 | | points | Number of points. | 1000 |")
    filters: Optional[LoyaltiesPointsExpirationExportCreateResponseBodyParametersFilters] = None
    __properties = ["order", "fields", "filters"]

    @validator('order')
    def order_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('expires_at', '-expires_at',):
            raise ValueError("must be one of enum values ('expires_at', '-expires_at')")
        return value

    @validator('fields')
    def fields_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('id', 'campaign_id', 'voucher_id', 'points', 'status', 'expires_at',):
                raise ValueError("each list item must be one of ('id', 'campaign_id', 'voucher_id', 'points', 'status', 'expires_at')")
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
    def from_json(cls, json_str: str) -> LoyaltiesPointsExpirationExportCreateResponseBodyParameters:
        """Create an instance of LoyaltiesPointsExpirationExportCreateResponseBodyParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # set to None if order (nullable) is None
        # and __fields_set__ contains the field
        if self.order is None and "order" in self.__fields_set__:
            _dict['order'] = None

        # set to None if fields (nullable) is None
        # and __fields_set__ contains the field
        if self.fields is None and "fields" in self.__fields_set__:
            _dict['fields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesPointsExpirationExportCreateResponseBodyParameters:
        """Create an instance of LoyaltiesPointsExpirationExportCreateResponseBodyParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesPointsExpirationExportCreateResponseBodyParameters.parse_obj(obj)

        _obj = LoyaltiesPointsExpirationExportCreateResponseBodyParameters.parse_obj({
            "order": obj.get("order"),
            "fields": obj.get("fields"),
            "filters": LoyaltiesPointsExpirationExportCreateResponseBodyParametersFilters.from_dict(obj.get("filters")) if obj.get("filters") is not None else None
        })
        return _obj


