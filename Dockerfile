FROM python:3.9.17
COPY . /digits
RUN pip3 install --no-cache-dir -r /digits/requirements.txt
WORKDIR /digits
# CMD ["python3","exp.py"]

ENV FLASK_APP=app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
