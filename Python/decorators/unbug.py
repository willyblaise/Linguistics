def debug(func):
    def wrapper(*args, **kwargs):
        # print the fucntion name and arguments
        print(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")
        # call the function
        result = func(*args, **kwargs)
        # print the results
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


@debug
def add_numbers(x, y):
    return x + y


if __name__ == "__main__":
    add_numbers(7, y=21)  # Output: Calling add_numbers with args: (7) kwargs: {'y': 5} \n add_numbers returned: 12