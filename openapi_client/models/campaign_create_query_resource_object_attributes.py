# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-08-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.audiences_sub_object import AudiencesSubObject
from openapi_client.models.campaign_create_query_resource_object_attributes_campaign_messages import CampaignCreateQueryResourceObjectAttributesCampaignMessages
from openapi_client.models.send_strategy_sub_object import SendStrategySubObject

class CampaignCreateQueryResourceObjectAttributes(BaseModel):
    """
    CampaignCreateQueryResourceObjectAttributes
    """
    name: Optional[StrictStr] = Field(..., description="The campaign name")
    audiences: AudiencesSubObject = Field(...)
    send_strategy: SendStrategySubObject = Field(...)
    send_options: Optional[Dict[str, Any]] = Field(None, description="Options to use when sending a campaign")
    tracking_options: Optional[Dict[str, Any]] = Field(None, description="The tracking options associated with the campaign")
    campaign_messages: CampaignCreateQueryResourceObjectAttributesCampaignMessages = Field(..., alias="campaign-messages")
    __properties = ["name", "audiences", "send_strategy", "send_options", "tracking_options", "campaign-messages"]

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
    def from_json(cls, json_str: str) -> CampaignCreateQueryResourceObjectAttributes:
        """Create an instance of CampaignCreateQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of audiences
        if self.audiences:
            _dict['audiences'] = self.audiences.to_dict()
        # override the default output from pydantic by calling `to_dict()` of send_strategy
        if self.send_strategy:
            _dict['send_strategy'] = self.send_strategy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_messages
        if self.campaign_messages:
            _dict['campaign-messages'] = self.campaign_messages.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignCreateQueryResourceObjectAttributes:
        """Create an instance of CampaignCreateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignCreateQueryResourceObjectAttributes.parse_obj(obj)

        _obj = CampaignCreateQueryResourceObjectAttributes.parse_obj({
            "name": obj.get("name"),
            "audiences": AudiencesSubObject.from_dict(obj.get("audiences")) if obj.get("audiences") is not None else None,
            "send_strategy": SendStrategySubObject.from_dict(obj.get("send_strategy")) if obj.get("send_strategy") is not None else None,
            "send_options": obj.get("send_options"),
            "tracking_options": obj.get("tracking_options"),
            "campaign_messages": CampaignCreateQueryResourceObjectAttributesCampaignMessages.from_dict(obj.get("campaign-messages")) if obj.get("campaign-messages") is not None else None
        })
        return _obj

