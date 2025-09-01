FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 8001
CMD ["python", "apiwriter.py", "http://172.17.0.2:8001"]
