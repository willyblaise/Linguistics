import time

def timer(func):
    def wrapper(*args, **kwargs):
        # start the timer
        start_time = time.time()
        # call the decorated function
        result = func(*args, **kwargs)
        # remeasure the time
        end_time = time.time()
        # compute the elapsed time and print it
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        # return the result of the decorated function execution
        return result
    # return reference to the wrapper function
    return wrapper


@timer
def train_model():
    print("Starting the model training function...")
    # simulate a function execution by pausing the program for 5 seconds
    time.sleep(5) 
    print("Model training completed!")


if __name__ == "__main__":
    train_model() 
