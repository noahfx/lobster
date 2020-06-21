
FROM  python
COPY . /lobster_source
RUN apt update 
RUN apt install -y ffmpeg
RUN pip install /lobster_source/
CMD lobster

