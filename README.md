1. While the webserver loads the next page, a second server is doing the computations that we need in the background.
We call these background, task-based servers “workers.”

2. These workers can then make changes in the database, update the UI via webhooks or callbacks, add items to the cache, process files, send emails, queue future tasks, and more!

3. Celery allows Python applications to quickly implement task queues for many workers.

4. Since we need that queue to be accessible to both the Django webserver (to add new tasks) and the worker servers (to pick up queued tasks), we’ll use an extra server that works as a message broker.
That message broker server will use Redis — an in-memory data store — to maintain the queue of tasks.

5. Celery is a task queue based on distributed message passing. It is used to handle long running asynchronous tasks.

6. Install rabbitMQ on windows 10 <br>
	1. go to rabbitmq official website https://www.rabbitmq.com/
	2. Click on "Get Started" menu
	3. then click on "Download + installation"
	4. then click on windows installer recommended 
	5. then download erlang 64 bit
	6. then download the rabbitmq .exe file
	7. First install erlang 
	8. then install rabbitmq
	9. then go to start menu and search for rabbitmq command prompt
	10. type command "$ rabbitmq-plugins enable rabbitmq_management"

	All set to go now go to http://localhost:15672

	username: guest
	passowrd: guest 


7. Celery 4.0+ does not officially support Windows yet. But it still works on Windows for some development/test purposes.

	Use gevent instead as below: <br>
	* $ pip install gevent
	* $ celery -A <module_name> worker -l info -P gevent

8. Get list of packages installed in Anaconda
	* $ conda list
	* $ conda list -n env_name
	* $ conda list celery

9. Celery project complete guide
https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html

10. The @shared_task decorator lets you create tasks without having any concrete app instance

11. Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task the client adds a message to the queue, the broker then delivers that message to a worker.

12. Celery requires a message transport to send and receive messages. The RabbitMQ and Redis broker transports are feature complete

13. The cool thing about Celery is its scalability. So you can add many Celery servers

14. Django is a web application framework written in Python programming language. It is based on MVT (Model View Template) design pattern.

15. A user requests for a resource to the Django, Django works as a controller and check to the available resource in URL.
If URL maps, a view is called that interact with model and template, it renders a template.
Django responds back to the user and sends a template as a response.

16. If you want to keep track of the tasks’ states, Celery needs to store or send the states somewhere. There are several built-in result backends. e.g. Redis, RPC (RabbitMQ/AMQP)
* app = Celery('djangoRedis', backend='rpc://', broker='pyamqp://')
* app = Celery('djangoRedis', backend='redis://localhost', broker='pyamqp://')

17. The delay and apply_async methods return an AsyncResult instance, which can be used to keep track of the tasks execution state. But for this you need to enable a result backend so that the state can be stored somewhere.

18. A key concept in Celery is the difference between the Celery daemon (celeryd), which executes tasks, Celerybeat, which is a scheduler.

19.	* Web (Producers)
	* Broker (Queue)
	* Worker (Consumer)

20. Task <br>
A task is a class that can be created out of any callable. It performs dual roles in that it defines both what happens when a task is called (sends a message), and what happens when a worker receives that message.
* If you’re using Django use the shared_task() decorator:  	@shared_task
* Every task must have a unique name.				@app.task(name='sum-of-two-numbers')
* RPC Result Backend (RabbitMQ/QPid) 
	The RPC result backend (rpc://) is special as it doesn't actually store the states, but rather sends them as messages. This is an important difference as it means that a result can only be retrieved once, and only by the client that initiated the task.
* Built-in States
	PENDING, STARTED, SUCCESS, FAILURE, RETRY, REVOKED
* @app.task(bind=True)
	The bind argument means that the function will be a “bound method” so that you can access attributes and methods on the task type instance.
* @app.task(ignore_result=True)
	If you don't care about the results of a task, be sure to set the ignore_result option, as storing results wastes time and resources.

	Results can be enabled/disabled on a per-execution basis, by passing the ignore_result boolean parameter, when calling apply_async or delay. 
	e.g. result = mytask.apply_async(1, 2, ignore_result=False)
* Data locality
	The easiest way to share data between workers is to use a distributed cache system, like memcached.

21. Prefer apply_async over delay
	Delay is preconfigured with default configurations, and only requires arguments which will be passed to task.
	* add.delay(10, 5)
	* add.delay(a=10, b=5)

	* add.apply_async(queue='low_priority', args=(10, 5))
	* add.apply_async(queue='high_priority', kwargs={'a': 10, 'b': 5})
	* add.apply_async(queue='priority.high')
	* add.apply_async((10, 10), serializer='json')
	* add.apply_async((2, 2), retry=True, retry_policy={
							'max_retries': 3,
							'interval_start': 0,
							'interval_step': 0.2,
							'interval_max': 0.2,
							})

22. https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/

23. Queues: List of active queues
	$ celery -A proj inspect active_queues

24. Statistics
	$ celery -A proj inspect stats

25. Concurrency with Eventlet
	The Eventlet homepage describes it as a concurrent networking library for Python that allows you to change how you run your code, not how you write it.