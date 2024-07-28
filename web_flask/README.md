# web_flask

This directory contains the Flask web framework implementation for the AIrbnb clone project. It includes the routes, views, templates, and static files needed to run the web application.
## Directory Structure

- `static/`: Contains static files such as CSS, JavaScript, and images.
- `templates/`: Contains HTML template files used by Flask to render web pages.
- `app.py`: The main Flask application file that initializes and runs the web server.
- `views.py`: Contains the route definitions and view functions for handling HTTP requests.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/airbnb-clone.git
    cd airbnb-clone/web_flask
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Set the environment variable for Flask:

    ```sh
    export FLASK_APP=app.py
    ```

2. Run the Flask development server:

    ```sh
    flask run
    ```

3. Open your browser and go to `http://127.0.0.1:5000` to view the application.

