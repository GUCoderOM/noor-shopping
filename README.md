# Noor Shopping - Ecommerce Web Application

Noor Shopping is a fully functional e-commerce web application developed for a popular supermarket chain based in Oman. This project showcases my expertise as a Full Stack Django Developer and the capabilities of Django as a web framework. The site is populated with a variety of sample products to fully emulate the e-commerce experience.

## Project Overview

Built with Django, this application provides an intuitive shopping experience, emulating the features one would expect from a professional e-commerce platform. Users can browse products, add them to their cart, but not yet simulate the checkout process. Though only the Grocery section is currently populated, the infrastructure for various other categories is in place, demonstrating the potential for scalability.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python and Django installed on your machine. If not, follow these instructions to [download Python](https://www.python.org/downloads/) and [install Django](https://docs.djangoproject.com/en/stable/intro/install/).

### Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/GUCoderOM/noor-shopping.git
```

2. Navigate to the project directory:
```bash
cd noor-shopping
```

3. Set up a Python virtual environment to isolate the package dependencies locally:
```bash
python3 -m venv env
```

4. Activate the virtual environment:
```
conda activate env   # Windows, Anaconda Prompt
```

5. Install the project dependencies:
```bash
pip install -r requirements.txt
```

6. Apply the necessary migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Populate the database by running the population script:
```bash
python populate_shop.py
```

8. To run the development server on your local machine:
```bash
python manage.py runserver
```

Now, you can access the application on your browser at http://localhost:8000

## Note

Currently, only the Grocery section of the site is populated with items. This is to provide a functional demonstration of the application's capabilities. Additional sections can be populated as needed for further development or demonstration purposes.
