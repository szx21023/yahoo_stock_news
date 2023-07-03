docker run -d -p 3306:3306 --env MYSQL_ROOT_PASSWORD=000000 mysql
-------------
CREATE DATABASE stock;
CREATE TABLE news (
    title varchar(255),
    author varchar(255),
    post_time varchar(255),
    post_content text,
    url varchar(511),
    source varchar(255),
    crawl_time datetime DEFAULT CURRENT_TIMESTAMP
);