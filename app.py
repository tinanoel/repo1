FROM python:3.4 -alpine
ADD . / code
WORKDIR / code
run pip install -r requirements.txt
Expose 5000
CMD["python","app.py"]
