# A simple django restful api for CRUD Bucketlist app with JWT authentication
This repo contains the source code for a simple api to for creating a Bucketlist app. 
It uses authentication to prevent users from editing bucketlists except their own

### How to use 
-Before proceeding make sure all requirements are installed. <br>
-You can install all requirements by using `pip install -r requirements.txt`.<br>
- Change `YOUR_SECRET_KEY` in `/bucketlist/settings.py` to your unique secret key
- Change `YOUR_HEROKU_APP` in `ALLOWED_HOSTS` in `/bucketlist/settings.py` to the your heroku app url or if you don't want to host the app on heroku just remove it.
#### Run it on local system
- `git clone https://github.com/theimperium20/sqllite-flask-api.git`
- Run the follwing commands on powershell or terminal:
  - `python manage.py makemigrations`
  - `python manage.py migrate`
- Create a superuser by using `python manage.py createsuperuser`
- Enter the deatils for the user
- To run the server use `python manage.py runserver`
- Make a `POST` request to `/get-token/` with `data={"username":"*name_of_user_you_created*,"password":"*password_you_entered*"}`
- It will return you the authorization token
- Include this token in headers as `headers={"Authorization":"Token <obtained-token-here>", "Content-Type":"application/json"` in all your further requests

#### Endpoints 
- POST /get-token `-- Expects - {"username":value,"password":value}` `-- Returns authorization token`
- GET /bucketlist/ `-- Expects - authorization token` `Returns all bucketlists`
- POST /bucketlist/ `--Expects - authorization token -{"name": your_bucketlist}` `-- Returns the inserted records`
- PUT /bucketlist/id/ `-- Expects - authorization token -{"name": your_bucketlist}` `--Returns the updated records`
- PATCH /bucketlist/id/ `-- Expects - authorization token -{"name": your_bucketlist}` `--Returns the updated records`
- DELETE /bucketlist/id/ `-- Expects - authorization token`

### Live API server base url https://bucketlist-restapi.herokuapp.com/bucketlist/

Set `DEBUG=False` on production server
