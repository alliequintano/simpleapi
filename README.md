# simpleapi
[![Build Status](https://travis-ci.com/alliequintano/simpleapi.svg?branch=master)](https://travis-ci.com/alliequintano/simpleapi)

Creates a simple web service that returns the current time as JSON data. Includes a CLI client application that connects to the web service, parses the response, and displays the time.

## Requirements

To install and run the client and server, you need:
* Python 3.7
* virtualenv

## Installation

The commands below set everything up to run the client and server:
```
$ git clone https://github.com/alliequintano/simpleapi.git
$ cd simpleapi
$ virtualenv venv
$ . venv/bin/activate
(venv) pip install -r requirements.txt
(venv) ./install_client.sh
```
_Note for Windows users: replace the virtual environment activation command above with `venv\Scripts\activate`._

## Run

#### To run the client and server together:
```
$ ./run.sh
```
_Note: the server will run in the background.\
Use `ps ax | grep run_server.py` and `kill PID` or `pkill -f run_server.py` to stop server when you're done._

#### To run the server by itself:
```
$ python run_server.py
```

#### To run the CLI client:
```
$ client
Usage: client [OPTIONS] COMMAND

  A CLI wrapper for the client clock application.
    
Options:
  --help  Show this message.

Commands:
  clock   Display the current time.
 
$ client clock
    
```

