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

