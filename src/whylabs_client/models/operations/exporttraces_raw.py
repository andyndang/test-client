"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import exporttraceserviceresponse as components_exporttraceserviceresponse
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class ExportTracesRawRequest:
    UNSET='__SPEAKEASY_UNSET__'
    request_body: bytes = dataclasses.field(metadata={'request': { 'media_type': 'application/x-protobuf' }})
    x_whylabs_resource: Optional[str] = dataclasses.field(default=UNSET, metadata={'header': { 'field_name': 'X-WHYLABS-RESOURCE', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class ExportTracesRawResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    export_trace_service_response: Optional[components_exporttraceserviceresponse.ExportTraceServiceResponse] = dataclasses.field(default=None)
    r"""ExportTraces 200 response"""
    
