FROM python:3.11.2-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip --root-user-action=ignore
RUN pip install -r requirements.txt --root-user-action=ignore
COPY . .
EXPOSE 8000
