"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import getmembershipsresponse as components_getmembershipsresponse
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetMembershipsByOrgRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetMembershipsByOrgResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    get_memberships_response: Optional[components_getmembershipsresponse.GetMembershipsResponse] = dataclasses.field(default=None)
    r"""GetMembershipsByOrg 200 response"""
    
