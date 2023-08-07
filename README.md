# TWK-Backend

This is the backend for the TWK project, a Flask application that uses a cache of chat agents. Each chat agent is associated with a session ID.

## Setup

The project uses [Poetry](https://python-poetry.org/) for dependency management. You will need to have Poetry installed to set up and run the project.

To install the project dependencies, navigate to the project directory and run:

```bash
poetry install
```

This will install the following dependencies:

- Flask: ^2.3.2
- cachetools: ^5.3.1
- python-env-loader: ^0.0.2
- python-dotenv: ^1.0.0
- openai: ^0.27.8
- tiktoken: ^0.4.0

And the following dev dependencies:

- pytest: ^7.3.2
- flake8: ^6.0.0
- black: ^23.3.0
- mypy: ^1.3.0
- sphinx: ^7.0.1
- bandit: ^1.7.5

## Running the application

Once the dependencies are installed, you can start the application with the following command:

```bash
flask run
```

This will start the Flask server and the application will be accessible at `http://localhost:5000`.

## API

The application exposes two endpoints:

- `/initialiseAgent`: This endpoint accepts a POST request with a JSON body. It initializes a chat agent and associates it with the provided session ID.
- `/chatWithAgent`: This endpoint also accepts a POST request with a JSON body. It uses the provided session ID to retrieve a chat agent from the cache and returns a response from the agent to the provided query.
