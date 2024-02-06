def record_outing(num_seniors):
    senior_list = []
    num_extra_people = 0

    for i in range(num_seniors):
        name = input(f"Enter name of senior citizen {i+1}: ")
        payement = float(input(f"Enter amount paid by {name}: $"))

    if num_seniors < 36:
        num_extra_people = 36 - num_seniors
        for i in range(num_extra_people):
            name = input(f"Enter name of extra person {i+1}: ")
            payement = float(input(f"Enter amound paid by {name}: $"))
            senior_list.append((name, payement))

    total_collect = sum(payement for _, payement in senior_list)

    print("\nList of people on the outing: ")
    for name, payement in senior_list:
        print(f"{name}: ${payement}")

    return total_collect

num_seniors = int(input("Enter the number of senior citizens going on the outing: "))
total_collect = record_outing(num_seniors)

print("\nTotal amount collected: $", total_collect)