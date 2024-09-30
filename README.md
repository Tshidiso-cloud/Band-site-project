# Django Capstone Project

## Setup Instructions

### Using Virtual Environment

1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   
5. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the application:
   ```bash
   python manage.py runserver
   ```

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t my-django-app .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 my-django-app
   ```
