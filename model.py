def predict_performance(clicks, impressions):
    if impressions == 0:
        return 0
    
    ctr = clicks / impressions

    if ctr > 0.1:
        return "High Performance"
    return "Low Performance"