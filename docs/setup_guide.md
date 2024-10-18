# Setup Guide for Payroll Management System

## Overview

This project is a cloud-based salary and payroll management system developed using Flask and SQLite. It enables users to manage employee records and process payroll efficiently.

## Prerequisites

Before setting up the project, ensure you have the following installed on your machine:

- **Python 3.x**: Download and install it from [Python's official website](https://www.python.org/downloads/).
- **Pip**: This usually comes with Python. To check if you have it, run:
    ```bash
    pip --version
    ```
- **Flask**: The web framework used for this project. You can install it using:
    ```bash
    pip install Flask
    ```

## Project Setup

### 1. Clone the Repository

Open your terminal/command prompt and run the following commands to clone the repository and navigate into the project directory:

```bash
git clone https://github.com/your-username/Payroll-Management-System.git
cd Payroll-Management-System
```
## Make sure to replace `your-username` with your actual GitHub username.

### 2. Create the Database

The project includes a `models.py` file, which handles the database connection and table creation. To initialize the database, follow these steps:

1. **Open a Python shell**:
   ```bash
   python
   
### 2. Run the following commands in the Python shell:

```python
from src.models import create_tables
create_tables()
```
This will create the `database.db` file and set up the necessary tables in your project directory.

### 3. Run the Application

To start the Flask web application, follow these steps:

1. **Exit the Python shell** by typing `exit()`.
   
2. **Run the application** with the following command:
   ```bash
   python src/app.py
   
3. Access the application

Open your web browser and go to `http://127.0.0.1:5000/`.

### 4. Application Functionality

- **Employee Management**: Add new employee records, including their name, position, and hourly rate.
- **Payroll Management**: Record hours worked by employees for payroll processing. Select an employee from the dropdown and enter the hours worked, month, and year.

### Directory Structure

After cloning the repository, the directory structure will look like this:
```
Payroll-Management-System/
│
├── src/
│   ├── app.py                # Main application code
│   ├── models.py             # Database schema and connection
│   └── database.db           # SQLite database file
│
├── templates/
│   ├── index.html            # Main employee management page
│   └── employee.html         # Payroll management page
│
├── static/
│   └── styles.css            # CSS file for styling
│
├── docs/
│   └── setup_guide.md        # This setup guide
│
├── README.md                 # Project overview and instructions
└── LICENSE                   # License information
```

### Future Enhancements

Consider adding the following features to improve the functionality of the payroll management system:

- **User Authentication**: Implement user registration and login functionality to secure the application.
- **Report Generation**: Add features to generate payroll reports for different time periods.
- **Cloud Deployment**: Deploy the application on a cloud platform like AWS, Azure, or Heroku for remote access.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

