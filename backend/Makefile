.PHONY: serve testall test migration migrations migrate admin shell lock build add erd reset docs bsetup fsetup db

serve:
	python3 manage.py runserver
	
testall:
	python3 manage.py test

test:
	python3 manage.py test tests.test_$(app)

migration:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate --run-syncdb

admin:
	python3 manage.py createsuperuser

shell:
	python3 manage.py shell --no-startup

lock:
	poetry lock && poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

build:
	docker build -t backend backend/

# django-extensions commands
erd:
	python3 manage.py graph_models -a -g -I DoctorProfile,PatientProfile,Appointment,MedicalRecord,MedicineShop,MedicalTest,Call -o healthlink/erd.png

reset:
	python3 manage.py reset_db --noinput patient

# Backend setup
bsetup:
	pip install poetry && cd backend && poetry install && poetry shell && cd ..

# Frontend setup
fsetup:
	cd frontend && nvm use 18 && npm install -g @angular/cli@12.2.0 && npm install && ng serve

# Aggregate commands
db: migration migrate