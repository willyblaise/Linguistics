FROM python:latest

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . /app

# start the server
#CMD ["uvicorn", "books_api:app", "--host", "0.0.0.0", "--port", "5050"]
ENTRYPOINT ["python"]
CMD ["books_api.py"]
