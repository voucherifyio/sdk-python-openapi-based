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



from pydantic import BaseModel, Field, StrictStr, validator

class RedeemPromotionTier(BaseModel):
    """
    Redeem a discount code.  # noqa: E501
    """
    object: StrictStr = Field(..., description="Redeemable object type.")
    id: StrictStr = Field(..., description="Promotion tier unique id, such as: promo_Mwy9XpA0TLctSGriM5kum0qp")
    __properties = ["object", "id"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('promotion_tier',):
            raise ValueError("must be one of enum values ('promotion_tier')")
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
    def from_json(cls, json_str: str) -> RedeemPromotionTier:
        """Create an instance of RedeemPromotionTier from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedeemPromotionTier:
        """Create an instance of RedeemPromotionTier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedeemPromotionTier.parse_obj(obj)

        _obj = RedeemPromotionTier.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'promotion_tier',
            "id": obj.get("id")
        })
        return _obj

