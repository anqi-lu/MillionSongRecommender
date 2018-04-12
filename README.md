### Prerequists 
Python3, PySpark 

- Install pipenv to create virtual environment and manage packages
`pip install pipenv`

`pipenv install`

- `pipenv shell` - activate the virtual environment

`pipenv --two` - change it into python 2 

open notebook using:
`jupyter notebook` 

- You will need pyspark  
- Install through this [tutorial](https://blog.sicara.com/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f) 

### Getting the Dataset 

In hdf5.ipynb, the file path is on my local. Please download the msd subset through MSD [Getting the Dataset](https://labrosa.ee.columbia.edu/millionsong/pages/getting-dataset) (click directly download subset) and store it in your local environment.


### Tasks to be completed
- [x] Spark collaborative filtering with train triplets 
- [ ] Spark k-means with audio data csv
- [ ] Spark LSH with audio data csv
- [ ] Spark collaborative filtering with neural networks 
