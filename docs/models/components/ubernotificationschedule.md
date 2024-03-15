# UberNotificationSchedule


Combination of all possible schedule types, a hacky workaround for bugs in generated clients that use polymorphic types.
There are three types of schedules. Weekly, Daily, and Individual. You need to set the right fields for each one.

Weekly:
    enabled, cadence=WEEKLY, dayOfWeek, local24HourOfDay, localMinuteOfHour, localTimezone
    
Daily:
    enabled, cadence=DAILY, local24HourOfDay, localMinuteOfHour, localTimezone
    
Individual:
    enabled, cadence=INDIVIDUAL



## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `enabled`                                                                                            | *bool*                                                                                               | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `cadence`                                                                                            | [components.NotificationSqsMessageCadence](../../models/components/notificationsqsmessagecadence.md) | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `day_of_week`                                                                                        | [Optional[components.DayOfWeek]](../../models/components/dayofweek.md)                               | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `local24_hour_of_day`                                                                                | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `local_minute_of_hour`                                                                               | *Optional[int]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `local_timezone`                                                                                     | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |