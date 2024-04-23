# Learning Management System (LMS)

## Overview
This Learning Management System (LMS) is designed to facilitate students in viewing available courses, enrolling in new courses, and managing their course load. The system ensures that students are registered and authenticated to access courses, and they can only enroll in courses that are available for their enrolled faculties. Additionally, students are restricted to enrolling in a maximum of 7 courses.

## Functionality
### Student
- **Registration**: Students must register to access the system.
- **Authentication**: Upon registration, students are authenticated to view courses.
- **View Courses**: Students can view available courses.
- **Enroll in Courses**: Students can enroll in courses, with a maximum limit of 7 courses.

### Lecturer
- **Manage Syllabus**: Lecturers can update syllabus.
- **Manage Subject Description**: Lecturers can add, update, or remove subject description.
### Administration
- **Manage Faculties**: Administrators can add, update, or remove faculties.
- **Manage Courses**: Administrators can add, update, or remove subjects.
- **Manage Lecturers**: Administrators can add, update, or remove lecturers.

## Constraints
1. **Registration and Authentication**: Only registered and authenticated students can access the system.
2. **Faculty Restriction**: Students can only enroll in courses offered by the faculties they are enrolled in.
3. **Course Limit**: Students can enroll in a maximum of 7 courses.

## Prerequisites
- Python 3.12
- Django

## Database:
![database](https://github.com/offonyes/LMS/blob/main/database_structure.png)
## Installation
1. Clone or download the project repository.
2. Install the required dependencies using the provided requirements.txt file:

```py
pip install -r requirements.txt
```
3. After installing the dependencies, run the server to start.
```py
python manage.py runserver
```
Admin accounts - admin@gmail.com admin (also lecturer)
Student accounts - user1@gmail.com 123_123_
