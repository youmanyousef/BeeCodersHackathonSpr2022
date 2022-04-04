# BeeCodersHackathonSpr2022
Hello judges!

How to clone our program:

```bash
$ git init
$ (main) git clone "https://github.com/youmanyousef/BeeCodersHackathonSpr2022.git"
$ (main) chmod +x reset_db.sh
$ (main) ./reset_db.sh
$ (main) python3 manage.py makemigrations app
$ (main) python3 manage.py migrate
$ (main) python3 manage.py createsuperuser
```

Once you are done creating the super user, the project should be done!

Run the server 

```bash
$ (main) python3 manage.py runserver
```

Please note some of our features may not be fully functional. To manually add stuff, login to the super user account with Django's builtin admin panel
`
http://127.0.0.1:8000/admin
`

Thanks so much!
DEMO https://www.youtube.com/watch?v=a1su_PqrwZs

DEVPOST https://devpost.com/software/groupwork-project-networking-service
Libraries used
Django: https://github.com/django/django
Pristine.js: https://github.com/sha256/Pristine
