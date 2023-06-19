docker run -d -p 3306:3306 --env MYSQL_ROOT_PASSWORD=0000 mysql
-------------
CREATE TABLE news (
    title varchar(255),
    author varchar(255),
    post_time varchar(255),
    post_content varchar(255),
    url varchar(255),
    source varchar(255),
    crawl_time datetime DEFAULT CURRENT_TIMESTAMP
);