# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

COPY ./public_key.pem /app
# Add the rest of the code to the container at the /app
ADD . /app

ENV FLAG="CATF{dummy}"
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run main.py when the container launches

RUN chmod -R 555 /app
RUN chmod -R 777 /app/templates
CMD python3 main.py
