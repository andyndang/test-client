"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import getmembershipsresponse as components_getmembershipsresponse
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetMembershipsByEmailRequest:
    email: str = dataclasses.field(metadata={'query_param': { 'field_name': 'email', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetMembershipsByEmailResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    get_memberships_response: Optional[components_getmembershipsresponse.GetMembershipsResponse] = dataclasses.field(default=None)
    r"""GetMembershipsByEmail 200 response"""
    
