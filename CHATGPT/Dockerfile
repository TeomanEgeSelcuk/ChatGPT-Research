FROM python:3.8
WORKDIR /app

# COPY requirements.txt ./
# RUN pip install -r requirements.txt
RUN pip install pymongo

COPY ./ ./
CMD ["./myscript.py"]

# Create src and dump directories
RUN mkdir /app
VOLUME ["/app/src", "/app/dump", "/data/db", "/var/www/html"]

CMD ["/bin/bash"]
