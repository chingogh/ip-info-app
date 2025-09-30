import requests

API_URL = "http://ip-api.com/json/"

def fetch_ip_info():
    try:
        response = requests.get(API_URL)
        data = response.json()
        return {
            "IP": data.get("query"),
            "ISP": data.get("isp"),
            "ASN": data.get("as"),
            "City": data.get("city"),
            "Region": data.get("regionName"),
            "Country": data.get("country"),
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    info = fetch_ip_info()
    for key, value in info.items():
        print(f"{key}: {value}")
