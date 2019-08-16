import unittest
from city_functions import get_formatted_city

class CityCountryTester(unittest.TestCase):
    def test_city_country(self):
        city_country = get_formatted_city("santiago", "chile")
        self.assertEqual(city_country, "Santiago, Chile")


    def test_city_country_population(self):
        city_country = get_formatted_city("santiago", "chile", "5000000")
        self.assertEqual(city_country, "Santiago, Chile - 5000000")
        
unittest.main()
