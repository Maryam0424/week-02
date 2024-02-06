def cal_profit_or_loss(estimate_cost, total_collect):
    if total_collect >= estimate_cost:
        return total_collect - estimate_cost, "profit"
    
    else:
        return estimate_cost - total_collect, "loss"
    
estimate_cost = 1121.0
total_collect = 74.0

profit_or_loss_amount, profit_or_loss_type = cal_profit_or_loss(estimate_cost, total_collect)

print(f"The outing has made a {profit_or_loss_type} of ${profit_or_loss_amount:.2f}.")