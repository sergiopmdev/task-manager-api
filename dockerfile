FROM python:3.11.2-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip --root-user-action=ignore
RUN pip install -r requirements.txt --root-user-action=ignore
COPY . .
ENV PORT=8000
EXPOSE 8000
CMD ["uvicorn", "main:app", "--port", "8000"]
