FROM selenium/standalone-chrome

USER root
RUN apt-get update && apt-get install -y python3-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

COPY ./requirements.txt ./
RUN python3 -m pip install -r requirements.txt
COPY . .


CMD ["python3", "main.py"]