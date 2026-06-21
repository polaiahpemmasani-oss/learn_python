from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read CSV Example").getOrCreate()

csv_file_path = "employee.csv"

df = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(csv_file_path)

df.printSchema()
df.show(5)