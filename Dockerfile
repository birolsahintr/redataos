# Resmi Node.js imajını kullan
FROM node:18-alpine

# Çalışma dizinini ayarla
WORKDIR /app

# Paket dosyalarını kopyala
COPY package*.json ./

# Bağımlılıkları yükle
RUN npm install

# Proje dosyalarını kopyala
COPY . .

# Uygulamanın çalışacağı port (Cloud Run genelde 8080 bekler)
EXPOSE 8080

# Uygulamayı başlat
CMD ["npm", "start"]
