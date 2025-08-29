# Sarthak's Box Office API

A FastAPI-based box office booking system with event management, seat holds, and booking functionality.

## 🚀 Quick Start

### Option 1: Run with Docker (Recommended)

```bash
# Make the script executable
chmod +x run-docker.sh

# Run with Docker
./run-docker.sh
```

**Or manually:**
```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in background
docker-compose up -d --build
```

### Option 2: Run Locally

```bash
cd app && uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 🐳 Docker Commands

```bash
# Build the image
docker build -t box-office-api .

# Run container
docker run -p 8000:8000 box-office-api

# Stop containers
docker-compose down

# View logs
docker-compose logs -f

# Rebuild and restart
docker-compose up --build --force-recreate
```

## 📋 Prerequisites

### For Docker:
- Docker
- Docker Compose

### For Local Development:
- Python 3.8+
- pip or conda

## 🔧 Installation

### Docker Setup:
1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd sarthak-s-box-office
   ```

2. **Run with Docker**
   ```bash
   ./run-docker.sh
   ```

### Local Setup:
1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd sarthak-s-box-office
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**
   ```bash
   cd app && uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## 🌐 API Endpoints

- **Events**: `POST/GET /api/event/`
- **Holds**: `POST /api/hold/hold/`
- **Bookings**: `POST /api/book/book/`

## 📖 API Documentation

Once the server is running, visit:
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🗄️ Database

- **SQLite** database with auto-table creation
- Tables are automatically created on server startup
- **Docker**: Database file: `./data/box_office.db`
- **Local**: Database file: `./box_office.db`

## 🔄 Complete Workflow

1. **Create Event** → `POST /api/event/event/`
2. **Create Hold** → `POST /api/hold/hold/` (reserves seats)
3. **Book Seats** → `POST /api/book/book/` (converts hold to booking)

## 🧪 Testing

Use the provided `api_curl_commands.md` file for testing all endpoints with curl commands.

## 📝 Notes

- Holds expire after 2 minutes
- Seats are automatically managed (deducted on hold, restored on expiry)
- Background worker automatically releases expired holds
- Concurrent seat reservations are handled with row-level locking

## 🛠️ Development

### Docker Development:
- **Hot reload**: Enabled with volume mounting
- **Port**: `8000` (accessible at http://localhost:8000)
- **Data persistence**: Database stored in `./data/` directory

### Local Development:
- **Auto-reload**: Enabled with `--reload` flag
- **Host**: `0.0.0.0` (accessible from other devices on network)
- **Port**: `8000` (change with `--port` flag)

## 🚨 Troubleshooting

### Docker Issues:
- **Port already in use**: Change port in docker-compose.yml
- **Permission errors**: Run `chmod +x run-docker.sh`
- **Container won't start**: Check logs with `docker-compose logs`

### Local Issues:
- **Port already in use**: Change port with `--port 8001`
- **Database errors**: Delete `box_office.db` and restart server
- **Import errors**: Ensure you're in the `app` directory when running uvicorn

## 🔍 Container Health

The Docker container includes health checks:
- **Health endpoint**: Monitors API availability
- **Auto-restart**: Container restarts on failure
- **Logs**: Easy access to application logs