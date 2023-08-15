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


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator

class CatalogVariantUpdateQueryResourceObjectAttributes(BaseModel):
    """
    CatalogVariantUpdateQueryResourceObjectAttributes
    """
    title: Optional[StrictStr] = Field(None, description="The title of the catalog item variant.")
    description: Optional[StrictStr] = Field(None, description="A description of the catalog item variant.")
    sku: Optional[StrictStr] = Field(None, description="The SKU of the catalog item variant.")
    inventory_policy: Optional[StrictInt] = Field(None, description="This field controls the visibility of this catalog item variant in product feeds/blocks. This field supports the following values: `1`: a product will not appear in dynamic product recommendation feeds and blocks if it is out of stock. `0` or `2`: a product can appear in dynamic product recommendation feeds and blocks regardless of inventory quantity.")
    inventory_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The quantity of the catalog item variant currently in stock.")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="This field can be used to set the price on the catalog item variant, which is what gets displayed for the item variant when included in emails. For most price-update use cases, you will also want to update the `price` on any parent items using the [Update Catalog Item Endpoint](https://developers.klaviyo.com/en/reference/update_catalog_item).")
    url: Optional[StrictStr] = Field(None, description="URL pointing to the location of the catalog item variant on your website.")
    image_full_url: Optional[StrictStr] = Field(None, description="URL pointing to the location of a full image of the catalog item variant.")
    image_thumbnail_url: Optional[StrictStr] = Field(None, description="URL pointing to the location of an image thumbnail of the catalog item variant.")
    images: Optional[conlist(StrictStr)] = Field(None, description="List of URLs pointing to the locations of images of the catalog item variant.")
    custom_metadata: Optional[Dict[str, Any]] = Field(None, description="Flat JSON blob to provide custom metadata about the catalog item variant. May not exceed 100kb.")
    published: Optional[StrictBool] = Field(None, description="Boolean value indicating whether the catalog item variant is published.")
    __properties = ["title", "description", "sku", "inventory_policy", "inventory_quantity", "price", "url", "image_full_url", "image_thumbnail_url", "images", "custom_metadata", "published"]

    @validator('inventory_policy')
    def inventory_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (0, 1, 2):
            raise ValueError("must be one of enum values (0, 1, 2)")
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
    def from_json(cls, json_str: str) -> CatalogVariantUpdateQueryResourceObjectAttributes:
        """Create an instance of CatalogVariantUpdateQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if title (nullable) is None
        # and __fields_set__ contains the field
        if self.title is None and "title" in self.__fields_set__:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if sku (nullable) is None
        # and __fields_set__ contains the field
        if self.sku is None and "sku" in self.__fields_set__:
            _dict['sku'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if image_full_url (nullable) is None
        # and __fields_set__ contains the field
        if self.image_full_url is None and "image_full_url" in self.__fields_set__:
            _dict['image_full_url'] = None

        # set to None if image_thumbnail_url (nullable) is None
        # and __fields_set__ contains the field
        if self.image_thumbnail_url is None and "image_thumbnail_url" in self.__fields_set__:
            _dict['image_thumbnail_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CatalogVariantUpdateQueryResourceObjectAttributes:
        """Create an instance of CatalogVariantUpdateQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CatalogVariantUpdateQueryResourceObjectAttributes.parse_obj(obj)

        _obj = CatalogVariantUpdateQueryResourceObjectAttributes.parse_obj({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "sku": obj.get("sku"),
            "inventory_policy": obj.get("inventory_policy"),
            "inventory_quantity": obj.get("inventory_quantity"),
            "price": obj.get("price"),
            "url": obj.get("url"),
            "image_full_url": obj.get("image_full_url"),
            "image_thumbnail_url": obj.get("image_thumbnail_url"),
            "images": obj.get("images"),
            "custom_metadata": obj.get("custom_metadata"),
            "published": obj.get("published")
        })
        return _obj

