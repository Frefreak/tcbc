FROM alpine:latest

RUN apk add python3 py3-pip make gcc musl-dev
RUN pip3 install uvicorn fastapi requests
RUN mkdir -p /server
ADD server.py /server
ADD jd_rev /server/jd_rev
RUN make -C /server/jd_rev/sign/lib
WORKDIR /server
EXPOSE 8000
CMD uvicorn server:app --host 0.0.0.0
