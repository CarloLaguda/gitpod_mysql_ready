FROM gitpod/workspace-mysql
RUN pip install -r requirements.txt
RUN python import_data.py