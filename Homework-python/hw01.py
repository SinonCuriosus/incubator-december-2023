import unittest
from datetime import date

def is_eligible_for_covid_vaccine(birth_year):
    """
    Validate if a person is above 80 years old and eligible for a COVID vaccine.

    Parameters:
    - birth_year (int): The birth year of the person.

    Returns:
    - bool: True if the person is above 80 years old, False otherwise.
    """
    current_year = date.today().year
    print(current_year)
    age = current_year - birth_year

    return age > 80

class TestCovidVaccineEligibility(unittest.TestCase):
    def test_eligibility_above_80(self):
        # Test with birth year of a person above 80
        result = is_eligible_for_covid_vaccine(1940)  # Assuming the current year is 2024
        self.assertTrue(result, "Person should be eligible for COVID vaccine.")

    def test_eligibility_below_80(self):
        # Test with birth year of a person below 80
        result = is_eligible_for_covid_vaccine(1970)  # Assuming the current year is 2024
        self.assertFalse(result, "Person should not be eligible for COVID vaccine.")

    def test_eligibility_equal_80(self):
        # Test with birth year of a person exactly 80
        result = is_eligible_for_covid_vaccine(1944)  # Assuming the current year is 2024
        self.assertFalse(result, "Person should not be eligible for COVID vaccine.")

if __name__ == '__main__':
    unittest.main()