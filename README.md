# wad2_team_project
Team project for Web Application Development class:

This web application is called the Neighborhood Cookbook.
Its purpose is to allow users to upload, share, and view recipes from other users in an informal setting.
Users can register for the Neighborhood Cookbook, allowing them to create a username, add recipes,
and add reviews and ratings to other users' recipes, as well as suggest a category. Users are able
to customise their profile by uploading a personalised bio to introduce themselves to the community,
and by adding a profile picture. All aspects of the profile can be edited except username, after first registering
for an account, by using the Edit Profile button displayed on the profile page.

Similarly, users can navigate the website's categories and recipes anonymously without signing in, but
cannot leave reviews or ratings or add recipes. Anonymous users can also read the About Us page
to learn more about the creators of the Neighborhood Cookbook.

How To Run:<br/>
<br/>
python manage.py makemigrations<br/>
python manage.py migrate<br/>
python populate_script.py<br/>
python manage.py runserver<br/>

The site is available on https://localhost:8000
