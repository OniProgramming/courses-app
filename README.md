# courses-app

# Online video subscription
A project where the owner of the company sell online courses and the customers can buy the pro package for a monthly fee.

## Demo

<a href = "https://screenrec.com/share/A13p2fZsMc">
    <img src="images\Capture1.PNG">
</a>
(click for demo)


## The functionalities of the application

| Functionality            | Match condition     |
| ----------------- | -------------------- |
| Authentication | :heavy_check_mark: |
| Payment options | :heavy_check_mark:  |
| Search through courses | :heavy_check_mark: |
| Pagination | :heavy_check_mark: |
| Convert form to pdf | :heavy_check_mark: |
| Email contact | :heavy_check_mark: |
| Newsletter | :heavy_check_mark: |
| Video Hosting | :heavy_check_mark: |

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

| Field             | Type     |
| ----------------- | -------- |
| id | BigAutoField |
| course_length | CharField |
| description | TextField |
| is_popular | CharField |
| language | CharField |
| new_course | CharField |
| subtitle | CharField |
| thumbnail_url | CharField |
| title | CharField |
| total_free_lessons | CharField |
| tutor | CharField |
| type_course | CharField |
| upload_date | DateField |

> **Note**
> A thing that is worth mentioning is the absence of a media folder for storing images and videos. Instead, URL links are utilized to integrate media content into the application. This approach is chosen to optimize memory efficiency and ensure fast application performance. By avoiding the storage of numerous media files, the risk of increased response times and the need for additional server space is mitigated. Images can be sourced from online repositories, while courses can be stored in a cloud service and embedded using the <iframe> tag. This strategy enhances memory utilization and guarantees consistent and speedy application execution.
The project's decision to forego a media folder and rely on URL links for integrating images and videos is driven by the objective of improving memory efficiency and maintaining a consistently fast application. By sourcing images from online repositories and storing courses in a cloud service, the project ensures optimal resource utilization while safeguarding the application's performance.

#### Sections model
Sections model is connected with courses models. After adding our course, the next step is to create a section model. This model will contain the chapters upon which the course are presented. For this we will have a field that is a Foreign key which connect the Sections model to the Course model. The reason for this is because we want to know which section belong to which course.
The Sections models contain three fields, namely: 
- course: this field is a Foreign key to the Course model; the field is linked with the “id” (primary key) form Course model; in this way we tell the model the courses between we can choose
- free_count_lessons: this field contain the information about the type of the section, meaning, if the section has free lessons or not
- title: this field contain the name of the section (or better said, the name of the chapter)

| Field             | Type     |
| ----------------- | -------- |
| id | BigAutoField |
| course | Foreignkey (id) (the id from courses model)  |
| free_count_lessons | CharField |
| title | CharField |


#### Lessons model
The Lessons model serves as a child model of both the Course model and the Section model, resulting in the inclusion of two foreign key fields. One of these fields contains a foreign key referencing the Course model, while the other field references the Section model. This design choice enables us to determine the course and section to which each lesson belongs. These two pieces of information are crucial for displaying the lessons appropriately. The structure of the model is:
- video_url: this field contains the link of the video that is on the cloud service and embedded with the iframe tag in the HTML code. - - title: the field stores the name of the lesson
- preview: this field has two options, yes or no. If it is yes then the course will be show regardless if the course is pro (of course this means that the free_count_lessons field from the section model must be set to “yes” too). If it is no, then the lesson will not be available for pro courses (of course in this case the free_count_lessons field from the section model is set to “no”)
- lesson_description: this field contain relatable information about the lesson
- section: this field contain the foreign key to the primary key “id” of the Sections model, it inherits the names of the sections from which we can choose, and the lesson will belong to that particularly section 
- course: the field contain the foreign key to the primary key “id” of the courses model, it inherits the names of the courses that we have created. 

| Field             | Type     |
| ----------------- | -------- |
| id | BigAutoField |
| course | Foreignkey (id) (the id from courses model) |
| section | Foreignkey (id) (the id from sections model) |
| lesson_description | TextField |
| preview | CharField |
| title | CharField |
| video_url | CharField |

> **Note**
> To create a comprehensive course video, a specific workflow is followed. Firstly, the necessary information is filled in the Course model. Subsequently, the information is populated in the Section model. Lastly, the information pertaining to the lessons is filled in the Lessons model. This sequential approach ensures that before creating a lesson, we have the prerequisite knowledge of the associated course and section/chapter to which it pertains.

#### Persons model
The person model is made for storing newsletter subscription. This model is of the type “Self-Referencing relationship” as it is just a single table with no relationships with other tables. The person model has three fields: 
- country: the field stores the information about the country form where the user is
- email: the field stores the information about the email of the user
- name: it contains the name of the user with which he wants to subscribe for the newsletter

This person model was created because we want to notify the users when we uploaded a new course on our platform, and they can check and watch the course. 

| Field             | Type     |
| ----------------- | -------- |
| id | BigAutoField |
| country | CharField |
| email | CharField |
| name | CharField |

#### Notes model
Notes model is also a “Self-Referencing relationship model”. This model was created as an attempt to provide to the pro users an environment where they can take notes from the course while learning and playing the lesson. After they took the notes the application will generate a pdf with the information from the notes model, and it will be downloaded automatically after the user type the link button for the pdf. Notes model has the following features:
- course_name: this field contains the name of the course for which the user will take the notes 
- lesson_name: this field contains the name of the lesson for which the user will take the notes
- notes: this field stores in a text field the notes of the user
- user_name: this field will contain the name of the account for which the notes are taken

| Field             | Type     |
| ----------------- | -------- |
| id | BigAutoField |
| course_name | CharField |
| lesson_name | CharField |
| user_name | CharField |
| notes | TextField |

> **Note**
> We need to show the pdf with the informations for a specific logged user. For this, normally we needed to link the Notes model with the user model. But we didn’t do that. The reason why, is because we added the user_name field in the notes model. When we generate the pdf file, we can check first if the username form the notes model is the same user within users model; this is made by filtering the information within a variable. We can do that by typing the following code: “<name_of_the_variable> = Notes.objects.filter(user_name = user_account)”. This line of code means this: our variable is of the type Notes, and it will store the name of the user. Then it will be filtered by the same username form the user account model. If the two are the same, then we can show the information for that respective user. 

#### Students model
Students model provides the extended information about the Users model, meaning it contains additional information that we need for a specific user. This model contains information about the users that are subscribed or are not subscribed to the pro package. This mean that we need to have an account with all the informations about the user, along with the authentication of the users. The student model has the following features:
- subscribed: this field will store the boolean field yes or no for the user subscription. If the user is subscribed, hen our field will be a filled checkbox, otherwise, it will be an empty checkbox (meaning the user didn’t subscribed)
- subID: this field will contain the subscription Id for our pro package. After paying this field will have the id of the subscription plan, otherwise it ill have by default the value null (meaning the user didn’t subscribed).
- user: the field will contain the name of the user for which the subscription is happening or not

| Field             | Type     |
| ----------------- | -------- |
| id | BigAutoField |
| user | OneToOneField(id) (the id form the Users model; the pre-build django model |
| subID | CharField |
| subscribed | BooleanField |

> **Note**
> The user field is in a  one to one field relationship with the user model

