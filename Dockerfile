FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 8001
CMD ["python", "apiwriter.py", "http://webserver:8001"]
