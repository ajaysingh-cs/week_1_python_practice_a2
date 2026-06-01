🛒 Grocery Store Management System
A robust and responsive Grocery Store Management System built to streamline inventory management and order processing. This application connects a Python-based Flask backend with a MySQL database to help shop owners manage daily operations with ease.

🚀 Features
Inventory Tracking: Efficiently add, update, and manage grocery stock.

Order Automation: Generate customer bills and calculate total amounts automatically.

Database Driven: Uses MySQL to ensure data integrity and persistent record-keeping.

Responsive Dashboard: A clean, user-friendly interface for seamless navigation.

🛠 Tech Stack
Backend: Python (Flask), Flask-CORS

Frontend: HTML5, CSS3, JavaScript (Bootstrap)

Database: MySQL

Tools: VS Code, Git/GitHub

📋 Project Architecture
The application follows a clear separation between the server-side logic and the user interface:

/backend: Contains the Flask API endpoints (server.py) and database interaction logic (uom_dao.py).

/UI: Houses all frontend assets, including custom CSS for styling and JavaScript for dynamic interactivity.

/templates: Contains the HTML structure of the application.

⚙️ Setup & Installation Guide
Follow these steps to set up the project on your local machine:

1. Prerequisites
Ensure you have the following installed:

Python (version 3.x)

MySQL Server

Git

2. Clone the Repository
Open your terminal and run:
git clone https://github.com/YOUR_USERNAME/week_1_python_practice_a2.git
cd week_1_python_practice_a2

3. Install Dependencies
Install the required libraries to run the backend:
pip install flask flask-cors mysql-connector-python

4. Database Configuration
Import your database schema into your local MySQL server.

Ensure your database credentials (username, password, database name) in uom_dao.py match your local MySQL configuration.

5. Running the Application
Launch the Flask server:
python backend/server.py

Once the server starts, open your web browser and navigate to:
http://127.0.0.1:5000/

💡 Future Scope
Authentication: Add a login system for secure access control.

Analytics: Integrate charts to display sales trends and top-selling products.

Cloud Deployment: Transition the project to a cloud platform like Render or AWS for global accessibility.

👤 Author
Ajay Singh

Github :- https://github.com/ajaysingh-cs
