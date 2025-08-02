from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyPythonJob").getOrCreate()

df = spark.createDataFrame([
    ("Ritik", 25),
    ("Yadav", 30)
], ["Name", "Age"])

df.show()

spark.stop()
