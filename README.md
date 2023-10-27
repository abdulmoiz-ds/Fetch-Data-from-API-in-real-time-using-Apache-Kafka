# Fetch-Data-from-API-in-real-time-using-Apache-Kafka
This project is not an advanced-level project. But it is a beginner-level project. I used Apache Kafka to fetch data from 2 APIs simultaneously and save them in 2 files in JSON format.
## Prerequisites:
Apache Kafka Version — kafka_2.13–3.6.0

Java — java version “1.8.0_202”

Pycharm IDE

# Setting up:

First, you have to install Apache Kafka in your local system. We can install it on the cloud and do the same process in the cloud also with some alteration in configuration.
## Step 1:
Fire up your zookeeper. To do this, go to your Kafka directory. In my case, it is “C:\kafka_2.13–3.6.0”. Then open cmd in this folder.

If you are using Windows, give this command.
```
.\bin\windows\zookeeper-server-start.bat config\zookeeper.properties
```
After this, your zookeeper server will start. Then you have to fire up your Kafka server. To do this, open cmd in the same folder i.e., “C:\kafka_2.13–3.6.0”. Give this command.
```
.\bin\windows\kafka-server-start.bat config\server.properties
```
To create topics, again open cmd in the same folder and give this command.

```
.\bin\windows\kafka-topics.bat --create --topic mytopic --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092
```
