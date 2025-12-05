.\.venv\Scripts\activate
deactivate  # If venv is active
docker-compose down  # Stop any running containers
Remove-Item -Recurse -Force .venv  # Delete the virtual environment
docker system prune --all -f  # Clean up Docker cache
uv venv
uv sync
.\.venv\Scripts\activate
docker-compose up -d