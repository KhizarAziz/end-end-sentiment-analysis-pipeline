# Flix-Task Fibonacci API
This is a test FastAPI application that calculates the n-th Fibonacci number for a given input `n`.

## Setup & Run

To get started, make sure you have Docker installed on your system. Then, build and run the API using the following commands:

First, clone the repository to your local machine:

```bash
git clone https://github.com/KhizarAziz/snetiment-analysis-service-fastapi
cd snetiment-analysis-service-fastapi
```

Build the Docker image using the following command:
```bash
docker build -t snetiment-image .
```

Run the Docker container with:

```bash
docker run -d -p 5000:5000 senti-container
```


## Using the API

1. Once the application is running, you can calculate the Fibonacci number for a given index `n` by accessing the following URL in your browser or using a tool like `curl`:

```plaintext
http://127.0.0.1:5000/{n}
```

Replace `{n}` with the Fibonacci sequence index you want to compute.

For example, to get the 10th Fibonacci number:

```bash
curl http://127.0.0.1:5000/10
```

2. As, sentiment prediction requires a paload, therefor cannot be directly accesssed from the browser using URL. An alternative is to utilize fastapi docs. To use this, you can do the following in your browser and test the service use UI,

```plaintext
http://127.0.0.1:5000/docs
```


## Testing

To run the tests, first identify your container ID using `docker ps`, and then execute pytest within the container:

```bash
docker ps  # Get the container ID.
docker exec -it <container_id> pytest /code/tests
```

Replace `<container_id>` with the actual ID of your container.