# Python 3.9 tabanlı hafif bir Linux kullan
FROM python:3.9-slim

# Çalışma klasörünü ayarla
WORKDIR /app

# Dosyaları kopyala
COPY . .

# Gereksinimleri yükle (requirements.txt birazdan oluşturacağız)
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit'in Cloud Run'da çalışması için özel ayarlar
# Burası ÇOK ÖNEMLİ: Portu 8080'e sabitliyoruz.
EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Uygulamayı başlatırken portu zorla 8080 yapıyoruz
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]docker build \
    -t gcr.io/gen-lang-client-0632716855/github.com/birolsahintr/redataos:$COMMIT_SHA \
    -f DockerFile \
    .
