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
- •	course_length: 
