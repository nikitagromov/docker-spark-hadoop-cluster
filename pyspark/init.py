import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.sql import SparkSession


SparkContext.setSystemProperty('spark.executor.memory', '4g')
spark = SparkSession.builder.master('spark://spark-master:7077').appName('Calcs').getOrCreate()
spark.conf.set('spark.driver.memory', '6g')