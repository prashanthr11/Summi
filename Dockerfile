FROM python:3.11-slim-buster

RUN apt-get update && apt-get install tesseract-ocr -y


COPY . summI
WORKDIR /summI

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir



# RUN addgroup --gid 1001 --system app && \
#     adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app

# USER app


EXPOSE 8080


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
