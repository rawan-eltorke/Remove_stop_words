# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install nltk

# Download NLTK data
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

# Run the Python script
CMD ["python", "app.py"]
