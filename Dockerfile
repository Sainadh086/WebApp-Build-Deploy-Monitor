# selecting python as base image
FROM python:3.9

# creating working directory
RUN mkdir TASKAPP

# changing directory to working directory
WORKDIR TASKAPP

# copying files to working directory
COPY task_app/ .

# installing requirements
RUN pip3 install -r requirements.txt

#Exposing the application port 
EXPOSE 8080

# running the application
CMD ["python3", "app.py"]
