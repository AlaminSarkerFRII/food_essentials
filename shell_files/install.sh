python3 -m venv venv
source venv/bin/activate

python3 run pip install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser

deactivate