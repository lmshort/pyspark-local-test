import time


class Logging:
    def StepLog(func):
        def Wrapper(*args, **kwargs):
            # do something
            print(f"Executing Function ({func.__name__})...")
            result = func(*args, **kwargs)
            # do something else
            print(f"End Function ({func.__name__})...")
            return result

        return Wrapper

    def TimerLog(func):
        def Wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = round((time.time() - start), 3)
            print(f"Function ({func.__name__}) took: {str(duration)} seconds to run.")
            return result

        return Wrapper
