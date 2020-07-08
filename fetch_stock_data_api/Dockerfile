FROM python:3-alpine

WORKDIR /fetch_stock_data_api
COPY . /fetch_stock_data_api

RUN apk add postgresql-libs postgresql-dev && \
    apk add --virtual .build-deps gcc musl-dev && \
    pip install -r requirements.txt && \
    apk --purge del .build-deps


RUN ls
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-w", "4", "wsgi:application"]

# Expose the Flask port
EXPOSE 8000