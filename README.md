# flaskp - Express frontend + Flask backend example

## Run locally (without Docker)
1. Backend:
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python app.py
   # Backend listens on http://localhost:5000

2. Frontend:
   cd frontend
   npm install
   npm start
   # Frontend listens on http://localhost:3000 and posts to /submit which proxies to backend

## Run with Docker Compose
# Build and run (from project root)
docker compose up --build

# Access:
# Frontend: http://localhost:3000
# Backend (direct): http://localhost:5000

## Build, tag and push images to Docker Hub
# 1. login
docker login

# 2. build & tag images
docker build -t https://hub.docker.com/u/rajusinghstm/flaskp-backend:latest/backend
docker build -t https://hub.docker.com/u/rajusinghstm//flaskp-frontend:latest/frontend

# 3. push
docker push https://hub.docker.com/u/rajusinghstm//flaskp-backend:latest
docker push https://hub.docker.com/u/rajusinghstm//flaskp-frontend:latest

## Git + GitHub
git init
git add .
git commit -m "Initial commit - Express frontend + Flask backend + docker files"
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
