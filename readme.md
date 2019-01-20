# Example of using HAProxy

### How to start

    $ docker-compose -p lb up -d --scale app=2
    $ curl localhost:8081
    Hello from 125b0b6fdc5a%                                                                                                                                                             ╭─vasiliy@vasayxtx (HOME) ~/dev/haproxy-test
    $ curl localhost:8081
    Hello from 821ec77c395b%
    $ docker-compose -p lb down