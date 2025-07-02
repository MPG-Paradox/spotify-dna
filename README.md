# Your Spotify DNA

Your Spotify DNA analyzes your Spotify listening habits, visualizes audio features, and generates custom playlists using machine learning and GPT.

## Setup

1. Clone the repository and create a `.env` inside `backend/` using `.env.example` as a template.
2. Install backend requirements and start the Flask server:

```bash
cd backend
python app.py
```

The app will auto-install requirements on first run.

3. In another terminal install frontend deps and start React dev server:

```bash
cd frontend
npm install
npm start
```

The React app will proxy API requests to the Flask backend running on port 5000.

## Docker

Build and run the full stack using Docker:

```bash
docker build -t spotify-dna .
docker run -p 5000:5000 --env-file backend/.env spotify-dna
```

This builds the React frontend and serves it via Flask in a single container.

