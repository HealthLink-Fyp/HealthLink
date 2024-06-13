.PHONY: serve testall test migration migrations migrate admin shell lock build add erd reset docs bsetup fsetup db

serve:
	# poetry run python3 manage.py runserver
	gunicorn --bind 0.0.0.0:8000 healthlink.wsgi:application

testall:
	poetry run python3 manage.py test

test:
	poetry run python3 manage.py test tests.test_$(file)

migration:
	poetry run python3 manage.py makemigrations

migrate:
	poetry run python3 manage.py migrate --run-syncdb

admin:
	poetry run python3 manage.py createsuperuser

shell:
	poetry run python3 manage.py shell --no-startup

lock:
	poetry lock && poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

build:
	docker build --no-cache --rm -t backend .

add:
	poetry add $(package) && make lock

# django-extensions commands
erd:
	poetry run python3 manage.py graph_models -a -g -I DoctorProfile,PatientProfile,Appointment,MedicalRecord,MedicineShop,MedicalTest,Call -o healthlink/erd.png

reset:
	poetry run python3 manage.py reset_db --noinput patient

# MKDocs commands
docs:
	mkdocs serve

# Backend setup
bsetup:
	pip install poetry && cd backend && poetry install && poetry shell && cd ..

# Frontend setup
fsetup:
	cd frontend && nvm use 18 && npm install -g @angular/cli@12.2.0 && npm install && ng serve

# Aggregate commands
db: migration migrate