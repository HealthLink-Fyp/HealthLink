.PHONY: serve testall test migration migrations migrate admin shell lock build add erd reset docs bsetup fsetup db

serve:
	python3 backend/manage.py runserver
	# gunicorn --bind 0.0.0.0:8000 healthlink.wsgi:application

testall:
	python3 backend/manage.py test

test:
	python3 backend/manage.py test tests.test_$(app)

migration:
	python3 backend/manage.py makemigrations

migrate:
	python3 backend/manage.py migrate --run-syncdb

admin:
	python3 backend/manage.py createsuperuser

shell:
	python3 backend/manage.py shell --no-startup

lock:
	poetry lock && poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

build:
	docker build -t backend backend/

# django-extensions commands
erd:
	python3 backend/manage.py graph_models -a -g -I DoctorProfile,PatientProfile,Appointment,MedicalRecord,MedicineShop,MedicalTest,Call -o healthlink/erd.png

reset:
	python3 backend/manage.py reset_db --noinput patient

# Backend setup
bsetup:
	pip install poetry && cd backend && poetry install && poetry shell && cd ..

# Frontend setup
fsetup:
	cd frontend && nvm use 18 && npm install -g @angular/cli@12.2.0 && npm install && ng serve

# Aggregate commands
db: migration migrate