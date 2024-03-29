"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import notificationsettings as components_notificationsettings
from typing import Optional


@dataclasses.dataclass
class UpdateNotificationSettingsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    notification_settings: components_notificationsettings.NotificationSettings = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateNotificationSettingsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    notification_settings: Optional[components_notificationsettings.NotificationSettings] = dataclasses.field(default=None)
    r"""UpdateNotificationSettings 200 response"""
    

