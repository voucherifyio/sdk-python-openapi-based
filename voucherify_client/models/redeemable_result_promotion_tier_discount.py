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
from voucherify_client.models.discount_amount import DiscountAmount
from voucherify_client.models.discount_fixed import DiscountFixed
from voucherify_client.models.discount_percent import DiscountPercent
from voucherify_client.models.discount_unit import DiscountUnit
from voucherify_client.models.discount_unit_multiple import DiscountUnitMultiple
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

REDEEMABLE_RESULT_PROMOTION_TIER_DISCOUNT_ONE_OF_SCHEMAS = ["DiscountAmount", "DiscountFixed", "DiscountPercent", "DiscountUnit", "DiscountUnitMultiple"]

class RedeemableResultPromotionTierDiscount(BaseModel):
    """
    Discount details about the type of discount to be applied for the redeemable.
    """
    # data type: DiscountAmount
    oneof_schema_1_validator: Optional[DiscountAmount] = None
    # data type: DiscountUnit
    oneof_schema_2_validator: Optional[DiscountUnit] = None
    # data type: DiscountUnitMultiple
    oneof_schema_3_validator: Optional[DiscountUnitMultiple] = None
    # data type: DiscountPercent
    oneof_schema_4_validator: Optional[DiscountPercent] = None
    # data type: DiscountFixed
    oneof_schema_5_validator: Optional[DiscountFixed] = None
    if TYPE_CHECKING:
        actual_instance: Union[DiscountAmount, DiscountFixed, DiscountPercent, DiscountUnit, DiscountUnitMultiple]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(REDEEMABLE_RESULT_PROMOTION_TIER_DISCOUNT_ONE_OF_SCHEMAS, const=True)

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
        instance = RedeemableResultPromotionTierDiscount.construct()
        error_messages = []
        match = 0
        # validate data type: DiscountAmount
        if not isinstance(v, DiscountAmount):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DiscountAmount`")
        else:
            match += 1
        # validate data type: DiscountUnit
        if not isinstance(v, DiscountUnit):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DiscountUnit`")
        else:
            match += 1
        # validate data type: DiscountUnitMultiple
        if not isinstance(v, DiscountUnitMultiple):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DiscountUnitMultiple`")
        else:
            match += 1
        # validate data type: DiscountPercent
        if not isinstance(v, DiscountPercent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DiscountPercent`")
        else:
            match += 1
        # validate data type: DiscountFixed
        if not isinstance(v, DiscountFixed):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DiscountFixed`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in RedeemableResultPromotionTierDiscount with oneOf schemas: DiscountAmount, DiscountFixed, DiscountPercent, DiscountUnit, DiscountUnitMultiple. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in RedeemableResultPromotionTierDiscount with oneOf schemas: DiscountAmount, DiscountFixed, DiscountPercent, DiscountUnit, DiscountUnitMultiple. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> RedeemableResultPromotionTierDiscount:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> RedeemableResultPromotionTierDiscount:
        """Returns the object represented by the json string"""
        instance = RedeemableResultPromotionTierDiscount.construct()
        error_messages = []
        match = 0

        # deserialize data into DiscountAmount
        try:
            instance.actual_instance = DiscountAmount.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DiscountUnit
        try:
            instance.actual_instance = DiscountUnit.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DiscountUnitMultiple
        try:
            instance.actual_instance = DiscountUnitMultiple.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DiscountPercent
        try:
            instance.actual_instance = DiscountPercent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DiscountFixed
        try:
            instance.actual_instance = DiscountFixed.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into RedeemableResultPromotionTierDiscount with oneOf schemas: DiscountAmount, DiscountFixed, DiscountPercent, DiscountUnit, DiscountUnitMultiple. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into RedeemableResultPromotionTierDiscount with oneOf schemas: DiscountAmount, DiscountFixed, DiscountPercent, DiscountUnit, DiscountUnitMultiple. Details: " + ", ".join(error_messages))
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


