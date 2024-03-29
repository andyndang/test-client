"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .errorstatus import ErrorStatus
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StatusResponse:
    UNSET='__SPEAKEASY_UNSET__'
    errors: List[ErrorStatus] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('errors') }})
    request_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('requestId'), 'exclude': lambda f: f is StatusResponse.UNSET }})
    

