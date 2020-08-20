import unittest
from facade import DatabaseFacade


class FacadeTest(unittest.TestCase):
    def setUp(self) -> None:
        self._database = DatabaseFacade()

    def tearDown(self) -> None:
        self._database.disconnect()
        self._database = None

    def test_get_all_ids_returns_ids(self):
        self._database.update_table_with_note("Test note")
        ids = self._database.get_all_ids()

        self.assertTrue(len(ids) > 0)
        for id in ids:
            self.assertTrue(type(id) == int)

    def test_get_row_count_returns_rows(self):
        self._database.update_table_with_note("Test note 1")
        self._database.update_table_with_note("Test note 2")
        row_count = self._database.count_rows()
        self.assertEqual(row_count, 2)
