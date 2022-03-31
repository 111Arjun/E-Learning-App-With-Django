
# E-Learning App With Django 
An online Learning and Teaching platform which
empowers you to grow professionally and personally.

# Project Live @https://dj-course.herokuapp.com/
```bash
  Use 4111 1111 1111 1111 as Card Number while purchasing Course.
```
### Note: The live site is hosted on free tier of heroku, so it may take some time to load the data.


## Installation

Start by either Downloading Zip file or Clone the repo

```bash
  git clone https://github.com/giriarjun111/E-Learning-App-With-Django.git
  cd E-Learning-App-With-Django
```

```bash
  Create a virtual environment and activate
      pip install virtualenv
      virtualenv envname
  For Mac OS / Linux:
      source envname/bin/activate
  For Windows:
      envname\scripts\activate
```
```bash
  Rename .env.example to .env and Add the values for the follwing or copy this:
    SECRET_KEY=a0kqo78v_8bv=5jkqbtgt$w3(h7xe&(bspu*6s+429=rh+2xd!
    DEBUG=True
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=youremail@gmail.com
    EMAIL_HOST_PASSWORD=yourpassowrd
    EMAIL_USE_TLS=True

   For Razorpay, Create an account and paste your Key ID and SECRET_KEY data
    Razorpay_KEY_ID = 
    Razorpay_KEY_SECRET = 
```

```bash
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
```
    
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://arjungiri.tk/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arjun-giri-full-stack-web-developer-08577519b/)
[![facebook](https://img.shields.io/badge/facebook-1DA1F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/arjun.giri.5099940)



## Features

- Payment System By Razorpay (in future I will also add Stripe)
- Authentication by [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/)
- Bootstrap Theme
- Buy and Enrolled in the Course


## Tech Stack

**Client:** Javascript, HTML & CSS

**Server:** Django


## Screenshots
Home Page
![Home Page](static/images/home.png "Home Page")

Course Page
![Course Page](static/images/course.png "Course Page")








