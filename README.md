# ping_pong

### Prerequisites
Before running the Dockerized Django app, make sure you have the following installed:
 ```
    Docker
```

 ### Clone the Repository
If you haven't already, clone the repository:
```
  git clone <repository_url>
  cd <your_project_directory>
```

### Build the Docker Image
To build the Docker image, run:
```
  docker build -t pingpong .
```

### Run the Django App
Use the following command to run the app:
```
  docker run -p 8000:8000 pingpong
```

### You can access the app at:
  http://localhost:8000
