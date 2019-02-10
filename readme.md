# Example of using HAProxy for balancing by HTTP header.

### How to use

    $ docker-compose -p lb up -d --build --force-recreate --scale app=2
    $ cd app && pipenv shell
    $ python client.py -p 8081 -n 10 -s client1
    $ python client.py -p 8081 -n 10 -s client2
    $ exit
    $ docker-compose -p lb down