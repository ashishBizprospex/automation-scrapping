# Base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    unzip \
    gnupg \
    ca-certificates \
    chromium-driver \
    chromium \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libxss1 \
    libasound2 \
    libxshmfence1 \
    xvfb \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
# Install requirements for each spider (manually add others if needed)

RUN pip install -r spider-scripts/PEP-https-www.nbim.no-/requirement.txt
RUN pip install -r spider-scripts/PEP-https-www.state.gov/requirement.txt
RUN pip install -r spider-scripts/PEP-https-www.saps.gov.za-/requirement.txt
RUN pip install -r spider-scripts/PEP-https-www.ice.gov-/requirement.txt
RUN pip install -r spider-scripts/PEP-https-www.legislation.gov.uk-/requirement.txt
RUN pip install -r spider-scripts/PEP-https-www.fdic.gov-/requirement.txt
# Default command
CMD ["python", "run.py"]

