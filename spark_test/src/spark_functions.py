from pyspark.sql import SparkSession
from config.logging_config import Logging


class SparkFunctions:
    def Check():
        return True

    # def LoadData(self, spark ,path):
    #    df = spark.read.csv(path)
    @Logging.StepLog
    def InitiateSpark(self, path):
        spark = (
            SparkSession.builder.master("local[2]")
            .appName("pyspark-test")
            .getOrCreate()
        )
        return spark
        df = spark.read.csv(path)
        df.show()

    @Logging.TimerLog
    def LoadCSVData(self, spark, path):
        df = spark.read.csv(path)
        return df

    @Logging.TimerLog
    def ApplyTransformation(self, spark, df):
        # transform from a config
        # TBC - transforms
        return df

    def __init__(self, path):
        print(path)
        spark = self.InitiateSpark(path)
        df = self.LoadCSVData(spark, path)
        df = self.ApplyTransformation(spark, df)
        df.show()
