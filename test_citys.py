from city_functions import get_city_country

def test_city_country():
    """Verify that calling get_city_country() returns the correct string."""
    formatted_string = get_city_country('santiago', 'chile')
    assert formatted_string == 'Santiago, Chile'
