FROM python:3.9.17
COPY . /digits
RUN pip3 install --no-cache-dir -r /digits/requirements.txt
WORKDIR /digits
CMD ["python3","exp.py"]

#7-11 lec

ENV FLASK_APP=app.py

CMD ["flask", "run","--host=0.0.0.0"]