FROM python:3.8



# WORKDIR /emis .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# COPY script.py .
COPY . .
CMD [ "python", "./main.py" ]