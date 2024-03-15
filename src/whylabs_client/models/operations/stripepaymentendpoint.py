"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import response as components_response
from typing import Optional


@dataclasses.dataclass
class StripePaymentEndpointResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    response: Optional[components_response.Response] = dataclasses.field(default=None)
    r"""StripePaymentEndpoint 200 response"""
    

