"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import diagnosticintervalrequest as components_diagnosticintervalrequest
from ...models.components import diagnosticintervalresponse as components_diagnosticintervalresponse
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class RecommendDiagnosticIntervalRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    diagnostic_interval_request: components_diagnosticintervalrequest.DiagnosticIntervalRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class RecommendDiagnosticIntervalResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    diagnostic_interval_response: Optional[components_diagnosticintervalresponse.DiagnosticIntervalResponse] = dataclasses.field(default=None)
    r"""RecommendDiagnosticInterval 200 response"""
    

