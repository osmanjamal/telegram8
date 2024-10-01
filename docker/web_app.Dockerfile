FROM node:14 as build

WORKDIR /app

COPY web_app/package*.json ./
RUN npm install

COPY web_app .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]