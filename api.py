def recommend_budget(ctr):
    if ctr > 0.1:
        return "Increase Budget"
    return "Decrease Budget"