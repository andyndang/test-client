"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import accountuser as components_accountuser
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetAccountUserByEmailRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    email: str = dataclasses.field(metadata={'query_param': { 'field_name': 'email', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetAccountUserByEmailResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    account_user: Optional[components_accountuser.AccountUser] = dataclasses.field(default=None)
    r"""GetAccountUserByEmail 200 response"""
    
