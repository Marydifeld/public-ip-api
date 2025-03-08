from fastapi import FastAPI, Request
import requests

app = FastAPI()

# Get user's public IP
@app.get("/ip")
async def get_ip(request:Request):
    user_ip = request.client.host
    return {"ip":user_ip}

# Get information about the IP 
@app.get("/ip/details")

async def get_ip_details(request:Request):
    client_ip = request.client.host
    response = requests.get(f"http://ip-api.com/json/{client_ip}")
    data = response.json()
    return {
        "ip": client_ip,
        "city": data.get("city"),
        "region": data.get("regionName"),
        "country": data.get("country"),
        "isp": data.get("isp"),
        "latitude": data.get("lat"),
        "longitude": data.get("lon"),
    }

# Look up a specific IP 
@app.get("/ip/{ip}")
async def lookup_ip(ip:str):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    return {
        "ip": ip,
        "city": data.get("city"),
        "region": data.get("regionName"),
        "country": data.get("country"),
        "isp": data.get("isp"),
        "latitude": data.get("lat"),
        "longitude": data.get("lon"),
    }
