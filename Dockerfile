FROM python:3.8

RUN pip install fastapi uvicorn mangum pydantic

EXPOSE 8080

COPY ./ld_proxy /ld_proxy

CMD ["uvicorn", "ld_proxy.main:app", "--host", "0.0.0.0", "--port", "8080"]
