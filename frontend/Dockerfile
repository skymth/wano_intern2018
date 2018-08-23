FROM node:8.11.2-alpine
ENV LANG C.UTF-8

WORKDIR /opt/docker

COPY package.json .
RUN npm install -g vue-cli && yarn install
COPY . .

# Build app
RUN npm run build

ENV HOST 0.0.0.0
EXPOSE 8080

VOLUME ["/opt/docker"]

# start command
CMD [ "npm", "run", "dev" ]
