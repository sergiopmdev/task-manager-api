docker build --pull --rm -f "dockerfile" -t taskmanagerapi:run "."
docker run --rm -it -p 8000:8000/tcp taskmanagerapi:run
