def calculate_profit(num_cakes, num_cookies):
    if num_cakes > 250:
        return -1
    if num_cookies > 200:
        return -1
    if num_cakes + num_cookies > 300:
        return -1
    profit = (num_cakes * 5) + (num_cookies)
    return profit
