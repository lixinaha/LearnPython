# city_country

def city_countrys(city, country):
    return(city.title() + ", " + country.title())

def city_country_population(city, country, population=100):
    return city.title() + ", " + country.title() + " - population " + str(population)