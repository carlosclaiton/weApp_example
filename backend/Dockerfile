# 
FROM python:3.11-slim
# 
WORKDIR /code
# copy requirements to the main working directory
COPY ./requirements.txt /code/
#copy the app content to the workdirectory
COPY ./app/*.* /code/

# combining commands to reduce image size (it is a good practice)
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /code/requirements.txt

#expose the port application
EXPOSE 8000

# run the main api application
CMD [ "python", "./main.py"]
