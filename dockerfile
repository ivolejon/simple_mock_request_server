FROM python:3
EXPOSE 8001
ADD server.py /
RUN pip install flask
CMD [ "python", "./server.py" ]