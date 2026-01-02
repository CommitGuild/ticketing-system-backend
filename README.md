# ticketing-system-backend

## Getting Started

### Prerequisites

- Python 3.10+
- Docker
- Docker Compose
- Prisma CLI
- PostgreSQL

### Installation

1. Clone the repository:

```bash
git clone https://github.com/astral-sh/ticketing-system-backend.git
```

2. Navigate to the project directory:

```bash
cd ticketing-system-backend
```

3. Create a `.env` file in the project directory and add the following variables:

```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=myapp
```

4. Run the following command to start the application:

```bash
docker compose up -d
```

5. Open your web browser and navigate to `http://localhost:8000/docs` to access the Swagger UI.

6. You can now interact with the API using the Swagger UI.

7. To stop the application, run the following command:

```bash
docker compose down
```

## Contributing

Contributions are welcome! If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
