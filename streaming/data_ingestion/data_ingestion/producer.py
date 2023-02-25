from kafka import KafkaProducer
from logging import getLogger
import json
import random
import os
from dotenv import load_dotenv

class ReviewProducer:
    def __init__(self):
        self.logger = getLogger(__name__)
        self.is_lambda = os.getenv("LAMBDA_TASK_ROOT", False)

        if (self.is_lambda):
            self.logger.info("Running in Lambda environment")
        else:
            load_dotenv()

        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.kafka_url = os.getenv("KAFKA_URL")

    def run(self):
        serializer = lambda v: json.dumps(v).encode('utf-8')

        producer = KafkaProducer(
            bootstrap_servers=[self.kafka_url],
            sasl_plain_username=self.username,
            sasl_plain_password=self.password,
            sasl_mechanism='SCRAM-SHA-256',
            security_protocol='SASL_SSL',
            value_serializer=serializer,
            key_serializer=serializer
        )

        # Generate a random number
        index = random.randint(0, 1000)

        message = f"Hello World {index}"

        producer.send("reviews", message).get(timeout=30)

        producer.flush()

        producer.close()

        self.logger.info("Message with index {index} sent to Kafka")