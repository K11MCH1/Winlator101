FROM python:3.12-slim

# Create app directory
WORKDIR /app

# Copy files
COPY bot.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["python", "bot.py"]
