"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import patchaccountmembershipsrequest as components_patchaccountmembershipsrequest
from ...models.components import role as components_role
from ...models.components import statusresponse as components_statusresponse
from typing import Optional


@dataclasses.dataclass
class PatchOrganizationMembershipsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    managed_org_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'managed_org_id', 'style': 'form', 'explode': True }})
    role: components_role.Role = dataclasses.field(metadata={'query_param': { 'field_name': 'role', 'style': 'form', 'explode': True }})
    patch_account_memberships_request: components_patchaccountmembershipsrequest.PatchAccountMembershipsRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PatchOrganizationMembershipsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    status_response: Optional[components_statusresponse.StatusResponse] = dataclasses.field(default=None)
    r"""PatchOrganizationMemberships 200 response"""
    
