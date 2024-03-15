# OrganizationMetadata

Metadata about an organization


## Fields

| Field                                                                                                                                | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          | Example                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                 | *str*                                                                                                                                | :heavy_check_mark:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `name`                                                                                                                               | *str*                                                                                                                                | :heavy_check_mark:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `creation_time`                                                                                                                      | *int*                                                                                                                                | :heavy_check_mark:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `deleted`                                                                                                                            | *bool*                                                                                                                               | :heavy_check_mark:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `subscription_tier`                                                                                                                  | [Optional[components.OrganizationMetadataSubscriptionTier]](../../models/components/organizationmetadatasubscriptiontier.md)         | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  | FREE                                                                                                                                 |
| `email_domains`                                                                                                                      | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `observatory_url`                                                                                                                    | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `notification_settings`                                                                                                              | [Optional[components.OrganizationMetadataNotificationSettings]](../../models/components/organizationmetadatanotificationsettings.md) | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `use_cloud_front`                                                                                                                    | *Optional[bool]*                                                                                                                     | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `parent_org_id`                                                                                                                      | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `subscription_id`                                                                                                                    | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `storage_bucket_override`                                                                                                            | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |
| `allow_managed_membership_updates_only`                                                                                              | *Optional[bool]*                                                                                                                     | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |