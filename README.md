# Simple FastAPI with Firebase Authentication
I always start my projects with a baseline that includes user management, which I handle using Firebase. This repository contains the most basic FastAPI application that I use as a starting point for new projects.

* Set up a FastAPI app which is connected to Firebase Auth Project
* Simple "Protected" API Endpoint (requires user auth)

In the future I will add some basic SQLAlchemy setups, simple CI, etc.


### Setup:
First, make sure you have a Firebase project, with Auth app:
```
https://firebase.google.com/docs/auth
```

Then, clone the repo:
```
git clone https://github.com/adamcohenhillel/simple_fastapi_with_firebase.git
```

Install dependencies:
```
cd simple_fastapi_with_firebase
python3 -m pip install -r requirements.txt
```

Set environment variables [for Firebase]:
for fulle explanation, read: https://firebase.google.com/docs/admin/setup#python_1
```
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"
```

*And run:*
```
python3 run_api.py
```

### How to test:
1. Create a user in your Firebase Auth App
2. Genertae a TokenID
POST https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[WEBAPIKEY]
{
	"email": "email@gmail.com",
	"password":"password",
	"returnSecureToken":true
}
3. Send a request to your FastAPI protected endpoint
GET http://127.0.0.1:8000/api/simple_router/firebase_user
Headers:
Authorization: TokenID


