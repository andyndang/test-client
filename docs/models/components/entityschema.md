# EntitySchema

Entity schema for a dataset


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `columns`                                                                                    | Dict[str, [components.ColumnSchema](../../models/components/columnschema.md)]                | :heavy_check_mark:                                                                           | Column schema for a given column                                                             |
| `metadata`                                                                                   | [Optional[components.EntitySchemaMetadata]](../../models/components/entityschemametadata.md) | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `metrics`                                                                                    | Dict[str, [components.MetricSchema](../../models/components/metricschema.md)]                | :heavy_minus_sign:                                                                           | Schema for user-defined metrics (map of unique custom metric labels to their definitions)    |