# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
food = 0
transport = 0
utilities = 0
week_total = 0
weeks = []
# Calculates expenses
# Use loop statements
for week in monthly_expenses:
    weeks_total = 0
    food = 0
    transport = 0
    utilities = 0
    for category in week:
        if category == week[0]:
            food += category
        elif category == week[1]:
            transport += category
        else:
            utilities += category
        week_total += category
    weeks.append(week_total)
        
total = food + transport + utilities


...

# Print expenses
print(f'MONTHLY EXPENSES')
print(f'----------------')
print(f'Food:',{food})
print(f'Transport:',{transport})
print(f'Utilities:',{utilities})
print(f'Week 1:',weeks[0])
print(f'Week 2:',weeks[1])
print(f'Week 3:',weeks[2])
print(f'Week 4:',weeks[3])
print(f'---------------')
print(f'TOTAL:',total)