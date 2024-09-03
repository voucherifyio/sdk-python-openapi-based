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


from typing import Optional
from pydantic import BaseModel
from voucherify_client.models.junction import Junction
from voucherify_client.models.qualifications_field_conditions import QualificationsFieldConditions
from voucherify_client.models.qualifications_option_filters_campaign_type import QualificationsOptionFiltersCampaignType
from voucherify_client.models.qualifications_option_filters_holder_role import QualificationsOptionFiltersHolderRole
from voucherify_client.models.qualifications_option_filters_resource_type import QualificationsOptionFiltersResourceType

class QualificationsOptionFilters(BaseModel):
    """
    A set of filters to return only a specific category or type of redeemable.  # noqa: E501
    """
    junction: Optional[Junction] = None
    category_id: Optional[QualificationsFieldConditions] = None
    campaign_id: Optional[QualificationsFieldConditions] = None
    campaign_type: Optional[QualificationsOptionFiltersCampaignType] = None
    resource_id: Optional[QualificationsFieldConditions] = None
    resource_type: Optional[QualificationsOptionFiltersResourceType] = None
    voucher_type: Optional[QualificationsFieldConditions] = None
    code: Optional[QualificationsFieldConditions] = None
    holder_role: Optional[QualificationsOptionFiltersHolderRole] = None
    __properties = ["junction", "category_id", "campaign_id", "campaign_type", "resource_id", "resource_type", "voucher_type", "code", "holder_role"]

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
    def from_json(cls, json_str: str) -> QualificationsOptionFilters:
        """Create an instance of QualificationsOptionFilters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of category_id
        if self.category_id:
            _dict['category_id'] = self.category_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_id
        if self.campaign_id:
            _dict['campaign_id'] = self.campaign_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_type
        if self.campaign_type:
            _dict['campaign_type'] = self.campaign_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_id
        if self.resource_id:
            _dict['resource_id'] = self.resource_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_type
        if self.resource_type:
            _dict['resource_type'] = self.resource_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher_type
        if self.voucher_type:
            _dict['voucher_type'] = self.voucher_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code
        if self.code:
            _dict['code'] = self.code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of holder_role
        if self.holder_role:
            _dict['holder_role'] = self.holder_role.to_dict()
        # set to None if campaign_type (nullable) is None
        # and __fields_set__ contains the field
        if self.campaign_type is None and "campaign_type" in self.__fields_set__:
            _dict['campaign_type'] = None

        # set to None if resource_type (nullable) is None
        # and __fields_set__ contains the field
        if self.resource_type is None and "resource_type" in self.__fields_set__:
            _dict['resource_type'] = None

        # set to None if holder_role (nullable) is None
        # and __fields_set__ contains the field
        if self.holder_role is None and "holder_role" in self.__fields_set__:
            _dict['holder_role'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QualificationsOptionFilters:
        """Create an instance of QualificationsOptionFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QualificationsOptionFilters.parse_obj(obj)

        _obj = QualificationsOptionFilters.parse_obj({
            "junction": obj.get("junction"),
            "category_id": QualificationsFieldConditions.from_dict(obj.get("category_id")) if obj.get("category_id") is not None else None,
            "campaign_id": QualificationsFieldConditions.from_dict(obj.get("campaign_id")) if obj.get("campaign_id") is not None else None,
            "campaign_type": QualificationsOptionFiltersCampaignType.from_dict(obj.get("campaign_type")) if obj.get("campaign_type") is not None else None,
            "resource_id": QualificationsFieldConditions.from_dict(obj.get("resource_id")) if obj.get("resource_id") is not None else None,
            "resource_type": QualificationsOptionFiltersResourceType.from_dict(obj.get("resource_type")) if obj.get("resource_type") is not None else None,
            "voucher_type": QualificationsFieldConditions.from_dict(obj.get("voucher_type")) if obj.get("voucher_type") is not None else None,
            "code": QualificationsFieldConditions.from_dict(obj.get("code")) if obj.get("code") is not None else None,
            "holder_role": QualificationsOptionFiltersHolderRole.from_dict(obj.get("holder_role")) if obj.get("holder_role") is not None else None
        })
        return _obj


