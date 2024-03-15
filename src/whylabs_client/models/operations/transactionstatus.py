"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import transactionstatusresponse as components_transactionstatusresponse
from typing import Optional


@dataclasses.dataclass
class TransactionStatusRequest:
    transaction_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'transaction_id', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class TransactionStatusResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    transaction_status_response: Optional[components_transactionstatusresponse.TransactionStatusResponse] = dataclasses.field(default=None)
    r"""TransactionStatus 200 response"""
    

