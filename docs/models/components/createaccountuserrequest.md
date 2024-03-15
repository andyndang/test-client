# CreateAccountUserRequest

Request to create a user in an account


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `email`                                                 | *str*                                                   | :heavy_check_mark:                                      | The user's email address                                |
| `external_id`                                           | *Optional[str]*                                         | :heavy_minus_sign:                                      | The external id the user is known by in the provisioner |
| `user_schema`                                           | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |
| `active`                                                | *Optional[bool]*                                        | :heavy_minus_sign:                                      | N/A                                                     |