FROM python:slim-buster
EXPOSE 5000 
WORKDIR /app2 
COPY requirements.txt . 
RUN pip install -r requirements.txt 
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
