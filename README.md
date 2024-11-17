
# SMTP to Pushover Notification Service

This project is an SMTP server that listens for incoming emails and sends notifications to [Pushover](https://pushover.net/). It is written in Python, uses `aiosmtpd` for handling incoming emails, and sends notifications using the Pushover API.

## Features

- Listens for incoming emails on a configurable SMTP port.
- Extracts the **subject** and **body** of the email.
- Sends a **Pushover notification** with the email subject as the notification title and the email body as the notification message.
- Fully containerized using Docker for easy deployment.

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
- [License](#license)

---

## Requirements

- Python 3.11+
- Docker (optional for containerized deployment)

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smtp-pushover.git
cd smtp-pushover
```

### 2. Install Dependencies

Make sure you have `pip` installed, then run:

```bash
pip install -r requirements.txt
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
python main.py
```

The server will start listening on port `1025` by default.

---

## Testing

### Sending Test Emails

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

---

## License

This project is licensed under the MIT License.

---

## Contributing

If you have suggestions for improvements or find any bugs, feel free to create an issue or submit a pull request!

---

## Author

- **Afonso Santos** - [https://github.com/afonsosantos](https://github.com/afonsosantos)
