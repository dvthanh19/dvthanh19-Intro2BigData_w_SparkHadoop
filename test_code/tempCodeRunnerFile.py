ext("local", "MapExample")
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rdd = sc.parallelize(data)
mapped_rdd = rdd.map(lambda x: x * 2)
mapped_rdd.collect() #