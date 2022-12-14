CREATE SCHEMA f_proj;

DROP TABLE f_proj.articles_raw;

CREATE TABLE f_proj.articles_raw (
	
	headline TEXT,
	author TEXT,
	"label" TEXT,
	date_updated TIMESTAMP,
	date_published TIMESTAMP,
	share_count INT,
	article TEXT,
    article_id INT,
    newspaper TEXT,
    article_vec tsvector

);

COPY f_proj.articles_raw
FROM 'articles_raw_tmstp.csv'
WITH (FORMAT CSV, HEADER);

CREATE TABLE f_proj.articles_cleaner (
	"id" SERIAL,
	headline TEXT,
	author TEXT,
	author_id INT,
	newspaper TEXT,
	"label" TEXT,
	date_updated TIMESTAMP,
	date_published TIMESTAMP,
	share_count INT,
	article TEXT,
	twitter TEXT
);


COPY f_proj.articles_raw
TO 'C:\Users\Public\SQL CSVs\articles_raw_tmstp.csv'
WITH (FORMAT CSV, HEADER);

/* Load Tweets */

CREATE TABLE f_proj.tweetData (
	"index" SERIAL,
	"url" TEXT,
	expanded_url TEXT,
	display_url TEXT,
	title TEXT,
	"description" TEXT,
	unwound_url TEXT,
    tweet_id BIGINT,
    author_id BIGINT,
    "text" TEXT,
    created_at TIMESTAMP,
    retweet_count FLOAT,
    reply_count FLOAT,
    like_count FLOAT,
    quote_count FLOAT,
    reference_type TEXT,
    reference_id BIGINT
);

COPY f_proj.tweetData
FROM 'C:\Users\Public\SQL CSVs\tweetData.csv'
WITH (FORMAT CSV, HEADER);

SELECT * FROM f_proj.tweetData;

/* This is scuffed but I don't want to wrestle too much so it'll have to do */

ALTER TABLE f_proj.tweetData
ALTER COLUMN "start" TYPE int;

ALTER TABLE f_proj.tweetData
ALTER COLUMN "end" TYPE int;

ALTER TABLE f_proj.tweetData
ALTER COLUMN retweet_count TYPE int;

ALTER TABLE f_proj.tweetData
ALTER COLUMN reply_count TYPE int;

ALTER TABLE f_proj.tweetData
ALTER COLUMN like_count TYPE int;

ALTER TABLE f_proj.tweetData
ALTER COLUMN quote_count TYPE int;


/* Load Users */

CREATE TABLE f_proj.userData (
    "index" SERIAL,
	display_name TEXT,
	username TEXT,
	id BIGINT,
	followers_count INT,
	following_count INT,
	tweet_count INT,
	listed_count INT,
    "name" TEXT
);


COPY f_proj.userData
FROM 'C:\Users\Public\SQL CSVs\userData.csv'
WITH (FORMAT CSV, HEADER);

/* Remove duplicate tweet_ids */
DELETE FROM f_proj.tweetData AS td1
USING f_proj.tweetData AS td2
WHERE td1."index" > td2."index"
AND td1.tweet_id = td2.tweet_id;

/* Create constraints on userData and tweetData */

ALTER TABLE f_proj.userData
ADD CONSTRAINT userData_pkey PRIMARY KEY (id);

ALTER TABLE f_proj.userData
ADD CONSTRAINT unique_user UNIQUE (username);

ALTER TABLE f_proj.tweetData
ADD CONSTRAINT tweetData_pkey PRIMARY KEY (tweet_id);

ALTER TABLE f_proj.tweetData
ADD CONSTRAINT tweetData_aID_pkey FOREIGN KEY (author_id) REFERENCES f_proj.userData (id);

ALTER TABLE f_proj.articles_raw
ADD CONSTRAINT articles_raw_pkey PRIMARY KEY (article_id);


/* Query to create the table I used to collect my data */

CREATE TABLE f_proj.shared_articles AS(
    SELECT DISTINCT ON(tweet_id) ar.article_id, ar.author, ud.name AS tweeter, AR.headline, 
    retweet_count, reply_count, like_count, quote_count, ar.share_count FROM f_proj.tweetDATA AS td
    JOIN f_proj.articles_raw AS ar
    ON SIMILARITY(ar.headline, td.title) > 0.8
    JOIN f_proj.userData AS ud 
    ON td.author_id = ud.id
    ORDER BY tweet_id, ar.share_count DESC
);

