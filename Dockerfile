FROM python:3

WORKDIR /library_admin
COPY start_api.sh ./start_api.sh
COPY . .
RUN pip install --upgrade pip && \
     pip install -r requirements.txt
RUN chmod +x ./start_api.sh
ENTRYPOINT [ "sh", "/library_admin/start_api.sh" ]

