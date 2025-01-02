FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Run the app
CMD ["python", "predict.py"]