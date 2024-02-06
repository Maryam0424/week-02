def cal_cost(num_seniors):
    if num_seniors < 10 or num_seniors > 36:
        print("Invalid number of senior citizens. Minimum 10 and Maximum 36 allowed.")
        return None, None
    
    if num_seniors <= 16:
        hire_cost = 150
        meal_cost = 14.00
        ticket_cost = 2.00

    elif num_seniors <= 26:
        hire_cost = 190
        meal_cost = 13.50
        ticket_cost = 20.00
        
    else:
        hire_cost = 225
        meal_cost = 13.00
        ticket_cost = 19.00

    carer_count = 2
    if num_seniors > 24:
        carer_count += 1

    total_cost = hire_cost + (meal_cost + ticket_cost) * num_seniors
    cost_per_person  = total_cost / num_seniors

    return total_cost, cost_per_person

num_seniors = int(input("Enter the number of senior citizens: "))
total_cost, cost_per_person = cal_cost(num_seniors)

if total_cost is not None and cost_per_person is not None: 
    print("Total Cost: ", total_cost)
    print("Cost per person: ", cost_per_person)
    