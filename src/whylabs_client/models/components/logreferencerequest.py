"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LogReferenceRequest:
    r"""Request payload for LogReference."""
    UNSET='__SPEAKEASY_UNSET__'
    alias: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alias'), 'exclude': lambda f: f is LogReferenceRequest.UNSET }})
    dataset_timestamp: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datasetTimestamp'), 'exclude': lambda f: f is LogReferenceRequest.UNSET }})
    region: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is LogReferenceRequest.UNSET }})
    

