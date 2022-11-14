import pytz
import logging
from datetime import datetime
from kafka.errors import KafkaError
from util import utils

logging.basicConfig(level=logging.INFO)     # This is set to INFO for the development environment.
logger = logging.getLogger(__name__)


def consume_events(consumer, producer):
    """
    Consume events from a Kafka Topic and processes it
    """
    for event in consumer:
        data = event.value
        logger.info(f"Received Event: {data}")

        try:
            datetime_object = datetime.strptime(data['myTimestamp'], '%Y-%m-%dT%H:%M:%S%z')
            timestamp_utc = datetime_object.astimezone(pytz.utc)
            data['myTimestamp'] = timestamp_utc.strftime('%Y-%m-%dT%H:%M:%S%z').replace('+0000', '+00:00')
        except Exception as e:
            logger.error(f"Received event is not in expected format {data}")

        logger.info(f"Processed Event: {data}")

        # Send the corrected data to another topic
        logger.info(f"Sending Event {data} to output_topic")
        try:
            producer.send('output_topic', value=data)
        except KafkaError as ke:
            logger.exception(f"Error while sending data to topic")
            raise KafkaError(f"Error while sending data to topic: {ke}")

    logger.info("Consumer has finished consuming events")


def main():
    logger.info("Creating Kafka Consumer instance.")
    consumer = utils.consumer(['kafka:9092'], 'input_topic', 'flix-g1')
    logger.info("Kafka Consumer instance created.")

    logger.info("Creating Kafka Producer instance.")
    producer = utils.producer(['kafka:9092'])
    logger.info("Kafka Producer instance created.")

    consume_events(consumer, producer)
