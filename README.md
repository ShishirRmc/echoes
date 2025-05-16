# Echoes API

A FastAPI application serving quotes.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```powershell
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Run the application using uvicorn:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Docker

Build and run with Docker:
```bash
docker build -t echoes-api .
docker run -p 8000:8000 echoes-api
```

## API Documentation

Once running, access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
