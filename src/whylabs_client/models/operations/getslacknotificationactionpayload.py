"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import slacknotificationaction as components_slacknotificationaction
from typing import Optional


@dataclasses.dataclass
class GetSlackNotificationActionPayloadResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    slack_notification_action: Optional[components_slacknotificationaction.SlackNotificationAction] = dataclasses.field(default=None)
    r"""getSlackNotificationActionPayload 200 response"""
    

