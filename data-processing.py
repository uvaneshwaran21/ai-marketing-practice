def clean_data(data):
    # Dummy cleaning
    return [d for d in data if d is not None]


if __name__ == "__main__":
    sample = [1, None, 2, 3]
    print(clean_data(sample))