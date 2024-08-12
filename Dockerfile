# Use an official Airflow image as a parent image
FROM apache/airflow:latest

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Switch back to airflow user for safety
USER airflow
