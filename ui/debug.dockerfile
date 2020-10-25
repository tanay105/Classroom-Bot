FROM node:10
RUN mkdir app
COPY /classroom-bot-ui/. app/
RUN cd app/  && \
    npm install && 
CMD ["sudo", "cp", "-rf", "build", "/temp"]
