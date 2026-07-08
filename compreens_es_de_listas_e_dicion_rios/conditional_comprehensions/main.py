# Given travel wishlist
travel_wishlist = [['Paris', 'France', 2000],['Tokyo', 'Japan', 3000],['New York', 'USA', 2500],
                   ['Kyoto', 'Japan', 1500],['Rome', 'Italy', 2200],['Sydney', 'Australia', 2800],
                   ['Barcelona', 'Spain', 1900],['London', 'UK', 2600],['Berlin', 'Germany', 2100],
                   ['Dubai', 'UAE', 3500],['Bangkok', 'Thailand', 1800],['Singapore', 'Singapore', 2900],
                   ['Los Angeles', 'USA', 2700],['Cape Town', 'South Africa', 2300],['Venice', 'Italy', 2000],
                   ['Istanbul', 'Turkey', 1750],['Toronto', 'Canada', 2250],['Rio de Janeiro', 'Brazil', 1950],
                   ['Athens', 'Greece', 1850]]
                   
# Create a new list of affordable cities
affordable_cities = [city[0] for city in travel_wishlist if city [2] < 2500]

# Testing
print('Affordable Cities:', affordable_cities)