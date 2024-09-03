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
from pydantic import BaseModel, Field, StrictStr, validator
from voucherify_client.models.loyalty_tiers_expiration_all_expiration_date import LoyaltyTiersExpirationAllExpirationDate
from voucherify_client.models.loyalty_tiers_expiration_all_start_date import LoyaltyTiersExpirationAllStartDate

class LoyaltyTiersExpirationAll(BaseModel):
    """
    Defines the Loyalty Tiers Expiration.  # noqa: E501
    """
    qualification_type: Optional[StrictStr] = Field(None, description="Tier qualification.     `BALANCE`: Points balance is based on the customer's current points balance. Customers qualify for the tier if their points balance is in the points range of the tier.   `POINTS_IN_PERIOD`: A customer qualifies for the tier only if the sum of the accumulated points in a **defined time interval** reaches the tier threshold.")
    qualification_period: Optional[StrictStr] = Field(None, description="Customers can qualify for the tier if they collected enough points in a given time period. So, in addition to the customer having to reach a points range, they also need to have collected the points within a set time period.      | **Period** | **Definition** | |:---|:---| | **Calendar Month** | Points collected in one calendar month<br>January, February, March, etc. | | **Calendar Quarter** | Points collected in the quarter<br>- January - March<br>- April - June<br>- July - September<br>- October - December | | **Calendar Half-year** | Points collected in the half-year<br>- January - June<br>- July - December | | **Calendar Year** | Points collected in one calendar year<br>January - December |")
    start_date: Optional[LoyaltyTiersExpirationAllStartDate] = None
    expiration_date: Optional[LoyaltyTiersExpirationAllExpirationDate] = None
    __properties = ["qualification_type", "qualification_period", "start_date", "expiration_date"]

    @validator('qualification_type')
    def qualification_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BALANCE', 'POINTS_IN_PERIOD',):
            raise ValueError("must be one of enum values ('BALANCE', 'POINTS_IN_PERIOD')")
        return value

    @validator('qualification_period')
    def qualification_period_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('MONTH', 'QUARTER', 'HALF_YEAR', 'YEAR',):
            raise ValueError("must be one of enum values ('MONTH', 'QUARTER', 'HALF_YEAR', 'YEAR')")
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
    def from_json(cls, json_str: str) -> LoyaltyTiersExpirationAll:
        """Create an instance of LoyaltyTiersExpirationAll from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of start_date
        if self.start_date:
            _dict['start_date'] = self.start_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expiration_date
        if self.expiration_date:
            _dict['expiration_date'] = self.expiration_date.to_dict()
        # set to None if qualification_type (nullable) is None
        # and __fields_set__ contains the field
        if self.qualification_type is None and "qualification_type" in self.__fields_set__:
            _dict['qualification_type'] = None

        # set to None if qualification_period (nullable) is None
        # and __fields_set__ contains the field
        if self.qualification_period is None and "qualification_period" in self.__fields_set__:
            _dict['qualification_period'] = None

        # set to None if start_date (nullable) is None
        # and __fields_set__ contains the field
        if self.start_date is None and "start_date" in self.__fields_set__:
            _dict['start_date'] = None

        # set to None if expiration_date (nullable) is None
        # and __fields_set__ contains the field
        if self.expiration_date is None and "expiration_date" in self.__fields_set__:
            _dict['expiration_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltyTiersExpirationAll:
        """Create an instance of LoyaltyTiersExpirationAll from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltyTiersExpirationAll.parse_obj(obj)

        _obj = LoyaltyTiersExpirationAll.parse_obj({
            "qualification_type": obj.get("qualification_type"),
            "qualification_period": obj.get("qualification_period"),
            "start_date": LoyaltyTiersExpirationAllStartDate.from_dict(obj.get("start_date")) if obj.get("start_date") is not None else None,
            "expiration_date": LoyaltyTiersExpirationAllExpirationDate.from_dict(obj.get("expiration_date")) if obj.get("expiration_date") is not None else None
        })
        return _obj


