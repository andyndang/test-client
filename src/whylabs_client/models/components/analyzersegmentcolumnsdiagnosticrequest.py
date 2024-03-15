"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .segment import Segment
from dataclasses_json import Undefined, dataclass_json
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AnalyzerSegmentColumnsDiagnosticRequest:
    interval: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval') }})
    dataset_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datasetId') }})
    analyzer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('analyzerId') }})
    segment: Segment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('segment') }})
    
