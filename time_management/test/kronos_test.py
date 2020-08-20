import unittest
import datetime
import kronos

string_format_time = "%Y-%m-%d %H:%M:%S"
date_time_str = "2020-07-19 18:14:21"


class KronosTest(unittest.TestCase):
    def test_get_day_of_week(self):
        for i in range(len(kronos.week_days)):
            date = kronos.get_date_time_from_string(f"2020-08-{10 + i} 13:00:00")
            self.assertEqual(kronos.week_days.get(i), kronos.get_day_of_week(date))

    def test_is_yesterday(self):
        date_time = kronos.get_date_time_from_string("2020-07-20 18:14:21")
        self.assertTrue(kronos.is_yesterday(date_time_str, today=date_time))
        date_time = kronos.get_date_time_from_string("2020-07-19 18:14:21")
        self.assertFalse(kronos.is_yesterday(date_time_str, today=date_time))

    def test_is_previous_friday(self):
        last_friday = "2020-08-14 13:00:00"
        last_monday = kronos.get_date_time_from_string("2020-08-17 13:00:00")
        self.assertTrue(kronos.is_previous_friday(last_friday, last_monday))
        last_tuesday = kronos.get_date_time_from_string("2020-08-18 13:00:00")
        self.assertFalse(kronos.is_previous_friday(last_friday, last_tuesday))

    def test_is_overdue_checks_correctly(self):
        creation_date = "2020-08-10 13:00:00"
        completion_goal = 5
        self.assertTrue(kronos.is_overdue(creation_date, completion_goal))

        on_time_date = kronos.get_date_time_as_string()
        on_time_goal = 100
        self.assertFalse(kronos.is_overdue(on_time_date, on_time_goal))
