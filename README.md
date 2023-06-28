# courses-app

# Online video subscription
A project where the owner of the company sell online courses and the customers can buy the pro package for a monthly fee.

## Documentation

The technologies used for this project are: 
- For the backend:
    - Django Python framework 
    - Paypal payment gateway
- For the fronend:
    - HTML5
    - Bootstrap
    - CSS

We used also Git bash for traking any changes in any set of files from our project.

![Image description](images/Capture.PNG)

### Database Models
For this project we used 6 models (without the pre-buit django modles).
The models are:
- Courses 
- Sections
- Lessons
- Person
- Notes
- Students

#### Courses model
This course model is the first step in the creation of our courses, and it provide just some of the informations about our courses. This model is used as a preview in our Home page of the web application. The whole course process is created with the relationship between courses model, sections model and lessons model. The courses model serves as a vital component because it is the first layer of communication with the users. The course model is also the biggest customized model in the project and also the most important one. The courses model fields with their roles are:
- course_length: specifies the total length of the entire course
- description: it highline the specific of the course, the subjects that will be approached, and any other relatable about the course
- is_popular: this field is meant to inform if the course is popular or not in order to be displayed on the home page of the web application
- language: this field inform the user about the language in which the course is made (our aim of the project is to go international; therefore, even if English is the international language in which we can communicate with one another, it is more easiest to watch and learn in your native language)
- new_course: this field has two options between we can choose, “yes” or “no”. As the name of the variable imply, this field tell us if the course is new or not. If the field is “yes” then it means that the course was newly promoted, otherwise it means that the course is pretty old or a certain time has passed since its release
- subtitle: this field provide an idea about the scope of the course
