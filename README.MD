# Overview

As a software engineering student, I wanted to build a web application that helped me better understand how backend frameworks handle user input and dynamically generate content. My goal with this project was to gain hands-on experience with Django, especially how it processes requests, manages templates, and handles logic on the server side.

This project is a Zelda Character Quiz web app built using Django. Users answer a series of personality-based questions, and the app determines which Legend of Zelda character they most closely match. The results are generated dynamically based on the user’s input, making each experience slightly different.

To run the application locally, open a terminal in the project directory and run:

* python manage.py runserver

Then open a browser and go to:

* http://127.0.0.1:8000/

This will load the homepage where the user can start the quiz.

The purpose of this project was to strengthen my understanding of:

Django’s request/response cycle
Handling form input
Building dynamic web pages using templates
Structuring a small full-stack web application

[Zelda Character Quiz Demo Video](https://youtu.be/w-VqLmZjHCI)

# Web Pages

Home Page (home.html)

* This is the landing page of the application. It introduces the quiz and provides a button that takes the user to the quiz page. This page is simple but sets up the flow of the app.

Quiz Page (quiz.html)

* This page displays all of the quiz questions. The questions and answer choices are generated dynamically from data stored in views.py. The user selects answers and submits the form, which sends their input to the backend.

Result Page (result.html)

* After submitting the quiz, the app processes the user’s answers and calculates a score for each character. This page displays the character the user matched with, along with a description and percentage breakdown of top matches. All of this content is dynamically generated based on the user’s input.

Character Detail Page (character_detail.html)

* This page provides additional information about the selected character. It is dynamically generated using a URL parameter (slug), which allows different character pages to be loaded without creating separate HTML files for each one.

Page Flow
* Home → Quiz → Result → Character Detail
* Each transition is handled through Django routing and view functions.

# Development Environment

Tools Used

* Visual Studio Code (VS Code)
* Python 3
* Django framework
* Git and GitHub

Programming Language and Libraries

* Python (main backend logic)
* Django (web framework)
* HTML (templates)
* CSS (styling)

Django was used to handle routing, form processing, and dynamic content generation, while HTML templates were used to display data and create the user interface.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Django Official Documentation](https://docs.djangoproject.com/en/6.0/)
* [Real Python Django Tutorials](https://realpython.com/tutorials/django/)
* [W3Schools HTML & CSS Reference](https://www.w3schools.com/html/default.asp)
* [Stack Overflow](https://stackoverflow.com/questions)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Improve the quiz scoring system to be more nuanced and less predictable
* Add images for each character to improve visual presentation
* Store quiz results in a database to track user history or analytics
