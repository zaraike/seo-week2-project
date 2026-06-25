import unittest
from cities import create_cities_table, add_city, get_cities, delete_city


class TestCities(unittest.TestCase):

    def test_add_and_get_city(self):
        create_cities_table()
        add_city("test_user", "TestCity")
        cities = get_cities("test_user")
        self.assertIn("TestCity", cities)
        delete_city("test_user", "TestCity")

    def test_delete_city(self):
        create_cities_table()
        add_city("test_user", "DeleteMe")
        delete_city("test_user", "DeleteMe")
        cities = get_cities("test_user")
        self.assertNotIn("DeleteMe", cities)

    def test_empty_user_has_no_cities(self):
        create_cities_table()
        cities = get_cities("nobody_user_12345")
        self.assertEqual(cities, [])


if __name__ == "__main__":
    unittest.main()
