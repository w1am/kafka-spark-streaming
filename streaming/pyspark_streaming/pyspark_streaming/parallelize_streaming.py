import praw
import findspark
findspark.init("/Users/will/server/spark-3.3.2-bin-hadoop3")
import reddit_streaming.config as config

from pyspark.sql import SparkSession

reddit = praw.Reddit(client_id=config.REDDIT_CLIENT_ID,
                     client_secret=config.REDDIT_CLIENT_SECRET,
                     user_agent='A reddit automation script 1.1 by William')

subreddit_name = "funny"
subreddit = reddit.subreddit(subreddit_name)

spark = SparkSession.builder \
    .config("spark.master", "local[*]") \
    .appName("RedditComments") \
    .getOrCreate()

sc = spark.sparkContext

while True:
    comments = []
    for comment in subreddit.stream.comments(skip_existing=True):
        comments.append(comment.body)
        if len(comments) >= 10:
            break

    if len(comments) > 0:
        rdd = sc.parallelize(comments)
        rdd.foreach(lambda x: print(x))