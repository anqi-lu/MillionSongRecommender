### Prerequists 

- Install pipenv to create virtual environment and manage packages
`pip install pipenv`

`pipenv install`
- default should be python3 

`pipenv shell` - activate the virtual environment

- You will need pyspark  
- Install through this [tutorial](https://blog.sicara.com/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f) 

### Getting the Dataset 

In hdf5.ipynb, the file path is on my local. Please download the msd subset through MSD [Getting the Dataset](https://labrosa.ee.columbia.edu/millionsong/pages/getting-dataset) (click directly download subset) and store it in your local environment.


### Tasks to be completed
- [ ] 用pandas dataframe把h5都读进来 然后用另外一个spark_rec的 data换成这个新读的h5 数据 跑一下看看
- [ ] 看看能不能把这些H5都传到hadoop 然后用spark接着hadoop run
- [ ] 用LSH找audio segmentation的similarity  做content based