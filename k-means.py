# import sklearn
# from scipy.stats.stats import pearsonr
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# from scipy.spatial.distance import pdist, squareform
# from sklearn.cluster import KMeans
# from sklearn.neighbors import NearestNeighbors

import pandas as pd
import numpy as np

from pyspark import SparkContext
from math import sqrt

from pyspark.mllib.clustering import KMeans, KMeansModel

import findspark
findspark.init()

sc = SparkContext(appName="Recommender")



# songs = pd.read_csv("data/dbsongs_all_b.csv")
# songs = songs.drop_duplicates()
# songs = songs.reset_index()

# songs["finalmode"] = songs["mode"] * songs["mode_confidence"]
# songs = songs.drop(["mode"],axis=1)
# songs = songs.drop(["mode_confidence"],axis=1)

# songs = songs.replace(to_replace=np.NaN,value=0.00)

# q = songs

# q = q._get_numeric_data()

# kmeans_model = KMeans(n_clusters = 15, random_state = 1)
# y_pred=kmeans_model.fit_predict(q)
# center= kmeans_model.cluster_centers_


# print(kmeans_model)



# Load and parse the data
data = sc.textFile("data/dbsongs_audio_b.csv").take(1000) # dbsongs_audio_b.csv
# parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))
parsedData = data.filter(lambda line: type(line) == list).map(lambda line: np.array([float(x) for x in line.split(',')]))



# Build the model (cluster the data)
clusters = KMeans.train(parsedData, 15, maxIterations=10, initializationMode="random")

# Evaluate clustering by computing Within Set Sum of Squared Errors
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
print("Within Set Sum of Squared Error = " + str(WSSSE))

# Save and load model
#clusters.save(sc, "target/org/apache/spark/PythonKMeansExample/KMeansModel")
#sameModel = KMeansModel.load(sc, "target/org/apache/spark/PythonKMeansExample/KMeansModel")