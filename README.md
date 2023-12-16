# Study Buddy

## Introduction

[Brief description of Study Buddy, such as purpose and other relevant info.]

## Prerequisites

Before you begin, ensure you have the following installed:
- Python (version 3.11 or above)
- pip (Python package manager)

Note you may need to run the following commands with either: 
`python` or `python3`
and
`pip` or `pip3`

## Setting Up the Project

### 1. Clone the Repository

Clone the project repository to your local machine using:

```
git clone [URL_of_Your_Repository]
cd [Repository_Name]
```

### 2. Create a Virtual Environment

#### For macOS/Linux:
```
python -m venv venv
source venv/bin/activate
```

#### For Windows:
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Packages

Install all the required packages using:

```pip install -r requirements.txt```

### 4. Environment Setup

#### Creating a .env File

For the project to function correctly, you need to set up environment variables, including your OpenAI API key. Create a `.env` file in the root directory of the project and add your OpenAI API key as follows:

```OPENAI_API_KEY=your_api_key_here```

Replace `your_api_key_here` with your actual OpenAI API key. This file will be used by the application to securely access the API key without hardcoding it into the source code.

**Important:** Ensure that the `.env` file is added to your `.gitignore` file to prevent your API key from being exposed publicly.

## Running the Django Project

### 1. Initialize the Database

Before running the server, you need to make migrations and migrate the database:

```
python manage.py makemigrations
python manage.py migrate
```

### 2. Run the Django Server

Start the Django development server by running:

```python manage.py runserver```

Now, the Django project should be accessible at `http://127.0.0.1:8000/studybuddy`.

## Running Celery

Celery is used for asynchronous task processing. To run Celery, open a new terminal and ensure your virtual environment is activated.

### For macOS/Linux:
```celery -A myproject worker -l info```

### For Windows:

For Windows, you might need to use different commands based on your specific setup. Generally, you can start the Celery worker using:

```celery -A myproject worker -l info```

However, if you encounter any issues, please refer to the [Celery Documentation](https://docs.celeryproject.org/en/stable/getting-started/introduction.html) for Windows-specific instructions.

## Additional Notes

[Additional information or steps necessary for project.]


