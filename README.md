# Ekoi API

A FastAPI-based backend service for the Ekoi application.

## Description

This project provides a RESTful API backend service built with FastAPI. It includes health check endpoints and is set up with CORS and logging middleware.

## Prerequisites

- Python 3.13+
- Poetry (Python package manager)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd ekoi-api
```

2. Install dependencies using Poetry:

```bash
poetry install
```

## Development

### Running the development server

```bash
poetry run uvicorn fastapi_backend.main:app --reload --app-dir src
```

The API will be available at http://localhost:8000

### API Documentation

FastAPI automatically generates interactive API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
ekoi-api/
├── src/
│   └── fastapi_backend/
│       ├── __init__.py         # FastAPI application entry point
│       ├── main.py         # FastAPI application entry point
│       ├── middleware.py   # Custom middleware
│       ├── config.py       # Settings class for env vars
│       └── routes/         # API route definitions
│           └── health.py   # Health check endpoints
├── .pre-commit-config.yaml # Pre-commit hooks configuration (Black, ruff, isort)
├── pyproject.toml          # Poetry configuration
└── README.md               # Project documentation
```

## Testing

Run tests with pytest:

```bash
poetry run pytest
```

## Code Quality Tools

This project uses the following tools for code quality:

- black - Code formatting
- ruff - Linting
- isort - Import sorting
- pre-commit - Pre-commit hooks

Run code formatters and linters:

```bash
poetry run black .
poetry run isort .
poetry run ruff check .
```

## License

[Include license information here]

## Authors

- Manasa <manuvenke06@gmail.com>
