# ---- Frontend build ----
FROM node:18 AS frontend
WORKDIR /app
COPY frontend/package.json ./
RUN npm install
COPY frontend ./frontend
RUN npm run build --prefix frontend

# ---- Backend build ----
FROM python:3.9-slim AS backend
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY backend ./backend
COPY --from=frontend /app/frontend/build ./backend/static
WORKDIR /app/backend
CMD ["python", "app.py"]
