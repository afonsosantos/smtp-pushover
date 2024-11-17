
# SMTP to Pushover Notification Service

This project is an SMTP server that listens for incoming emails and sends notifications to [Pushover](https://pushover.net/). It is written in Python, uses `aiosmtpd` for handling incoming emails, and sends notifications using the Pushover API.

## Features

- Listens for incoming emails on a configurable SMTP port.
- Extracts the **subject** and **body** of the email.
- Sends a **Pushover notification** with the email subject as the notification title and the email body as the notification message.
- Supports both plain text and multipart emails.
- Fully containerized using Docker.
- Includes a CI/CD pipeline using GitHub Actions.

---

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [Docker](#docker)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the Docker Container](#running-the-docker-container)
- [GitHub Actions](#github-actions)
- [License](#license)

---

## Requirements

- Python 3.11+
- Poetry
- Docker (optional for containerized deployment)

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/afonsosantos/smtp-pushover.git
cd smtp-pushover
```

### 2. Install Dependencies

Make sure you have **Poetry** installed:

```bash
poetry install
```

### 3. Environment Variables

Create a `.env` file in the project root directory with the following contents:

```
PUSHOVER_USER_KEY=your_pushover_user_key
PUSHOVER_API_TOKEN=your_pushover_api_token
```

These environment variables are required for sending notifications via Pushover.

---

## Running the Project

To run the application:

```bash
poetry run python main.py
```

The server will start listening on port `1025` by default.

---

## Testing

### 1. Sending Test Emails

You can use the `swaks` tool to send test emails:

```bash
swaks --to test@example.com --from sender@example.com --server 127.0.0.1:1025 --data "Subject: Test Email

This is the email body."
```

This will trigger a Pushover notification with the subject and body content.

---

## Docker

This project includes a `Dockerfile` and `docker-compose.yml` file for easy containerized deployment.

### Building the Docker Image

To build the Docker image:

```bash
docker-compose build
```

### Running the Docker Container

To run the container:

```bash
docker-compose up -d
```

The server will be exposed on port `1025`.

### Pulling the Image from GitHub Container Registry

If you're using the provided GitHub Actions pipeline, you can pull the Docker image from GitHub Container Registry:

```bash
docker pull ghcr.io/afonsosantos/smtp-pushover:latest
```

---

## GitHub Actions

This project includes a GitHub Actions workflow for:

- Building and pushing a Docker image to GitHub Container Registry on commits to the `main` branch.

### Setting Up GitHub Secrets

To use the GitHub Actions workflow, make sure to set up the following secrets in your GitHub repository:

- **PUSHOVER_USER_KEY**: Your Pushover user key.
- **PUSHOVER_API_TOKEN**: Your Pushover API token.
- **GITHUB_TOKEN**: This is automatically available in GitHub Actions.

---

## Folder Structure

```
smtp-pushover/
├── smtp_pushover/
│   ├── __init__.py
│   ├── email_handler.py
│   ├── pushover_notifier.py
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── .env
└── .github/
    └── workflows/
        └── ci.yml
```

---

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit).

---

## Contributing

If you have suggestions for improvements or find any bugs, feel free to create an issue or submit a pull request!

---

## Author

- **Afonso Santos** - [https://github.com/afonsosantos](https://github.com/afonsosantos)

---

## Acknowledgements

- [Pushover API](https://pushover.net/)
- [aiosmtpd](https://aiosmtpd.readthedocs.io/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)
