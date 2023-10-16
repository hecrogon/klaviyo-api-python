# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-10-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.profile_location import ProfileLocation

class OnsiteProfileCreateQueryResourceObjectAttributes(BaseModel):
    """
    OnsiteProfileCreateQueryResourceObjectAttributes
    """
    email: Optional[StrictStr] = Field(None, description="Individual's email address")
    phone_number: Optional[StrictStr] = Field(None, description="Individual's phone number in E.164 format")
    external_id: Optional[StrictStr] = Field(None, description="A unique identifier used by customers to associate Klaviyo profiles with profiles in an external system, such as a point-of-sale system. Format varies based on the external system.")
    anonymous_id: Optional[StrictStr] = None
    kx: Optional[StrictStr] = Field(None, alias="_kx", description="Also known as the `exchange_id`, this is an encrypted identifier used for identifying a profile by Klaviyo's web tracking.  You can use this field as a filter when retrieving profiles via the Get Profiles endpoint.")
    first_name: Optional[StrictStr] = Field(None, description="Individual's first name")
    last_name: Optional[StrictStr] = Field(None, description="Individual's last name")
    organization: Optional[StrictStr] = Field(None, description="Name of the company or organization within the company for whom the individual works")
    title: Optional[StrictStr] = Field(None, description="Individual's job title")
    image: Optional[StrictStr] = Field(None, description="URL pointing to the location of a profile image")
    location: Optional[ProfileLocation] = None
    properties: Optional[Dict[str, Any]] = Field(None, description="An object containing key/value pairs for any custom properties assigned to this profile")
    __properties = ["email", "phone_number", "external_id", "anonymous_id", "_kx", "first_name", "last_name", "organization", "title", "image", "location", "properties"]

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
    def from_json(cls, json_str: str) -> OnsiteProfileCreateQueryResourceObjectAttributes:
        """Create an instance of OnsiteProfileCreateQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        # set to None if phone_number (nullable) is None
        # and __fields_set__ contains the field
        if self.phone_number is None and "phone_number" in self.__fields_set__:
            _dict['phone_number'] = None

        # set to None if external_id (nullable) is None
        # and __fields_set__ contains the field
        if self.external_id is None and "external_id" in self.__fields_set__:
            _dict['external_id'] = None

        # set to None if anonymous_id (nullable) is None
        # and __fields_set__ contains the field
        if self.anonymous_id is None and "anonymous_id" in self.__fields_set__:
            _dict['anonymous_id'] = None

        # set to None if kx (nullable) is None
        # and __fields_set__ contains the field
        if self.kx is None and "kx" in self.__fields_set__:
            _dict['_kx'] = None

        # set to None if first_name (nullable) is None
        # and __fields_set__ contains the field
        if self.first_name is None and "first_name" in self.__fields_set__:
            _dict['first_name'] = None

        # set to None if last_name (nullable) is None
        # and __fields_set__ contains the field
        if self.last_name is None and "last_name" in self.__fields_set__:
            _dict['last_name'] = None

        # set to None if organization (nullable) is None
        # and __fields_set__ contains the field
        if self.organization is None and "organization" in self.__fields_set__:
            _dict['organization'] = None

        # set to None if title (nullable) is None
        # and __fields_set__ contains the field
        if self.title is None and "title" in self.__fields_set__:
            _dict['title'] = None

        # set to None if image (nullable) is None
        # and __fields_set__ contains the field
        if self.image is None and "image" in self.__fields_set__:
            _dict['image'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OnsiteProfileCreateQueryResourceObjectAttributes:
        """Create an instance of OnsiteProfileCreateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OnsiteProfileCreateQueryResourceObjectAttributes.parse_obj(obj)

        _obj = OnsiteProfileCreateQueryResourceObjectAttributes.parse_obj({
            "email": obj.get("email"),
            "phone_number": obj.get("phone_number"),
            "external_id": obj.get("external_id"),
            "anonymous_id": obj.get("anonymous_id"),
            "kx": obj.get("_kx"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "organization": obj.get("organization"),
            "title": obj.get("title"),
            "image": obj.get("image"),
            "location": ProfileLocation.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "properties": obj.get("properties")
        })
        return _obj


