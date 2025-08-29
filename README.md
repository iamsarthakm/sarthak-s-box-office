# Sarthak's Box Office API

A FastAPI-based box office booking system with event management, seat holds, and booking functionality.

## 🚀 Quick Start

### Run the Server (Single Command)

```bash
cd app && uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

That's it! Your server will be running at `http://localhost:8000`

## 📋 Prerequisites

- Python 3.8+
- pip or conda

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd sarthak-s-box-office
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy
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
- Database file: `./box_office.db`

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

- **Auto-reload**: Enabled with `--reload` flag
- **Host**: `0.0.0.0` (accessible from other devices on network)
- **Port**: `8000` (change with `--port` flag)

## 🚨 Troubleshooting

- **Port already in use**: Change port with `--port 8001`
- **Database errors**: Delete `box_office.db` and restart server
- **Import errors**: Ensure you're in the `app` directory when running uvicorn