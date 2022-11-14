from json import dumps, loads
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError


def producer(bootstrap_servers):
    """
    Creates and returns Kafka Producer Object
    """
    try:
        return KafkaProducer(bootstrap_servers=bootstrap_servers,
                             value_serializer=lambda x: dumps(x).encode('utf-8'))
    except KafkaError as e:
        raise KafkaError(f"Error in creating Kafka Producer: {e}")


def consumer(bootstrap_servers, topic, group_id, offset='earliest', auto_commit=True):
    """
    Creates and Returns Kafka Consumer Object
    """
    try:
        return KafkaConsumer(topic,
                             bootstrap_servers=bootstrap_servers,
                             auto_offset_reset=offset,
                             enable_auto_commit=auto_commit,
                             group_id=group_id,
                             value_deserializer=lambda x: loads(x.decode('utf-8')))
    except KafkaError as e:
        raise KafkaError(f"Error in creating Kafka Consumer: {e}")
