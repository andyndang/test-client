"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import listorganizationmembershipsresponse as components_listorganizationmembershipsresponse
from typing import Optional


@dataclasses.dataclass
class ListOrganizationMembershipsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class ListOrganizationMembershipsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    list_organization_memberships_response: Optional[components_listorganizationmembershipsresponse.ListOrganizationMembershipsResponse] = dataclasses.field(default=None)
    r"""ListOrganizationMemberships 200 response"""
    

