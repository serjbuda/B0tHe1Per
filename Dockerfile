FROM python:3.10.5
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "bot_interface.py"]