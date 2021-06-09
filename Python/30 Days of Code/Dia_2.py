def solve(meal_cost, tip_percent, tax_percent):
    total_cost =  meal_cost + meal_cost * tip_percent/100 + meal_cost * tax_percent/100
    print(round(total_cost))

solve(12.00, 20, 8)