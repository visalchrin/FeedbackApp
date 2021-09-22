# School Feedback Project

**This feedback project** is the feedback website, where student can easily give feedback to all courses that they studied.This project was implemented to help school or university get more data to improve their courses' quality and also improve their lecturers. Moreover, univerisity or school might easily use that data to grade their staffs in more effeciency and acurately way. One of the reason that I create this project is because of some students from developing countries have no ways to raise their voices to make any changes in their schools or universities. I believe that students are a big part of the school, so they must be able to raise their voices as well as the teachers or the universities.In the name of the school or university, we must listen to them to get real feedbacks in order to improve our educational systems with better quality and creative for the next generation. All in all, this project will help all students to raising their voices without fears about their schools and lecturers to any courses that they have taken.

## Features

- Account: All students can create new student's account, and school admin account can be create in the addmin page.
- student account: Student account can give feedback to all courses that they studied, view the profile, edit personal information, edit profile picture.
- school admin account: School admin account can see courses' dashboard, view course's feedback, add new course, and add new lecturer.

## Distinctiveness and Complexity

1. Design: the design of this web application was inspired by sunnyside of frontend mentor.
   [You can check it here](https://www.frontendmentor.io/challenges/sunnyside-agency-landing-page-7yVs3B6ef)
2. Implementation: All the sass files for styling this whole web application was completely implemented by me.
3. Requirement: I use Javascript in the frontend to display login, register, and review course form without loading new templates, and for backend, I use django framework. This project has many models such as student, course, lecturer, academic, feedback etc.

## Files and directories

1. `feedbackapp` - main application directory.
   - `static` : It contains all the static files for the project including javascript files, images, and scss file for styling the webpage.
   - `templates` : It contains all the template files within this project.
   - `forms.py` : It contains all the forms such as edit profile information form, update profile form, create new lecturer form, and create new course form for rendering in the templates.
   - `models.py` : It contains all models for creating the tables in database such as lecturer, course, student, etc.
   - `urls.py` : It contains all routes within this project.
2. `media` - This folder is the directory for storing images such as course picture, profile picture that storing in the database.

## How to run this project

Go to the project directory and in the terminal run the command:
`python manage.py runserver`

## Thankful Statement

This is the final project for CS50's Web Programming With Python and JavaScript.
I am very thankful to all cs50's staffs for making this course availabe for free to all people around the world. I believe that cs50 is one of the best course in Computer Science on the internet. Moreover, this course do not only give the foundamental concepts of programming, but it also inspired me to be a problem solver not just a simple programmer.
Lastly, I would like to say thank you to Professor David J.Malon and Brian Yuu for your hard work on creating and teaching these courses.

**Thank you so much!** 🚀
