# !/bin/sh

# create conda virtual environment
echo y | conda create -n docker_train python=3.9 && conda activate docker_train

# install dependency packages
pip install -r requirements.txt

# create table
python manage.py migrate

# upload dependency data
python db_upload/db.py

# find server IP Address
echo "your_server_IP_address"
echo  | ipconfig getifaddr en0

# runserver
python manage.py runserver 0:8000
