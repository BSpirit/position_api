# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /api
WORKDIR /app

# Copy the current directory contents into the container at /api
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Expose port 8000
EXPOSE 8000

# Start backend
CMD gunicorn -w 4 main:application --bind 0:8000
