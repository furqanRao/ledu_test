**Install the requirements:**

pip install -r requirements.txt
Apply the migrations:

python manage.py makemigrations
python manage.py migrate

**Finally, run the development server:**

python manage.py runserver

**Create User here:**

http://127.0.0.1:8000/signup/

**Create Access Token to access the activity api here:**

http://127.0.0.1:8000/api/token/

**List/Create Activity here:**

http://127.0.0.1:8000/activity/

Authorized Request URL example:

http://127.0.0.1:8000/activity/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzMTY3NzMzLCJqdGkiOiIwMDBiMzA5M2Q5ZTc0Y2Q2YjZkNzc1NTI1NWIxMjhkOCIsInVzZXJfaWQiOjF9.0qA6cEG-9uFF5PdM_rntM6gp4Aewd4qpclT5wElW8pg"

**Activities List:**

["sign_up", "invite_friend", "watch_video", "like_video", "comment_video", "social_share"]
