virtualenv . && pip install coverage flask mock nose-exclude nosegae oauth2 pytest pyyaml

source bin/activate

ls app/secrets.py || cp app/secrets.py_TEMPLATE app/secrets.py

dev_appserver.py .
