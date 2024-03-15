"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import pagerdutynotificationaction as components_pagerdutynotificationaction
from typing import Optional


@dataclasses.dataclass
class GetPagerDutyNotificationActionPayloadResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    pager_duty_notification_action: Optional[components_pagerdutynotificationaction.PagerDutyNotificationAction] = dataclasses.field(default=None)
    r"""getPagerDutyNotificationActionPayload 200 response"""
    

