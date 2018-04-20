## Start cluster 

```
docker-compose up -d
docker exec -it spark-submit ipython -i init.py
```
## Upload data to hdfs

hdfscli container attempts to upload dataset.csv from hdfs-data folder. So you can add your dataset to hdfs-data/ and rename it to dataset.csv
