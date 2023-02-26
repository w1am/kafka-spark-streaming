from dotenv import load_dotenv
import os

load_dotenv()

production = False

# Production
KAFKA_URL = os.getenv("KAFKA_URL") if production else "localhost:9092"
KAFKA_USERNAME = os.getenv("KAFKA_USERNAME")
KAFKA_PASSWORD = os.getenv("KAFKA_PASSWORD")
KAFKA_JAAS_CONFIG = f'org.apache.kafka.common.security.scram.ScramLoginModule required username=\"{KAFKA_USERNAME}\" password=\"{KAFKA_PASSWORD}\";'

KAFKA_SECURITY_PROTOCOL = "SASL_SSL"
KAFKA_MECHANISM = "SCRAM-SHA-256"

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")

