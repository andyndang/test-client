"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .segmenttag import SegmentTag
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SegmentWeightSegment:
    tags: List[SegmentTag] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SegmentWeight:
    UNSET='__SPEAKEASY_UNSET__'
    weights: Dict[str, float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weights') }})
    r"""Entity weight value for each entity"""
    segment: Optional[SegmentWeightSegment] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('segment'), 'exclude': lambda f: f is SegmentWeight.UNSET }})
    

