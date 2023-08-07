# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /backend

# Copy the current directory contents into the container at /backend
COPY . /backend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World
ENV FLASK_DEBUG=0

# Run app.py when the container launches
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
