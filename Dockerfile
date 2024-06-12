FROM python:3.10-slim

WORKDIR /code

RUN pip install --upgrade pip

COPY Pipfile Pipfile.lock /code/
COPY . /code

RUN pip install pipenv
RUN pipenv sync --system

COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

EXPOSE 8000

CMD ["/code/entrypoint.sh"]
