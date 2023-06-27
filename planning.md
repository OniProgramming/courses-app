Data Bases Models

Courses -> Section -> Lessons

Courses
    - Title
    - Subtitle
    - Description 
    - Thumbnail
    - Type (free or Pro)

Lessons Page (Multiple lessons can belong to a course; but a course is unique)
    - Title
    - Video url
    - lesson (foreign key to Course)
    - section (foreign key to Sections)

Section Page
    - Title
    - section (foreign key to Course)
