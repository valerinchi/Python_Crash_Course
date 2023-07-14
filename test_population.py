from population import get_formatted_country

def test_city_country():
    """Do cities like 'Santiago, Chile' work?"""
    formatted_string = get_formatted_country('santiago', 'chile')
    assert formatted_string == 'Santiago, Chile'

def test_city_country_population():
    """Do cities with population like 'Santiago, Chile - population 5000000' work?"""
    formatted_string = get_formatted_country('santiago', 'chile', population=5000000)
    assert formatted_string == 'Santiago, Chile - Population 5000000'

test_city_country()
test_city_country_population()

