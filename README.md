![Asian Travel logo](/static/css/images/logo.png)


## Introduction
With the Asian Travel blog, users benefit from a wide range of extensive functionality.

Users can perform a number of actions including; register for an account, login, logout, and perform the full suite of CRUD administrative tasks including creating a post, creating and saving a draft, delete, edit and manage posts, and approve comments. 

Users can also have a profile, which can be created and edited, and displayed to other users. Unauthenticated users meanwhile are able to view and open posts, view comments, comment, and view a list of posts.


## Built with
Python & Django


## Built with

This project began with firstly ideating on, and generating the concept for the blog. 
From there, a study was carried out across similar blogs available online to help inform desirable user experience, actions and features - and the feasibility thereof. 
Following this, a high-level technical approach and dependency mapping was carried out that would allow all necessary functionality creation to be verified in terms of feasibility and viability. At this stage, work was also undertaken to identify areas of functionality overlap within the blog.
The high-level technical approach permitted the decomposition of the work into user stories, which were created thus enabling development to commence. 
Following development work, extensive end-to-end testing and validation was carried out to ensure code hygiene, performance and functionality for users. 


## User Experience (UX)
The Asian Travel blog is primarily designed for ease of navigation, readership and administration.
For blog readers, the primary focus is on readership and engagement with the content. This is reflected directly on the homepage, which surfaces blog articles listed by date posted and is paginated. 
The top navigation is straight-forward and enables users to sign up, or login (or log out, where relevant). 
On posts meanwhile, users are drawn through the article with engagement functions at the end including an intuitive heart icon to like/unlike a post and a clearly laid out comments box to create a comment.
Blog administrators (authenticated users) meanwhile see additional optionality provided to them natively within the blog pages, including the ability to view and edit their own posts directly from the post page.
The administration UX is similarly straightforward and creating a post is a guided process with several boxes for title, content, attachment, etc. centered on the page to maximise focus. Similarly, additional functions such as deleting a post, approving comments, etc. are simple one-click actions nested natively within the blog. 
Lastly, the user profiles allow for at-a-glance understanding of the blog user or author, so readers can quickly learn more about them. Meanwhile, for those users, the profile can be edited easily within the same page by selecting to edit the profile. 


## Design


**Colour Scheme**

The colour scheme for this blog emphasises light blue to dark blue gradient as the primary background colour, and black as the primary text colour in order to ensure ease of reading, and place the focus on the content.


**Typography**


Roboto from Google Fonts was chosen for this programme.


**Imagery**
No imagery exists within the programme.


## Features

- Clear navigation and button labels to relevant functions, dependent on authentication status.


- Ability for users to register an account, login and logout.


- Ability for users to create a profile for display on the blog, and to be able to edit this profile when necessary.


- Ability for authenticated users within the administration area to create a post, edit a post, delete a post, and create a draft.


- Authenticated users can review and approve blog post comments, like and unlike posts, and create a comment on a specific blog post.


- Both authenticated and unauthenticated users can view posts, view comments on specific blog posts and view like counts on specific posts. 


- The site is also responsive and displays across multiple different device and screen types; and includes pagination

- Upon will receive notification when they have :
    1) Logged in to their account
    2) Logged out from their account
    3) Edited a post
    4) Edited their profile content
    5) Commented on a post.


- Additionally, the admin of the site has to login and approve user's comments to avoid any scam/marketting comments to decrease the quality of the blog.


## Technologies Used
- Heroku

- GitPod

- Github


## Description of the technologies Used

**GIT**

GIT was used for version control and utilising the Gitpod terminal to commit to Git and push to Github.

**GitHub**


Github is used to store the projects code after being pushed from Git.
Github Projects was used to evidence of agile methodologies used during the project.


**Slack Channel**


Slack was used to communicate with other coders, and tutors to resolve issues which I was facing with the project.


**Heroku**


Heroku was used to deploy the project.

**Heroku PostgreSQL add-on**

Postgres was used to store the blog posts, likes and comments.  


## Testings

The PEP8 Validator was used to validate the code of the project to ensure there were no errors in the project.

The PEP8 Validator was used to validate the code of the project to ensure there were no errors in the project.
PEP Online Validator-

Result : "All Right"
In addition to that, I was also using the console to ensure that there were no errors in the whole duration of the project.

## Further Testings

**Add Post Test**
1. Navigated to "Add Post" page
2. Entered data Title: Post 1, Content: ABC etc. 
3. Clicked submit, or whatever you called the button
4. Navigated to Home page and saw the new post present

**Edit Post Test**
1. Navigated to Post 1
2. Changed content value to DEF, clicked edit
3. Navigated to Home Page
4. Saw that the content value had changed


**Delete Post**
1. Navigated to Post 1
2. Changed content value to DEF, clicked delete
3. Navigated to Home Page
4. Saw that the content has been deleted


**View Comments**
1. Created a comment
1. Created a comment
2. Entered comment 'test',
3. Navigated to Admin page
4. Approved comment
4. Saw that the comment was shown on page


**Approve Comments**
1. Created a comment
2. Entered comment 'test',
3. Navigated to Admin page
4. Approved comment
4. Saw that the comment was shown on page

****

**Like and Unlike Post**
1. Navigated to "Post" page as an authenticated logged-in user
2. Clicked on Like button
3. The heart lighted up and the likes count was shown as '1'


**Unlike Post**
1. Navigated to "Post" page as an authenticated logged-in user
2. Clicked on Unlike button
3. The heart lighted up and the likes was shown as '0'

**Account Registration**

1. Navigated to the "Sign Up" button
2. Entered details as requested
3, Navigated to the admin page
4. User was indicated as created

**Account Login**

1. Navigated to the "Login" button
2. Entered details as requested
3, User was logged in and was able to view post, edit post and delete post

**Account Logout**
1. Navigated to the "Sign Out" button
2. A re-confirmation message was received
3. Once clicked, user was signed out


**User Profile**
1. Navigated to the "User Profile" button
2. Information was displayed as entered

**Edit User Profile**
1. Navigated to the "Edit profile" button
2. Information was chnaged and 'Saved'
3. Navigated to the "User Profile" button
4. Information was displayed as entered


## Images of the programme

**Homepage**


![Homepage](/static/css/images/homepage.JPG)


**Post Details Page as a non logged in user**


![Post Details Page](/static/css/images/post-page1.JPG)


**Sign Up Page**


![Sign Up Page](/static/css/images/sign-up-page.JPG)


**Logout Page**


![Sign Out Page](/static/css/images/sign-out-page.JPG)


**Add Blog Post Page**


![Sign Out Page](/static/css/images/add-blogpost-page.JPG)


**Post Details Page as a logged in user (blogger)**


![Post Detail Page](/static/css/images/post-page2.JPG)


**Edit post page**


![Edit Post Page](/static/css/images/edit-post-page.JPG)


**Delete post page**


![Delete Post Page](/static/css/images/delete-post-page.JPG)


**Initial Profile Page**


![Initial Profile Page](/static/css/images/initial-profile-page.JPG)


**Updated and edited profile page**


![Updated and Edited Profile Page](/static/css/images/completed-profile-page.JPG)

**Edit Profile page**

![Updated and Edited Profile Page](/static/css/images/edit-profile-page.JPG)


## Accessibility

The project can be accessed using Heroku.


## Bugs

There was one uncorrectable bug at the time of final deployment as below;
1. In the sign-up process, users see a 500 Server Error upon entering their credentials, but this problem has been resolved.


## Issues Faced during the project

- Trying to create the Profile.form
- Final Git Push for the project

## Deployment

- This blog was deployed using Heroku, the steps of deployment are as follows:

1) Create the Heroku app and give the project a name.
2) Attach the Heroku Postgres database
3) Prepared the environment and settings.py file. 
4) Get the static and media files stored on Cloudinary.
5) Import the operating system library in the env.py file and Heroku in the config vars.
6) Deployment was then completed.



## Credits and references

- https://www.flake8rules.com/
- https://www.geeksforgeeks.org/
- https://realpython.com/python-operators-expressions/
- https://getbootstrap.com/docs/4.0/components/buttons/


