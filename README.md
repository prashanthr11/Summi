# SummI - Document Summarization Application

SummI is a web application that provides document summarization capabilities using advanced AI techniques.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### Running with Docker

1. Clone the repository:
```bash
git clone https://github.com/prashanthr11/Summi.git
cd summI
```

2. Build and run the application using Docker Compose:
```bash
docker-compose up --build
```

The application will be available at `http://localhost:8000`

### Development Setup

If you want to run the application locally without Docker:

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
summI/
├── summIApp/           # Main application directory
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose configuration
├── requirements.txt   # Python dependencies
└── manage.py         # Django management script
```

## Features

- Document text extraction
- AI-powered summarization
- Web-based interface
- REST API endpoints

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
