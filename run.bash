python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt --quiet


python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

