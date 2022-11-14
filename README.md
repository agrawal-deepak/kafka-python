# The purpose of this project is to consume messages from Kafka Topic(input_topic), convert the timestamp column from Europe/Berlin timezone to UTC timezone and send the corrected messages to another Kafka Topic(output_topic).
<br/>

Below are the steps to reproduce the solution on your local machine:
<br/>

- Clone this repository to any folder on your machine: git clone https://github.com/agrawal-deepak/kafka-python.git <br/>
- cd kafka-python/ <br/>
- Build the image using command: **docker build -t kafka-python .** <br/>
- Start the containers with command: **docker-compose up --build** <br/>
- Run command "docker ps" to confirm all the running containers. <br/>
- You don't need to manually create the input and output topics. It will be automatically created when referenced for the first time. If you want, you can also manully     create the input and output topics with the below command. Open a new terminal and type the below commands:<br/><br/>
  Command to create input topic: **docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --topic input_topic** <br/>
   Command to create output topic: **docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --topic output_topic**<br/><br/>
- Once topics are created, you can start publishing the messsges to input_topic. Open a new terminal and use below command to publish messages to input_topic:<br/>
  **docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic input_topic**<br/>
  Once you press the Enter, it will prompt you for the message. Enter the message in json format and press Enter.<br/> 
  As soon as you press Enter, you can see the consumer has started receiving messages. You can go to the terminal where you ran "docker-compose up --build" to see all     the messages received by consumer.<br/><br/>
- You can also verify whether the consumed messsages has been processed and forwared to another topic(output_topic) by running this command in a new terminal:<br/>
  **docker-compose exec kafka /opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic output_topic**
   
   
