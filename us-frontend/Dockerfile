# pull official base image
FROM node:13.12.0-alpine as build-step

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
COPY . ./
RUN npm install
RUN npm install react-scripts@3.4.1 -g
RUN npm run build

FROM caddy:alpine
EXPOSE 80
EXPOSE 443
COPY --from=build-step /app/build /usr/share/caddy
