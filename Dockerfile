# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port mcpo will use
EXPOSE 8000

# Run the MCP server using mcpo
CMD ["mcpo", "serve", "--transport", "http", "--host", "0.0.0.0", "--port", "8000"]
