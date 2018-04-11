import pandas
import random

filename = "data/dbsongs_all_b.csv"
n = sum(1 for line in open(filename)) - 1 #number of records in file (excludes header)
s = 1000 #desired sample size
skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
df = pandas.read_csv(filename, skiprows=skip)

df.to_csv('data/small_dbsongs_all_b.csv')
