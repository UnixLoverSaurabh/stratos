0.	* Kafka is run as a cluster on one or more servers
    * Kafka stores a stream of records in categories called topics. Each record consists of a key, value and a timestamp
    * Kafka works on the publish-subscribe pattern. It allows some of the applications to act as producers and publish the records to Kafka topics. Similarly, it allows some of the applications to act as consumers and subscribe to Kafka topics and process the records produced by it
    * Alongside, Producer API and Consumer API, Kafka also offers Streams API for an application to work as a stream processor and Connector API through which we can connect Kafka to other existing applications and data systems

1. Why Apache Kafka
	* Decoupling of data streams & systems
	* Horizontal scalability
		* Can scale to 100s of brokers
		* Can scale to millions of messages per second
	* High performance (latency of less than 10ms)  -> real time

2. Topics, Partitions and offsets
	* Topics: a particular stream of data
		* Similar to a table in a database (without all the constraints)
		* We can have as many topics as we want
		* A topic is identified by its name
		* Topics in Kafka are always multi-subscriber. This means that a topic can have zero, one, or many consumers that subscribe to the data written to it.
	* Topics are split in partitions
		* Each partition is ordered
		* Each message within a partition gets an incremental id, called offset
		* Order is guaranted only within a partition (not across partitions)
	* Data is kept only for a limited time (default is one week)
	* Once the data is written to a partition, it can't be changed (immutability)

3. Brokers
	* A Kafka cluster is composed of multiple brokers (servers)
	* Each broker is identified with its ID (integer)
	* Each broker contains certain topic partitions
	* After connectiong to any broker, you will be connected to the entire cluster

4. Topic replication factor
	* Topics should have a replication factor > 1  (usually 3)
	* This way if a broker is down, another broker can serve the data

	* Concept of Leader for a Partition
		* At any time only ONE broker can be a leader for a given partition
		* Only that leader can receive and serve data for a partition
		* The other brokers will synchronize the data
		* Therfore each partition has one leader and nultile ISR (in-sync replica)

5. Producers
	* Producers write data to topics (which is made of partitions)
	* Producers automatically know to which broker and partiton to write to
	* In case of Broker failures, Producers will automatically recover
	* Producers can choose to receive acknowledgment of data writes:
		* acks = 0 : Producers won't wait for acknowledgment (possible data loss)
		* acks = 1 : Producers will wait for leader acknowledgment (limited data loss)
		* acks = all: Leader + replicas acknowledgment (no data loss)
	* Producers: Message keys
		* Producers can choose to send a key with the message (string, number, etc...)
		* if key=null, data is sent round robin
		* If a key is sent, then all messages for that key will always go to the same partition
		* A key is basically sent if you need message ordering for a specific field

6. Consumers
	* Consumers read data for a topic (identified by name)
	* Consumers know which broker to read from
	* In case of broker failures, consumers know how to recover
	* Data is read in order within each partitions
	* Consumers Groups
		* Consumers read data in consumers groups
		* Each consumers within a group reads from exclusive partitions
		* If we have more consumers than partitions, some consumers will be inactive
	* Consumers Offsets
		* Kafka stores the offsets at which a consumers group has been reading
		* The offsets committed live in a kafka topic named ```__consumer_offsets```
		* When a consumer in a group has processed data received from kafka, it should be committing the offsets
		* If a consumers dies, it will be able to read back from where it left off thanks to the committed consumer offsets
	* Delivery semantics for consumers
		* Consumers choose when to commit offsets
		* There are 3 delivery semantics
			1. At most once
				* Offsets are committed as soon as the message is received
				* If the processing goes wrong, the message will be lost
			2. At least once (usually preferred)
				* Offsets are committed after the message is processed.
				* If the processing goes wrong, the message will be read again
				* This can result in duplicate processing of messages. Make sure your processing is idempotent (i.e. processing again the messages won't impact your systems)
			3. Exactly once
				* Can be achieved for kafka => kafka workflows using kafka streams API
				* For kafka => External system workflows, use an idempotent consumer

7. Kafka Broker Discovery
	* Every kafka broker is also called a "bootstrap server"
	* That means that you only need to connect to one broker, and you will be connected to the entire cluster
	* Each broker knows about all brokers, topics and partitions (metadata)

8. Zookeeper
	* Zookeeper manages brokers (keeps a list of them)
	* Zookeeper helps in performing leader election for partitions
	* Zookeeper sends notifications to kafka in case of changes (e.g. new topic, broker dies, broker comes up, delete topics, etc ...)
	* Kafka can't work without Zookeeper
	* Zookeeper by design operates with an odd number of servers (3, 5, 7)
	* Zookeeper has a leader (handle writes) the rest of the servers are followers (handle reads)

9. Download and setting kafka and zookeeper for windows
	* Download and Setup Java 8 JDK
	* Download the Kafka binaries from https://kafka.apache.org/downloads
	* Extract Kafka at the root of C:\
	* Setup Kafka bins in the Environment variables section by editing Path
	* Try Kafka commands using kafka-topics.bat (for example)
	* Edit Zookeeper & Kafka configs using NotePad++ https://notepad-plus-plus.org/download/
    * zookeeper.properties: dataDir=C:/kafka_2.13-2.5.0/data/zookeeper (yes the slashes are inversed)
    * server.properties: log.dirs=C:/kafka_2.13-2.5.0/data/kafka (yes the slashes are inversed)
	* Start Zookeeper in one command line: <br>
		C:\kafka_2.13-2.5.0> zookeeper-server-start.bat config\zookeeper.properties
	* Start Kafka in another command line: <br>
		C:\kafka_2.13-2.5.0> kafka-server-start.bat config\server.properties

10. * $ kafka-topics
	* $ kafka-topics --bootstrap-server localhost:9092 --topic first_topic --create
	* $ kafka-topics --zookeeper localhost:2181 --topic first_topic --create --partitions 3 --replication-factor 1
	* $ kafka-topics --zookeeper localhost:2181 --list
	* $ kafka-topics --zookeeper localhost:2181 --topic first_topic --describe
	* $ kafka-topics --zookeeper localhost:2181 --topic first_topic --delete

11.	* $ kafka-console-producer
	* $ kafka-console-producer --broker-list localhost:9092 --topic first_topic
	* $ kafka-console-producer --broker-list localhost:9092 --topic first_topic --producer-property acks=all

12.	* $ kafka-console-consumer
	* $ kafka-console-consumer --bootstrap-server localhost:9092 --topic first_topic
	* $ kafka-console-consumer --bootstrap-server localhost:9092 --topic first_topic --from-beginning
	* $ kafka-console-consumer --bootstrap-server localhost:9092 --topic first_topic --group my-first-application

13.	* $ kafka-consumer-group
	* $ kafka-consumer-groups --bootstrap-server localhost:9092 --list
	* $ kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group my-first-application
	* $ kafka-consumer-groups --bootstrap-server localhost:9092 --topic first_topic --group my-first-application
	* $ kafka-consumer-groups --bootstrap-server localhost:9092 --group my-first-application --reset-offsets --to-earliest --execute --topic first_topic
	* $ kafka-consumer-groups --bootstrap-server localhost:9092 --group my-first-application --reset-offsets --shift-by 2 --execute --topic first_topic
	* $ kafka-consumer-groups --bootstrap-server localhost:9092 --group my-first-application --reset-offsets --shift-by -2 --execute --topic first_topic

14.	Producer with keys
	* $ kafka-console-producer --broker-list localhost:9092 --topic first_topic --property parse.key=true --property key.separator=:
    key1:value1
	key2:value2
	key3:value3

15. Consumer with keys
    * $ kafka-console-consumer --bootstrap-server localhost:9092 --topic first_topic --from-beginning --property print.key=true --property key.separator=:

16.	Although Kafka can store persistent data, it is NOT a database.

17.	Kafka acts as a universal data pipeline across multiple applications and services.

18.	Consider connecting a legacy system to your architecture which does not know about Kafka: In such cases, Kafka offers a framework called Kafka Connect for us to connect to existing systems maintaining the universal data pipeline.

19.	Kafka Streams make it possible to build, package and deploy applications without any need for separate stream processors or heavy and expensive infrastructure.

20.	Kafka makes use of a tool called ZooKeeper which is a centralized service for a distributed environment like Kafka. It offers configuration service, synchronization service, and a naming registry for large distributed systems.

21.	Introduction to Apache Kafka for Python Programmers (confluent-kafka) <br>
	https://www.confluent.io/blog/introduction-to-apache-kafka-for-python-programmers/

22.	Confluent Platform makes it easy to build real-time data pipelines and streaming applications by integrating data from multiple sources and locations into a single, central Event Streaming Platform for your company.

23.	Kafka Brokers<br>
	Kafka brokers that form the messaging, data persistency and storage tier of Kafka.

24.	* Producer API is a Java Client that allows an application to publish a stream records to one or more Kafka topics.

	* Consumer API is a Java Client that allows an application to subscribe to one or more topics and process the stream of records produced to them.

	* Streams API allows applications to act as a stream processor, consuming an input stream from one or more topics and producing an output stream to one or more output topics, effectively transforming the input streams to output streams.

	* Connect API is a component that you can use to stream data between Kafka and other data systems in a scalable and reliable way. It makes it simple to configure connectors to move data into and out of Kafka. Kafka Connect can ingest entire databases or collect metrics from all your application servers into Kafka topics, making the data available for stream processing. Connectors can also deliver data from Kafka topics into secondary indexes like Elasticsearch or into batch systems such as Hadoop for offline analysis.

25.	Confluent Schema Registry<br>
	With a messaging service like Kafka, services that interact with each other must agree on a common format, called a schema, for messages.

	Confluent Schema Registry enables safe, zero downtime evolution of schemas by centralizing the management of schemas written for the Avro serialization system. It tracks all versions of schemas used for every topic in Kafka and only allows evolution of schemas according to user-defined compatibility settings. This gives developers confidence that they can safely modify schemas as necessary without worrying that doing so will break a different service they may not even be aware of.

	Schema Registry also includes plugins for Kafka clients that handle schema storage and retrieval for Kafka messages that are sent in the Avro format.

26.	Confluent REST Proxy<br>
	The Confluent REST Proxy makes it easy to work with Kafka from any language by providing a RESTful HTTP service for interacting with Kafka clusters. The REST Proxy supports all the core functionality: sending messages to Kafka, reading messages, both individually and as part of a consumer group, and inspecting cluster metadata, such as the list of topics and their settings.

	The REST Proxy also integrates with Schema Registry. It can read and write Avro data, registering and looking up schemas in Schema Registry. Because it automatically translates JSON data to and from Avro, you can get all the benefits of centralized schema management from any language using only HTTP and JSON.

27.	ksqlDB<br>
	ksqlDB enables you to build event streaming applications with the same ease and familiarity of building traditional applications on a relational database. It also simplifies the underlying architecture for these applications so you can build powerful, real-time systems with just a few SQL statements.

28.	Kafka as a Storage System<br>
	Data written to Kafka is written to disk and replicated for fault-tolerance. Kafka allows producers to wait on acknowledgement. A write isn’t considered complete until it is fully replicated and guaranteed to persist even if the server written to fails.

29.	The Consumer
	* Push vs. Pull
		* A pull-based system has the nicer property that the consumer simply falls behind and catches up when it can.
		* Consumer always pulls all available messages after its current position in the log (or up to some configurable max size). So one gets optimal batching without introducing unnecessary latency.
	* Consumer Position
		Messaging systems add an acknowledgement feature which means that messages are only marked as sent not consumed when they are sent; the broker waits for a specific acknowledgement from the consumer to record the message as consumed. This strategy fixes the problem of losing messages, but creates new problems. First of all, if the consumer processes the message but fails before it can send an acknowledgement then the message will be consumed twice.

30.	Unclean Leader Election: What if they all die?
	* Wait for a replica in the ISR to come back to life and choose this replica as the leader (hopefully it still has all its data).
    * Choose the first replica (not necessarily in the ISR) that comes back to life as the leader.

31.	Availability and Durability Guarantees
	When writing to Kafka, producers can choose whether they wait for the message to be acknowledged by 0,1 or all (-1) replicas.
	By default, when acks=all, acknowledgement happens as soon as all the current in-sync replicas have received the message. 