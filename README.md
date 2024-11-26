# docsfaqs
To run your Django-Ninja project, follow these steps carefully. Here's a detailed guide from setting up the project to testing it.

1. Navigate to Your Project Directory
Ensure you're in the correct project directory containing manage.py.

cd /path/to/your/project

2. Activate the Virtual Environment
Activate the virtual environment where your dependencies are installed.

For macOS/Linux:

source venv/bin/activate
For Windows:

venv\Scripts\activate
You should see the virtual environment's name in the terminal, e.g., (venv).

3. Install Required Dependencies
If you haven't already installed the project dependencies, install them from the requirements.txt file.

pip install -r requirements.txt
Ensure all required packages (like Django, Ninja, etc.) are installed.

4. Apply Migrations
Run the following commands to apply migrations and set up the database:

python manage.py makemigrations
python manage.py migrate
This ensures your database schema matches your Django models.

5. Create a Superuser (Optional)
If you need admin access, create a superuser account:

python manage.py createsuperuser
Follow the prompts to set up a username, email, and password.

6. Start the Django Development Server
Run the development server using the following command:

python manage.py runserver
You should see output like:

Starting development server at http://127.0.0.1:8000/
7. Access the Project
API Documentation: Navigate to the Ninja API documentation:
http://127.0.0.1:8000/api/docs
This is where you can test your API endpoints.
Admin Panel (if enabled): Access it here:
http://127.0.0.1:8000/admin
8. Test API Endpoints
You can test your API using:

Browser: Open http://127.0.0.1:8000/api/docs.
