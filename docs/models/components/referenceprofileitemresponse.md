# ReferenceProfileItemResponse

A single reference item response.


## Fields

| Field               | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `org_id`            | *str*               | :heavy_check_mark:  | N/A                 |
| `model_id`          | *str*               | :heavy_check_mark:  | N/A                 |
| `alias`             | *str*               | :heavy_check_mark:  | N/A                 |
| `id`                | *str*               | :heavy_check_mark:  | N/A                 |
| `upload_timestamp`  | *int*               | :heavy_check_mark:  | N/A                 |
| `dataset_timestamp` | *Optional[int]*     | :heavy_minus_sign:  | N/A                 |
| `download_url`      | *Optional[str]*     | :heavy_minus_sign:  | N/A                 |
| `segments`          | List[*str*]         | :heavy_minus_sign:  | N/A                 |
| `download_urls`     | List[*str*]         | :heavy_minus_sign:  | N/A                 |