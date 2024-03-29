"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import logreferencerequest as components_logreferencerequest
from ...models.components import logreferenceresponse as components_logreferenceresponse
from typing import Optional


@dataclasses.dataclass
class LogReferenceRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'model_id', 'style': 'simple', 'explode': False }})
    log_reference_request: components_logreferencerequest.LogReferenceRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class LogReferenceResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    log_reference_response: Optional[components_logreferenceresponse.LogReferenceResponse] = dataclasses.field(default=None)
    r"""LogReference 200 response"""
    

