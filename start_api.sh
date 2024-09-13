# !bin/bash

echo "<<<<<<<<<<<<<<<<<<<<<< running migrations >>>>>>>>>>>>>>>>>>>>>>>>>>"
python3 -m manage makemigrations --no-input
python3 -m manage migrate --no-input
echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<< starting the server >>>>>>>>>>>>>>>>>"
exec gunicorn --bind 0.0.0.0:8000 library_admin.wsgi:application
