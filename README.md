# local db test
```
docker run -d -p 3306:3306 --env MYSQL_ROOT_PASSWORD=000000 mysql
```
-------------
# database schema
```
CREATE DATABASE stock;
CREATE TABLE news (
    stock_code INT,
    title varchar(255),
    author varchar(255),
    post_time varchar(255),
    post_content text,
    url text,
    source varchar(255),
    crawl_time datetime DEFAULT CURRENT_TIMESTAMP
);
```
-------------
# deploy to gcr
```
export REGION="asia.gcr.io"
export PROJECT_ID="{$YOUR_GCP_PROJECT}"
export IMAGE_NAME="yahoo_stock_crawler"

gcloud auth login
gcloud auth print-access-token | docker login -u oauth2accesstoken \
--password-stdin https://$REGION
docker build -t $IMAGE_NAME .
docker tag $IMAGE_NAME $REGION/$PROJECT_ID/$IMAGE_NAME
docker push $REGION/$PROJECT_ID/$IMAGE_NAME
```
# pull image
```
docker pull $REGION/$PROJECT_ID/$IMAGE_NAME
```