"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import provisionnewuserresponse as components_provisionnewuserresponse
from typing import Optional


@dataclasses.dataclass
class ProvisionNewUserResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    provision_new_user_response: Optional[components_provisionnewuserresponse.ProvisionNewUserResponse] = dataclasses.field(default=None)
    r"""ProvisionNewUser 200 response"""
    
