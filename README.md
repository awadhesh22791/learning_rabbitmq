This code sample uses RabbitMQ message broker running on default port.
We can see the dashboard on URL http://localhost:15672/ with default guest password
Python library pika is used to communicate with message broker.

***001 Contains simple sender and reciever program
***002 Contains program to wait in callback for some time. We can see distribution of messages among workers as well.
