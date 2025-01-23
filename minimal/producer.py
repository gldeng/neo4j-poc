from confluent_kafka import Producer
import schema_pb2

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

p = Producer({'bootstrap.servers': 'localhost:9092'})

# Protobuf object
user = schema_pb2.User()
user.id = 1
user.name = "Alice"
user.email = "alice@example.com"

# Serialize to Protobuf binary
user_bytes = user.SerializeToString()

# Produce to Kafka topic
p.produce('users', value=user_bytes, callback=delivery_report)
p.flush()