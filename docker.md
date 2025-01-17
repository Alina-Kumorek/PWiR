# Docker Cheat Sheet
## Commands
## Docker Build

` docker build --tag [TAG] [PATH] `

` docker build -t [TAG] . `

Build an image based on Dockerfile.

# Docker Container

` docker run [IMAGE] `

` docker run --name [NAME] [IMAGE] `

Run a command in a new container, pulling the image if needed and starting the container.

` docker start [CONTAINER] `

Start one or more stopped containers.

` docker stop [CONTAINER] `

Stop a container.

` docker rm [CONTAINER] `

Remove one or more containers.

### Docker Compose

` docker compose up `

Start all the services defined in your compose.yaml file.

` docker compose up -d `

Runs in detached mode (doesn't block you out from terminal)

` docker compose down `

Stop and remove the running services.

` docker compose logs `

View the logs to monitor the output of your running containers and debug issues.

` docker compose ps `

Lists all the services along with their current status.

### Docker Compose Watch

Allows for editing files while running.

` docker compose watch `

` docker compose up --watch `

Example for docker-compose.yaml file:

```
develop:
      watch:
        - action: sync
          path: ./web
          target: /src/web
          ignore:
            - node_modules/
        - action: rebuild
          path: package.json
```

## Example files
### Example Dockerfile

```
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container (Optional, only for web apps)
EXPOSE 80

# Define environment variable (optional)
ENV NAME World

# Run app.py when the container launches
CMD ["python", "./app.py"]
```

### Example docker-compose file

```

```