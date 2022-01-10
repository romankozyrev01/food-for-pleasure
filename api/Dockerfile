FROM python:3

WORKDIR .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirments.txt ./code/
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r ./code/requirments.txt
COPY . ./code/

CMD ["python", "manage.py", 'migrate']