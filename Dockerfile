# Usar imagem base do Python
FROM python:3.10

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto para dentro do container
COPY . .

# Instalar dependências (se tiver um requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt || true

# Rodar o script Python
CMD ["python", "Teste.py"]
