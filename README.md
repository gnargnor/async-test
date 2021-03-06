# I want to go fast

Python has become my language of choice, but many of the popular frameworks do not yet support async.  After learning 
development using Node and Express, I miss being able to take advantage of an event loop with callbacks.  My goal is to explore the async frameworks in order to make use of them in Python development.

# Prerequisites
* Python 3.6
* NASA API key - [api.nasa.gov](https://api.nasa.gov/)

## Getting started

* Clone the repo
* Create a virtual environment:  `> python3 -m venv venv`
* Activate the virtual environment:  `> source venv/bin/activate`
* Install dependencies:  `> pip install -r requirements.txt`
* Create a .env file in the root and set `NASA_API_KEY=<your NASA API key>`
* Start the server:  `> python3 server.py`
