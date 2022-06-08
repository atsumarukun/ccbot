FROM ubuntu:20.04

RUN apt update && apt -y install tzdata
ENV TZ=Asia/Tokyo

RUN apt -y install vim python3 python3-pip python3-tk && \
    python3 -m pip install numpy matplotlib requests aiohttp
