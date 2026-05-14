FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask==2.1.0 werkzeug==2.1.0
ENV YOUR_NAME=Amsrai
EXPOSE 5500
ENTRYPOINT ["python", "app.py"]
