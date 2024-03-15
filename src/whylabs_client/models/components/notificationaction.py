"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .actiontype import ActionType
from .notificationactionpayload import NotificationActionPayload
from .notificationrelationshipitem import NotificationRelationshipItem
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from typing import List, Optional
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NotificationAction:
    UNSET='__SPEAKEASY_UNSET__'
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    type: ActionType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    payload: NotificationActionPayload = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('payload') }})
    last_update: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lastUpdate'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    enabled: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is NotificationAction.UNSET }})
    references: Optional[List[NotificationRelationshipItem]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('references'), 'exclude': lambda f: f is NotificationAction.UNSET }})
    creation_time: Optional[datetime] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creationTime'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is NotificationAction.UNSET }})
    
