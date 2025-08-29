# API Curl Commands for Sarthak's Box Office API

This document contains curl commands for all the available API endpoints in the project.

## Base URL
```
http://localhost:8000
```

## 1. Event Management APIs

### Create Event
```bash
curl -X POST "http://localhost:8000/api/event/event/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Concert in the Park",
    "seats": 100
  }'
```

### Get All Events
```bash
curl -X GET "http://localhost:8000/api/event/event/" \
  -H "Accept: application/json"
```

## 2. Hold Management APIs

### Create Hold (Reserve Seats)
```bash
curl -X POST "http://localhost:8000/api/hold/hold/" \
  -H "Content-Type: application/json" \
  -d '{
    "event_id": 1,
    "qty": 2
  }'
```

**Note:** This will return a payment token and hold ID that you'll need for booking.

## 3. Booking APIs

### Book Seats (Convert Hold to Booking)
```bash
curl -X POST "http://localhost:8000/api/book/book/" \
  -H "Content-Type: application/json" \
  -d '{
    "hold_id": 1,
    "payment_token": "your-payment-token-here"
  }'
```

## Complete Workflow Example

Here's a complete example of the booking workflow:

### Step 1: Create an Event
```bash
curl -X POST "http://localhost:8000/api/event/event/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Rock Concert 2024",
    "seats": 50
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "status_code": 201,
  "data": {
    "id": 1,
    "name": "Rock Concert 2024",
    "seats": 50,
    "created_at": "2024-01-01T10:00:00"
  }
}
```

### Step 2: Create a Hold (Reserve Seats)
```bash
curl -X POST "http://localhost:8000/api/hold/hold/" \
  -H "Content-Type: application/json" \
  -d '{
    "event_id": 1,
    "qty": 3
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "status_code": 201,
  "data": {
    "id": 1,
    "payment_token": "uuid-payment-token-here",
    "expires_at": "2024-01-01T10:02:00"
  }
}
```

### Step 3: Book the Seats
```bash
curl -X POST "http://localhost:8000/api/book/book/" \
  -H "Content-Type: application/json" \
  -d '{
    "hold_id": 1,
    "payment_token": "uuid-payment-token-here"
  }'
```

**Expected Response:**
```json
{
  "success": true,
  "status_code": 200,
  "data": {
    "id": 1,
    "hold_id": 1,
    "qty": 3
  }
}
```

### Step 4: Check Available Events
```bash
curl -X GET "http://localhost:8000/api/event/event/" \
  -H "Accept: application/json"
```

## Error Handling Examples

### Invalid Event ID
```bash
curl -X POST "http://localhost:8000/api/hold/hold/" \
  -H "Content-Type: application/json" \
  -d '{
    "event_id": 999,
    "qty": 2
  }'
```

### Insufficient Seats
```bash
curl -X POST "http://localhost:8000/api/hold/hold/" \
  -H "Content-Type: application/json" \
  -d '{
    "event_id": 1,
    "qty": 1000
  }'
```

### Expired Hold
```bash
# Wait for hold to expire (2 minutes) then try to book
curl -X POST "http://localhost:8000/api/book/book/" \
  -H "Content-Type: application/json" \
  -d '{
    "hold_id": 1,
    "payment_token": "expired-token"
  }'
```

### Invalid Payment Token
```bash
curl -X POST "http://localhost:8000/api/book/book/" \
  -H "Content-Type: application/json" \
  -d '{
    "hold_id": 1,
    "payment_token": "wrong-token"
  }'
```

## Testing with Different Data

### Create Multiple Events
```bash
# Event 1
curl -X POST "http://localhost:8000/api/event/event/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Jazz Night", "seats": 30}'

# Event 2
curl -X POST "http://localhost:8000/api/event/event/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Comedy Show", "seats": 80}'

# Event 3
curl -X POST "http://localhost:8000/api/event/event/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Theater Play", "seats": 120}'
```

### Multiple Holds for Same Event
```bash
# Hold 1: 2 seats
curl -X POST "http://localhost:8000/api/hold/hold/" \
  -H "Content-Type: application/json" \
  -d '{"event_id": 1, "qty": 2}'

# Hold 2: 1 seat
curl -X POST "http://localhost:8000/api/hold/hold/" \
  -H "Content-Type: application/json" \
  -d '{"event_id": 1, "qty": 1}'
```

## Notes

1. **Hold Expiration**: Holds expire after 2 minutes
2. **Payment Token**: Each hold gets a unique UUID payment token
3. **Seat Management**: Seats are automatically deducted when holds are created and restored when holds expire
4. **Foreign Keys**: The system maintains referential integrity between events, holds, and bookings
5. **Concurrent Access**: Uses `with_for_update()` for handling concurrent seat reservations

## Running the API

To run the API server:
```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Health Check

You can also check if the API is running:
```bash
curl -X GET "http://localhost:8000/docs" \
  -H "Accept: text/html"
```

This will open the FastAPI interactive documentation in your browser.
