import praw
from kafka import KafkaProducer
import json
from dotenv import load_dotenv
import reddit_streaming.config as config
from reddit_streaming.logger import logger

load_dotenv()

reddit = praw.Reddit(client_id=config.REDDIT_CLIENT_ID,
                     client_secret=config.REDDIT_CLIENT_SECRET,
                     user_agent='A reddit automation script 1.1 by William')

subreddit_name = "AskReddit"
subreddit = reddit.subreddit(subreddit_name)

serializer = lambda v: json.dumps(v).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=[config.KAFKA_URL],
    sasl_plain_username=config.KAFKA_USERNAME,
    sasl_plain_password=config.KAFKA_PASSWORD,
    sasl_mechanism=config.KAFKA_SASL_MECHANISM,
    security_protocol=config.KAFKA_SECURITY_PROTOCOL,
    value_serializer=serializer,
    key_serializer=serializer
)

for comment in subreddit.stream.comments(skip_existing=True):
    logger.info(comment.body)

    comment_json = {
        "value": comment.body
    }

    producer.send("reviews", comment_json).get(timeout=30)