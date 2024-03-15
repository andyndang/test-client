"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SlackNotificationAction:
    r"""Slack payload for Notification Actions"""
    slack_webhook: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slackWebhook') }})
    

