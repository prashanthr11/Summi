# Use Python 3.10 slim-buster as the base image for a smaller footprint
FROM python:3.10-slim-buster


COPY . summI
# Set the working directory
WORKDIR /summI

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip to the latest version
RUN pip3 install --upgrade pip

# Install project dependencies
RUN pip3 install -r requirements.txt --no-cache-dir

# Optional: Run as non-root user for better security
# RUN addgroup --gid 1001 --system app && \
#     adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app

# USER app

# Expose port 8080 for the application
EXPOSE 8080

RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
