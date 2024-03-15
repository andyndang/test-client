"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .segmenttag import SegmentTag
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LogAsyncRequest:
    r"""Request payload for LogAsync."""
    UNSET='__SPEAKEASY_UNSET__'
    dataset_timestamp: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datasetTimestamp') }})
    segment_tags: List[SegmentTag] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('segmentTags') }})
    region: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is LogAsyncRequest.UNSET }})
    
