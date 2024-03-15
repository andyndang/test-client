# AddMembershipRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `org_id`                                           | *str*                                              | :heavy_check_mark:                                 | N/A                                                |                                                    |
| `email`                                            | *str*                                              | :heavy_check_mark:                                 | N/A                                                |                                                    |
| `role`                                             | [components.Role](../../models/components/role.md) | :heavy_check_mark:                                 | N/A                                                | admin                                              |
| `created_by`                                       | *Optional[str]*                                    | :heavy_minus_sign:                                 | N/A                                                |                                                    |
| `default`                                          | *Optional[bool]*                                   | :heavy_minus_sign:                                 | N/A                                                |                                                    |