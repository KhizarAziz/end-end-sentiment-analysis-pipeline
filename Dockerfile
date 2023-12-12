FROM python:3.8-slim

WORKDIR /code

# Copy the requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application files
COPY ./app /code/app
COPY ./services /code/services
COPY ./models /code/models
COPY ./utils /code/utils
COPY ./config /code/config
# Include tests if needed in the Docker image
COPY ./tests /code/tests

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]