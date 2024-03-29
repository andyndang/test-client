"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import membershipmetadata as components_membershipmetadata
from ...models.components import role as components_role
from typing import Optional


@dataclasses.dataclass
class CreateOrganizationMembershipRequest:
    UNSET='__SPEAKEASY_UNSET__'
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    email: str = dataclasses.field(metadata={'query_param': { 'field_name': 'email', 'style': 'form', 'explode': True }})
    role: components_role.Role = dataclasses.field(metadata={'query_param': { 'field_name': 'role', 'style': 'form', 'explode': True }})
    set_default: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'set_default', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class CreateOrganizationMembershipResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    membership_metadata: Optional[components_membershipmetadata.MembershipMetadata] = dataclasses.field(default=None)
    r"""CreateOrganizationMembership 200 response"""
    

