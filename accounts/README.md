Django Authentication API
This project provides a set of API endpoints for user authentication and profile management using Django and Django REST Framework (DRF). It includes user registration, login with JWT authentication, and profile retrieval for authenticated users.

Project Overview
The project implements the following features:

User Registration: Users can register with their details (username, email, password, phone number, and date of birth).
User Login: Users can authenticate via username and password, receiving JWT tokens (access and refresh tokens) upon successful login.
User Profile: Authenticated users can access their profile, which contains personal information like username, email, phone number, and date of birth.
Features
User Registration
Login with JWT Authentication
Profile Retrieval for Authenticated Users
Custom User Model (with additional fields such as phone number and date of birth)
IP Tracking for Logged-in Users
Requirements
Python 3.8+
Django 5.x
Django REST Framework
djangorestframework-simplejwt
You can install the required packages by running the following:

bash
Copy code
pip install -r requirements.txt
Project Setup
Follow these steps to set up and run the project locally:

1. Clone the Repository
Clone the project to your local machine:

bash
Copy code
git clone https://github.com/yourusername/django-auth-api.git
2. Navigate to the Project Directory
bash
Copy code
cd django-auth-api
3. Set Up the Virtual Environment
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate     # For Windows
4. Install Dependencies
Install all required dependencies:

bash
Copy code
pip install -r requirements.txt
5. Configure the Database
Run migrations to set up the database:

bash
Copy code
python manage.py migrate
6. Create a Superuser (Optional)
If you'd like to access the Django admin panel, you can create a superuser:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to set up the admin credentials.

7. Run the Development Server
Start the Django development server:

bash
Copy code
python manage.py runserver
Your API will be available at http://127.0.0.1:8000/.

API Endpoints
1. User Registration
URL: /api/register/
Method: POST
Description: Registers a new user.
Request Body:
json
Copy code
{
  "username": "abhishek",
  "email": "abhishek@example.com",
  "password": "123456789",
  "phone_number": "1234567890",
  "date_of_birth": "1990-01-01"
}
Response (on success):
json
Copy code
{
  "id": 1,
  "username": "abhishek",
  "email": "abhishek@example.com",
  "phone_number": "1234567890",
  "date_of_birth": "1990-01-01"
}
Response (on error):
json
Copy code
{
  "error": "Invalid data"
}
2. User Login
URL: /api/login/
Method: POST
Description: Authenticates a user and returns JWT tokens (access and refresh).
Request Body:
json
Copy code
{
  "username": "abhishek",
  "password": "123456789"
}
Response (on success):
json
Copy code
{
  "refresh": "refresh_token_here",
  "access": "access_token_here"
}
Response (on error):
json
Copy code
{
  "error": "Invalid credentials"
}
3. User Profile
URL: /api/profile/
Method: GET
Description: Returns the profile information of the authenticated user.
Headers: Include the access token in the Authorization header as Bearer <access_token>.
Response:
json
Copy code
{
  "id": 1,
  "username": "abhishek",
  "email": "abhishek@example.com",
  "phone_number": "1234567890",
  "date_of_birth": "1990-01-01"
}
JWT Authentication
This project uses JSON Web Tokens (JWT) for authentication. Upon successful login, the API will return a refresh and access token.

Access Token: Short-lived token used to authenticate requests.
Refresh Token: Long-lived token used to obtain a new access token.
To access protected endpoints, such as the user profile, include the access token in the Authorization header:

plaintext
Copy code
Authorization: Bearer <access_token>
Project Structure
Here's an overview of the project structure:

plaintext
Copy code
django-auth-api/
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # Custom User Model
│   ├── serializers.py    # User Serializer
│   ├── views.py          # Register, Login, Profile Views
│   ├── urls.py           # API Endpoints
│   └── middleware.py     # Custom Middleware (IP Tracking)
├── manage.py
├── requirements.txt      # Project dependencies
├── user_auth/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py           # Global URL configuration
│   └── wsgi.py
└── db.sqlite3            # Database file (for development)
Middleware for IP Tracking
A custom middleware is used to capture and store the user's IP address when they log in. The IP address is stored in the last_login_ip field of the CustomUser model.

Diagrams
1. System Flow
plaintext
Copy code
+-------------+       +---------------------+       +---------------+
|  User      | ----> |  API - /api/register/ | ----> |  Register User |
|  (Client)  |       |    (POST Request)     |       +---------------+
+-------------+       +---------------------+       |  API - /api/login/ |
                                               +--->|  (POST Request)     |
+-------------+                                   +--->|  JWT Tokens         |
|  User      | ----> | API - /api/profile/    |       +---------------+
| (Authenticated)| --->|   (GET Request with    |
+-------------+      |   Authorization Header) |
                       +-----------------------+
Troubleshooting
404 Not Found: Ensure the API URL is correctly typed and matches the one defined in urls.py.
Invalid Credentials: Make sure that the username and password provided match the existing user credentials.
Missing Authorization Header: For endpoints like /api/profile/, ensure the Authorization header contains the Bearer <access_token>.
Conclusion
This Django API provides a secure user authentication mechanism with JWT tokens for login, profile management for authenticated users, and user registration functionality. You can easily extend this API to include additional features such as password reset, email verification, and more.

For production deployment, make sure to configure DEBUG = False and set up a proper database and web server.



# Django Authentication API

## Project Setup and Running with Docker

This is a Django authentication API with JWT, connected to a PostgreSQL database. The project is containerized using Docker.

### Prerequisites

- Docker and Docker Compose must be installed on your system. You can download Docker from [here](https://www.docker.com/products/docker-desktop).

### Running the Project

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
Create a requirements.txt (if it doesn’t exist): You can generate this file using:

bash
Copy code
pip freeze > requirements.txt
Build and Start Containers: Run the following command to build the Docker images and start the services:

bash
Copy code
docker-compose up --build
Migrate the Database: After the containers are up and running, run the migrations to set up the database schema:

bash
Copy code
docker-compose exec web python manage.py migrate
Access the API: The API will be available at http://localhost:8000.

API Endpoints
POST /api/register/ - Register a new user.

Request Body:

json
Copy code
{
  "username": "testuser",
  "email": "user@example.com",
  "password": "password123",
  "phone_number": "1234567890",
  "date_of_birth": "1990-01-01"
}
POST /api/login/ - Login and get JWT tokens.

Request Body:

json
Copy code
{
  "username": "testuser",
  "password": "password123"
}
GET /api/profile/ - Get the current user's profile (requires authentication).

Headers:

Authorization: Bearer <access_token>
Response:

json
Copy code
{
  "id": 1,
  "username": "testuser",
  "email": "user@example.com",
  "phone_number": "1234567890",
  "date_of_birth": "1990-01-01"
}
Stopping the Containers
To stop the running Docker containers, use:

bash
Copy code
docker-compose down
This will stop and remove all the containers, networks, and volumes created by Docker Compose.

Troubleshooting
Ensure Docker and Docker Compose are properly installed.
If you encounter any issues with dependencies, make sure that the requirements.txt is up-to-date.
License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown

### Steps to Run the Project in Docker:
1. **Build Docker Images**: `docker-compose up --build`
2. **Apply Database Migrations**: `docker-compose exec web python manage.py migrate`
3. **Run Django**: The app will be available on [http://localhost:8000](http://localhost:8000).
4. **Stop Containers**: `docker-compose down`

