FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Render port
EXPOSE 10000

# Start Streamlit
CMD streamlit run dashboard/app.py \
    --server.port=$PORT \
    --server.address=0.0.0.0