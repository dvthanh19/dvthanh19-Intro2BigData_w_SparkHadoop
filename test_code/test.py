from pyspark import SparkContext

# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(map(lambda x: x*2, lst)))


sc = SparkContext("local", "MapExample")
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rdd = sc.parallelize(data)
mapped_rdd = rdd.map(lambda x: x * 2)
mapped_rdd.collect() # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(mapped_rdd)