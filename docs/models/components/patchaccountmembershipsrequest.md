# PatchAccountMembershipsRequest

Request for the PatchAccountMemberships API


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `user_ids_to_add`                            | List[*str*]                                  | :heavy_check_mark:                           | A list of userIds that should be members     |
| `user_ids_to_delete`                         | List[*str*]                                  | :heavy_check_mark:                           | A list of userIds that should not be members |