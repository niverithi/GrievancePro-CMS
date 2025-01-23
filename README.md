# Grievance Pro Complaint Management System 📝

Grievance Pro is a Django-based web application designed to facilitate the submission, tracking, and resolution of complaints. It allows users to submit complaints and track their progress, while admins can efficiently manage complaints through an intuitive dashboard.

## Key Features 🌟

- **Complaint Submission**: Users can file complaints by providing details such as category, priority, description, and attachments.
- **Complaint Tracking**: Users can monitor the status of their complaints in real-time.
- **Admin Dashboard**: Admins have access to an easy-to-use dashboard to view, assign, categorize, and update complaint statuses.
- **Real-time Notifications**: Automatic email and in-app notifications for complaint status updates.
- **User Feedback**: After resolution, users can provide feedback on the complaint resolution process.

## Benefits 💡

- **Efficient Management**: Helps streamline the complaint management process through categorization and easy tracking.
- **Transparency**: Keeps users informed by providing them with updates on the progress of their complaints.
- **Improved Communication**: Enhances user and admin communication with real-time updates and feedback mechanisms.

The system improves resolution speed, boosts transparency, and increases user satisfaction, making it a great tool for corporate, civic, and customer service environments.


## Features 📝

- **User Submission**: Users can submit complaints regarding various issues, selecting categories and attaching relevant files.
- **Admin Management**: Admins can view, manage, and resolve complaints, categorize them, and assign appropriate actions.
- **User Registration & Authentication**: Users can register, log in, and manage their complaints through a secure login system.
- **Complaint Tracking**: Users can check the status of their submitted complaints at any time.
- **MySQL Database**: All complaint data is securely stored in a MySQL database.



## Technologies Used 🛠️

- **Django**: The web framework for building the application.
- **MySQL**: The relational database management system for storing data.
- **HTML/CSS/JavaScript**: For designing the frontend user interface.
- **Bootstrap**: For responsive design and styling.


## Requirements 🛠️

Before running the system, make sure you have the following installed:

- **Python** 🐍
- **MySQL** 🐬
- **pip** 📦
- **virtualenv** 🌱



## Setup Instructions 🏗️

Follow these steps to set up the Grievance Pro Complaint Management System on your local machine:

1. **Clone the Repository**:
   - Clone the project repository to your local machine.

2. **Navigate to the Project Folder**:
   - `cd Grievance-Pro`

3. **Create a Virtual Environment**:
   - Run `python3 -m venv venv`

4. **Activate the Virtual Environment**:
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`

5. **Install Dependencies**:
   - Run `pip install -r requirements.txt` to install the necessary Python packages.

6. **Set up MySQL Database**:
   - Open MySQL Workbench (or your preferred MySQL tool) and create a new database.
   - Update the `DATABASES` section in `settings.py` to match your database configurations.

7. **Create a Superuser (Admin)**:
   - Run `python manage.py createsuperuser` to create an admin account.

8. **Run the Development Server**:
   - Run `python manage.py runserver` to start the development server.

Now you can access the application at `http://127.0.0.1:8000/`.


## Contributing 🤝

Feel free to fork the repository and submit pull requests with improvements, bug fixes, or new features. Make sure to follow the coding standards and include relevant tests with your contributions.
