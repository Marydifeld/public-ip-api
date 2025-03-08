# Public IP Lookup API 🌍

A FastAPI-based Public IP Lookup API that returns your IP address and location details.

## Features
- Get your public IP address
- Fetch detailed IP info (city, country, ISP)
- Lookup any IP address for details

## Technologies
- **FastAPI** (Python)
- **Uvicorn** (ASGI server)
- **Requests** (API calls)

## Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/ip` | Returns your public IP |
| `GET` | `/ip/details` | Returns your IP + geolocation info |
| `GET` | `/ip/{ip}` | Lookup details for a specific IP |

## How to Run Locally
In bash:
pip install -r requirements.txt
uvicorn main:app --reload
