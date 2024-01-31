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
from voucherify_client.models.applicable_to_result_list import ApplicableToResultList
from voucherify_client.models.category import Category
from voucherify_client.models.inapplicable_to_result_list import InapplicableToResultList
from voucherify_client.models.order_calculated import OrderCalculated
from voucherify_client.models.redeemable_result import RedeemableResult
from voucherify_client.models.validation_rules_assignments_list import ValidationRulesAssignmentsList

class QualificationsRedeemableBase(BaseModel):
    """
    Data of single redeemable which was properly qualified.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Id of the redeemable.")
    object: Optional[StrictStr] = Field(None, description="Object type of the redeemable.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the object was created in ISO 8601 format.")
    result: Optional[RedeemableResult] = None
    order: Optional[OrderCalculated] = None
    validation_rule_id: Optional[StrictStr] = Field(None, description="A unique validation rule identifier assigned by the Voucherify API. The validation rule is verified before points are added to the balance.")
    applicable_to: Optional[ApplicableToResultList] = None
    inapplicable_to: Optional[InapplicableToResultList] = None
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the product. A set of key/value pairs that you can attach to a product object. It can be useful for storing additional information about the product in a structured format.")
    categories: Optional[conlist(Category)] = Field(None, description="List of category information.")
    banner: Optional[StrictStr] = Field(None, description="Name of the earning rule. This is displayed as a header for the earning rule in the Dashboard.")
    name: Optional[StrictStr] = Field(None, description="Name of the redeemable.")
    campaign_name: Optional[StrictStr] = Field(None, description="Name of the campaign associated to the redeemable. This field is available only if object is not `campaign`")
    campaign_id: Optional[StrictStr] = Field(None, description="Id of the campaign associated to the redeemable. This field is available only if object is not `campaign`")
    validation_rules_assignments: Optional[ValidationRulesAssignmentsList] = None
    __properties = ["id", "object", "created_at", "result", "order", "validation_rule_id", "applicable_to", "inapplicable_to", "metadata", "categories", "banner", "name", "campaign_name", "campaign_id", "validation_rules_assignments"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('campaign', 'promotion_tier', 'promotion_stack', 'voucher',):
            raise ValueError("must be one of enum values ('campaign', 'promotion_tier', 'promotion_stack', 'voucher')")
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
    def from_json(cls, json_str: str) -> QualificationsRedeemableBase:
        """Create an instance of QualificationsRedeemableBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of applicable_to
        if self.applicable_to:
            _dict['applicable_to'] = self.applicable_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of inapplicable_to
        if self.inapplicable_to:
            _dict['inapplicable_to'] = self.inapplicable_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['categories'] = _items
        # override the default output from pydantic by calling `to_dict()` of validation_rules_assignments
        if self.validation_rules_assignments:
            _dict['validation_rules_assignments'] = self.validation_rules_assignments.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QualificationsRedeemableBase:
        """Create an instance of QualificationsRedeemableBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QualificationsRedeemableBase.parse_obj(obj)

        _obj = QualificationsRedeemableBase.parse_obj({
            "id": obj.get("id"),
            "object": obj.get("object"),
            "created_at": obj.get("created_at"),
            "result": RedeemableResult.from_dict(obj.get("result")) if obj.get("result") is not None else None,
            "order": OrderCalculated.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "validation_rule_id": obj.get("validation_rule_id"),
            "applicable_to": ApplicableToResultList.from_dict(obj.get("applicable_to")) if obj.get("applicable_to") is not None else None,
            "inapplicable_to": InapplicableToResultList.from_dict(obj.get("inapplicable_to")) if obj.get("inapplicable_to") is not None else None,
            "metadata": obj.get("metadata"),
            "categories": [Category.from_dict(_item) for _item in obj.get("categories")] if obj.get("categories") is not None else None,
            "banner": obj.get("banner"),
            "name": obj.get("name"),
            "campaign_name": obj.get("campaign_name"),
            "campaign_id": obj.get("campaign_id"),
            "validation_rules_assignments": ValidationRulesAssignmentsList.from_dict(obj.get("validation_rules_assignments")) if obj.get("validation_rules_assignments") is not None else None
        })
        return _obj


