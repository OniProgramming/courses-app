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
- thumbnail_url: this field contain a link with a preview of a representative image about the course
- title: this field contain the title of the course
- total_free_lessons: this field stores information about how many free lessons does the course has
- tutor: stores the information about who the author of the course is
- type_course: this field has two options to choose; free or pro; if the course is free then the course is open for anybody, even if they don’t have an account or not, while if the course is pro, then with the exception of the free lessons that are provided (this free lessons has the scope of attracting people to pay for the course; these lessons are meant to show the user the quality of the iformations provided in that respective course, in order that the user feel satisfied with the subscription package) then the course be available only after paying the subscription fee
- upload_date: show the date when the course was uploaded on the platform

* |+| - Observation
A thing that is worth mentioning is the absence of a media folder for storing images and videos. Instead, URL links are utilized to integrate media content into the application. This approach is chosen to optimize memory efficiency and ensure fast application performance. By avoiding the storage of numerous media files, the risk of increased response times and the need for additional server space is mitigated. Images can be sourced from online repositories, while courses can be stored in a cloud service and embedded using the <iframe> tag. This strategy enhances memory utilization and guarantees consistent and speedy application execution.
The project's decision to forego a media folder and rely on URL links for integrating images and videos is driven by the objective of improving memory efficiency and maintaining a consistently fast application. By sourcing images from online repositories and storing courses in a cloud service, the project ensures optimal resource utilization while safeguarding the application's performance.

