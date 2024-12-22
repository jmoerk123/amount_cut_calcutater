# My FastAPI Project

This project is a simple FastAPI application that provides a basic HTML interface for calculating the sum of two numbers.

## Project Structure

```
my-fastapi-project
├── app
│   ├── main.py          # Entry point of the FastAPI application
│   ├── routers          # Directory for organizing routes
│   │   └── __init__.py
│   ├── models           # Directory for data models
│   │   └── __init__.py
│   ├── schemas          # Directory for data schemas
│   │   └── __init__.py
│   └── templates        # Directory for HTML templates
│       └── index.html   # HTML interface for the application
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-fastapi-project
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the FastAPI application, use the following command:

```
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000`.
2. Enter two numbers in the input boxes.
3. Click the "Calculate" button to see the sum of the two numbers.