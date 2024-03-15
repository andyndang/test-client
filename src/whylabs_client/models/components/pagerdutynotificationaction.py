"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PagerDutyNotificationAction:
    r"""Pager Duty payload for Notification Actions"""
    pager_duty_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagerDutyKey') }})
    

