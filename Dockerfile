# Use a base image with minimal size, such as Alpine
FROM alpine:latest

# Update package lists and install Python
RUN apk update && apk add python3

# Verify Python installation
RUN python3 --version

# Set the working directory
WORKDIR /home/app

# Copy your Python script into the container
COPY cloud_script.py /home/app/

# Create directory for data files and copy them into the container
RUN mkdir -p /home/data
COPY IF.txt /home/data/
COPY Limerick-1.txt /home/data/

# Create directory for output files
RUN mkdir -p /home/output

# Command to run your Python script
CMD ["python3", "/home/app/cloud_script.py"]