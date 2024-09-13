FROM python3

WORKDIR /library_admin
COPY requirements.txt /library_admin/
COPY start_api.sh .
COPY . .
RUN pip install --upgrade pip && \
     pip install -r requirements.txt
RUN chmod u+rwx start_api.sh
ENTRYPOINT [ "bash", "-c", "/library_admin/start_api" ]

