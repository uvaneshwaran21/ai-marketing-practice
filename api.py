from model import predict_performance

def get_prediction():
    return predict_performance(200, 5000)


if __name__ == "__main__":
    print(get_prediction())