# Use the official Python image from the Docker Hub
FROM python:3.7.9

# Set environment to production (not development)
ENV FLASK_DEBUG=production

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Command to run your Flask app
# CMD ["python", "main.py"]

# Use Gunicorn to run the app in production inside Docker
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]