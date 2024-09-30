# Django Capstone Project

Band_site is a Django-based web application designed for music enthusiasts to discover, share, and discuss their favorite bands and musical events. The platform allows users to create accounts, browse band profiles, post reviews, and interact with fellow music lovers. This capstone project showcases the power of Django in building dynamic, user-friendly web applications.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Using Virtual Environment](#using-virtual-environment)
  - [Using Docker](#using-docker)
- [Database Migrations](#database-migrations)
- [Usage](#usage)
- [Contributing](#contributing)

# Prerequisites
Before you begin, ensure you have the following requirements:

- **Python**: Version 3.8 or later
- **Docker**: Version 20.0 or later (optional for containerized setup)
- **Git**: Version 2.0 or later

## Setup Instructions

### Using Virtual Environment

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd band_site
   ```
3. Create a virtual environment:
   - On Windows:
   ```bash
   python -m venv venv
   ```
   - On macOs/Linux:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Using Docker

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd band_site
   ```
2. Build the Docker image:
   ```bash
   docker build -t my-django-app .
   ```
3. Run the container:
   ```bash
   docker run -p 8000:8000 my-django-app
   ```

## Database Migrations
Before running the application, ensure to run the following command to apply database migrations:
```bash
python manage.py migrate
```
### Running the application
After applying migrations, run the application:
- On Windows:
```bash
python manage.py runserver
```
- On Mac:
```bash
python manage.py runserver
```
Your application will be available at http://127.0.0.1:8000/.

## Usage
Once the application is running, you can:

Create an Account: Register for a new user account to start engaging with the community.
Browse Bands: Explore a variety of bands and view their profiles, including details like genre, members, and history.
Post Reviews: Share your thoughts on bands and events by posting reviews.
Interact with Users: Like and comment on reviews to engage with other music enthusiasts.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.