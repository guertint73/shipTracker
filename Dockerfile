FROM python3:10

RUN mkdir /shipTracker
COPY . /shipTracker

WORKDIR /shipTracker

RUN pip install pipenv
RUN pipenv install --system --deploy

EXPOSE 6565
CMD ["pipenv", "shell"]
ENTRYPOINT [ "python", "src/server.py" ]