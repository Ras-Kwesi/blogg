# BLOG

## Built By [Ras Kwesi](https://github.com/Ras-Kwesi/)

## Description
Blog is a Python project that uses Database to store blogs of blogers and subscribers comments.

## User Stories

As a user I would like:
* Get to see various sources to select a newsfeed from.
* Get to see news articles from the various news sources

##Behaviours

| Behaviour |  Input   |   Output    |  
| :--------------------- | :-------------------------: | ----------------------: |
| Display Pitches | **Landing Page** | List of pitches is displayed |
| Display Category of Pitch | **Category Page** | Pitches of certain category are displayed |
| New Pitch is input | **New Pitch Page** |Markdown form to add new pitch |
| Display Single Pitch | **Pitch Page** |Pitch and attributes displayed |
| Log in to account | **Login Page** |Form text boxes to login in user data |
| Register new user | **Registration Page** |Form to register new users data |
| Update user profile | **Update Profile Page** |Page to update the profile page |


## Project Specification
-[x] View sample pitches on home page, and ability to navigate to specific categories.
-[x] View a pitch and it's comments.
-[x] Log in requirement to create a new pitch.
-[x] Sign up navigation from navogation bar and log in page.
-[x] Log out when logged in.
-[x] Add new pitch form page.
-[x] Add new comment on pitch, form page
-[x] View logged-in user profile page.
-[x] Update profile page with bio and picture

### Installations & Prerequisites
* python3.6
* pip
* Heroku CLI
* Bootstrap
* ProsgreSQL

### Cloning
* In your terminal:
        
        `git clone https://github.com/ras-kwesi/blog/`
        `cd blog`

## Running the Application
* To run the application, in your terminal:

        `chmod +x run.py`
        `./start.sh`
        

## Testing the Application
* To run the tests for the class file:

        `python3.6 test_models.py`
   
## Technologies Used
* Python3.6
* SQLAlchemy
* AJAX
* jQuery

## License
MIT &copy;2017 [Ras Kwesi](https://github.com/ras-kwesi/)