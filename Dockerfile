FROM fedora:latest

RUN dnf update -y && \
    dnf install -y python3 python3-pip gcc && \
    dnf clean all

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]