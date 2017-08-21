virtualenv . && source bin/activate && pip install coverage flask mock nose-exclude nosegae oauth2 pytest pyyaml

ls app/secrets.py || cp app/secrets.py_TEMPLATE app/secrets.py

dev_appserver.py .
