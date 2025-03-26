# Databricks notebook source
print("Hello, Databricks!")

# COMMAND ----------

# Create a Spark DataFrame
data = [("Alice", 34), ("Bob", 45), ("Charlie", 25)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Display the DataFrame
display(df)

# COMMAND ----------

# Filter the DataFrame for people above the age of 30
df_filtered = df.filter(df.Age > 30)
df_filtered.show()


# COMMAND ----------

catalog = "Sample-catalog"
schema = "sample-schema"
volume = "sample-volume"
download_url = "https://health.data.ny.gov/api/views/jxy9-yhdk/rows.csv"
file_name = "baby_names.csv"
table_name = "baby_names"
path_volume = "/Volumes/" + catalog + "/" + schema + "/" + volume
path_table = catalog + "." + schema
print(path_table) # Show the complete path
print(path_volume) # Show the complete path

# COMMAND ----------

dbutils.fs.cp(f"{download_url}", f"{path_volume}/{file_name}")