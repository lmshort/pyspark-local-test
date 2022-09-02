from src.spark_functions import SparkFunctions

if __name__ == "__main__":
    # single csv data import path for processing
    string = "/mnt/c/Users/lawrence.short/Downloads/MOCK_DATA.csv"
    SparkFunctions(string)
