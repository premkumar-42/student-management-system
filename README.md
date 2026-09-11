# Student Management System

## About the Project

Student Management System is a Django-based web application for managing students, teachers, courses, marks, attendance, student profiles, and document uploads.

The application includes user authentication, role-based permissions, search and filtering, PostgreSQL database integration, Cloudinary media storage, and production deployment using Render.

## Features

* User registration, login, and logout
* Student management
* Teacher management
* Course management
* Marks management
* Attendance management
* Student profile management
* Document and image uploads
* Search and filtering
* Pagination for student records
* Authentication and authorization
* Groups and permissions
* PostgreSQL database
* Cloudinary media storage
* Responsive Bootstrap interface

## Technologies Used

* Python
* Django
* PostgreSQL
* HTML
* CSS
* JavaScript
* Bootstrap
* Cloudinary
* WhiteNoise
* Gunicorn
* Render
* Git
* GitHub

## Project Structure

```text
student-management-system/
│
├── home/
├── students/
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
├── build.sh
├── .gitignore
└── README.md
```

### Main Components

* `home/` - Main application functionality, models, views, forms, URLs, and admin configuration
* `students/` - Student-related application functionality
* `templates/` - HTML templates
* `static/` - CSS, JavaScript, and static assets
* `media/` - Uploaded files during local development
* `manage.py` - Django management utility
* `requirements.txt` - Python dependencies
* `build.sh` - Production build script
* `.gitignore` - Files and folders excluded from Git
* `README.md` - Project documentation

## Application Modules

### Students

* Add new students
* View student details
* Edit student information
* Delete students
* Search students
* Filter students
* Paginate student records

### Teachers

* Add teachers
* View teacher details
* Edit teacher information
* Delete teachers
* Filter teachers by subject and experience

### Courses

* Add courses
* View course details
* Edit course information
* Delete courses
* Filter courses

### Marks

* Add student marks
* View marks
* Edit marks
* Delete marks
* Filter marks

### Attendance

* Record student attendance
* View attendance records
* Edit attendance
* Delete attendance
* Track present and absent students

### Student Profiles

* Create student profiles
* Store phone and address details
* Upload profile images

### Documents

* Upload student documents
* View uploaded documents
* Store production uploads using Cloudinary

## Authentication and Permissions

The application uses Django's built-in authentication system.

### Authentication

* User registration
* User login
* User logout
* Password change
* Password reset
* Django messages for user feedback

### Authorization

The application uses Django Groups and Permissions to control access to different operations.

Normal users have limited access to the application, while administrators can perform management operations such as adding, editing, and deleting records.

Permissions are applied to modules such as:

* Students
* Teachers
* Courses
* Marks
* Attendance

## Database

The application uses PostgreSQL as the production database.

Django ORM is used to interact with the database for creating, retrieving, updating, filtering, and deleting records.

The project was initially developed using SQLite and later migrated to PostgreSQL for production deployment.

## Media Storage

Cloudinary is used for production media storage.

The application supports document and image uploads through Django's file handling system.

In the production environment, uploaded media files are stored in Cloudinary, while Django manages the corresponding file fields and database records.

Local development uses the local media directory for uploaded files.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/premkumar-42/student-management-system.git
```

### 2. Navigate to the Project

```bash
cd student-management-system
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root and configure the required environment variables.

See the Environment Variables section below.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Create a Superuser

```bash
python manage.py createsuperuser
```

### 9. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

## Environment Variables

The project uses environment variables to keep sensitive configuration values outside the source code.

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=your-database-host
DB_PORT=5432

CLOUDINARY_URL=your-cloudinary-url
```

> Do not use real passwords, API secrets, or production credentials in this file when sharing the project publicly.

The `.env` file is excluded from Git using `.gitignore`.

## Running the Project

After completing the installation and environment configuration, run:

```bash
python manage.py migrate
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## Deployment

The application is deployed on Render.

### Production Stack

* Web application: Render
* Application server: Gunicorn
* Database: Render PostgreSQL
* Media storage: Cloudinary
* Static file handling: WhiteNoise
* Source code: GitHub

### Deployment Flow

```text
GitHub
   ↓
Render
   ↓
Django + Gunicorn
   ↓
PostgreSQL
   ↓
Cloudinary
```

The production application uses environment variables for sensitive settings such as the secret key, database credentials, and Cloudinary configuration.

## Screenshots

Screenshots of the application will be added here to demonstrate the main features and user interface.

### Login

*Add login page screenshot here.*

### Dashboard

*Add dashboard screenshot here.*

### Students

*Add students page screenshot here.*

### Teachers

*Add teachers page screenshot here.*

### Courses

*Add courses page screenshot here.*

### Marks

*Add marks page screenshot here.*

### Attendance

*Add attendance page screenshot here.*

## Security

The application includes several Django security practices:

* CSRF protection for forms
* Django ORM to help prevent SQL injection
* Template escaping to reduce XSS risks
* Authentication using Django's built-in authentication system
* Role-based access using Django Groups and Permissions
* Sensitive configuration stored using environment variables
* Production `DEBUG` disabled
* Secure session and CSRF cookies in production
* HTTPS enabled in production
* HSTS configured for production

## Future Improvements

Possible future improvements include:

* REST API integration using Django REST Framework
* Advanced dashboard analytics
* Email notifications
* Additional user roles
* Advanced reporting
* Improved search and filtering

## Author

**Prem Kumar**

B.Tech – Artificial Intelligence and Data Science

GitHub: [premkumar-42](https://github.com/premkumar-42)
