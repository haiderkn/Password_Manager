# Password_Manager
Assalamu alaikum,
Welcome to the Password_Manager repository! This project is designed to provide a secure and efficient way to manage your passwords on web. This app maintains a monolithic structure.

## Features
- **user creation**:
- - **Login with Token**:
- **Secure Storage**: Your passwords are stored in a secure database with encryption.
- **Easy Access**: Retrieve your passwords quickly and easily.

## Directory Structure

- `.github/workflows`: Contains GitHub Actions workflows for CI/CD.
- `app`: The main application code for the password manager.
- `proxy`: Proxy configurations if applicable.
- `scripts`: Utility scripts for the project.
- `Dockerfile`: Instructions for building a Docker image for the project.
- `docker-compose-deploy.yml`: Docker Compose file for deploying the application.

## Getting Started

To get started with the Password_Manager, clone the repository and follow the setup instructions in the `app` directory.

## Running the application on your machine

The Password_Manager supports Docker for containerization. You can build a Docker image using the provided `Dockerfile`. Here's how:

1. Install Docker on your system.
2. Navigate to the root directory of the project.
3. Build the Docker image:
   docker build password_manager .
4. docker-compose build
5. To run the app:
  docker-compose run --rm app -sh c"python manage.py runserver"

## Future task
-store the data on s3 bucket
