"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from typing import List, Optional


@dataclasses.dataclass
class AddAccountUsersFromMembershipsRequest:
    org_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'org_id', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class AddAccountUsersFromMembershipsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    strings: Optional[List[str]] = dataclasses.field(default=None)
    r"""AddAccountUsersFromMemberships 200 response"""
    

