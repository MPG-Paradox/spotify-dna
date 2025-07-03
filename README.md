# Your Spotify DNA

Your Spotify DNA analyzes your Spotify listening habits, visualizes audio features, and generates custom playlists using machine learning and GPT.

## Setup

1. Clone the repository and create a `.env` inside `backend/` using `.env.example` as a template.
2. Install backend requirements and start the Flask server:

```bash
cd backend
python app.py
```

The app will auto-install requirements on first run and compile Python files.
On Windows you may see a warning like `Can't list ... python*.zip` during this
compile step. As long as no other errors appear, you can safely ignore it.

3. In another terminal install frontend deps and start React dev server:

```bash
cd frontend
npm install
npm start
```
4. Visit `http://localhost:3000` and click **Login with Spotify** to authorize access.
   After authentication the dashboard will display your top artists, tracks, a summary of your
   listening habits, and tools to generate playlists.


The React app will proxy API requests to the Flask backend running on port 5000.

## Docker

Build and run the full stack using Docker:

```bash
docker build -t spotify-dna .
docker run -p 5000:5000 --env-file backend/.env spotify-dna
```

This builds the React frontend and serves it via Flask in a single container.

## Environment variables

Create a `.env` file under `backend/` with your Spotify API credentials and optional `OPENAI_API_KEY`. See `.env.example` for all available variables.

