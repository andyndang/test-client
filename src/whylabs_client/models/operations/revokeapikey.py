"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import userapikey as components_userapikey
from typing import Optional


@dataclasses.dataclass
class RevokeAPIKeyRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    key_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'key_id', 'style': 'form', 'explode': True }})
    r"""ID of the key to revoke"""
    



@dataclasses.dataclass
class RevokeAPIKeyResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    user_api_key: Optional[components_userapikey.UserAPIKey] = dataclasses.field(default=None)
    r"""Revoked API Key's metadata"""
    

