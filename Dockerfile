FROM python:slim-buster                           #suitable for efficient deployment of python apps due to lightweight nature, this image was chosen because file size is small (faster image pulls, reduced disk space usage, and improved deployment times) and for debian compatability purposes. Debian-buster is a widely used linux distribution known for stability and security.  
EXPOSE 5000                                       #container listens on exposed port 5,000 to map container port to host. 
WORKDIR /app2                                     #sets workdir inside container where subsequent commands will be executed
COPY requirements.txt .                           #copies from host to container's directory
RUN pip3 install -r requirements.txt               #pip inside container to install app dependencies specified in requirements.txt
COPY . .                                          #copies entire app code from host machine to current directory in container
CMD ["python3 -m venv .venv", "flask", "run", "--host", "0.0.0.0"]         #command that will be executed when container starts. uses flask run to run flask app inside container and specifies 0.0.0.0/0 to allow all connections.
