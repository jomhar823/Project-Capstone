source venv/Scripts/activate

python3.11.4 -m pip install -r requirements.txt

python3.11.4 manage.py makemigrations --noinput
python3.11.4 manage.py migrate --noinput
python3.11.4 manage.py collectstatic --noinput --clear
