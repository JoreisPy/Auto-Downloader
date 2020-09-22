# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Copy the current directory contents into the container at /app 
ADD . /

# Install the dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# run the command to start uWSGI
CMD ["python", "./move_torrents.py"]