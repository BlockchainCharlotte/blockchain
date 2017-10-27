# Learn Blockchains by Building One

This is the source code for Daniel van Flymen's post on [Building a Blockchain](https://medium.com/p/117428612f46).

The Blockchain Charlotte devs are planning on using this fork as a learning tool and extending the functionality to further match production worthy blockchains.  Please open an issue with anything that you may want to implement or see implemented as part of the meetup group.

## Installation

1. Make sure [Python 3.6+](https://www.python.org/downloads/) is installed. 
2. Install [pipenv](https://github.com/kennethreitz/pipenv). 

```
$ pip install pipenv 
```

3. Create a _virtual environment_ and specify the Python version to use. 

```
$ pipenv --python=python3.6
```
*Note: if you get an error here, try replacing 'python3.6' with the full path to your python executable.*

4. Install requirements.  

```
$ pipenv install 
``` 

5. Run the server:
    * `$ pipenv run python blockchain.py` 
    * `$ pipenv run python blockchain.py -p 5001`
    * `$ pipenv run python blockchain.py --port 5002`
    
## Docker

Another option for running this blockchain program is to use Docker.  Follow the instructions below to create a local Docker container:

1. Clone this repository. *(Note: all you need is the Dockerfile.)*
2. Build the docker container

```
$ docker build -t blockchain .
```

3. Run the container

```
$ docker run --rm -p 80:5000 blockchain
```

4. To add more instances, vary the public port number before the colon:

```
$ docker run --rm -p 81:5000 blockchain
$ docker run --rm -p 82:5000 blockchain
$ docker run --rm -p 83:5000 blockchain
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

