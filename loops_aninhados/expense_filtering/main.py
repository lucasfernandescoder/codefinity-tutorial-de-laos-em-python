# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50],[200, 300, 120, 80],
                [180, 220, 130, 170], [600, 250, 200, 90],
                [300, 180, 150, 70], [400, 320, 110, 100],
                [550, 270, 180, 60], [250, 190, 140, 120],
                [700, 350, 210, 110], [450, 230, 160, 95],
                [320, 280, 190, 85], [580, 260, 175, 75]]

# List to store processed expenses
processed_expenses = []
i = 0
while i < len(travel_costs):
    j = 0
    trip_expenses = []

    while j < len(travel_costs[i]):
        if travel_costs[i][j] <= 100:
            trip_expenses.append("Cheap")
        else:
            trip_expenses.append(travel_costs[i][j])
        j += 1

    processed_expenses.append(trip_expenses)
    i += 1

print('Processed Travel Expenses:', processed_expenses)