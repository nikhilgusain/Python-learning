import requests
import geopyLibrary as gp
url = "https://api.wheretheiss.at/v1/satellites/25544"

def call_iss():
    conn= requests.get(url)
    data = conn.json()

    if data["name"]:
        print("Conncetion Successfull")
        lat = data["latitude"]
        long = data["longitude"]
        alti = data["altitude"]
        vis = data["velocity"]
        print(f"latitude - {lat}\nlongitude - {long}\nalti - {alti}\nvelocity - {vis} km/h")
        
        location = gp.get_location(lat, long)
        if location != "Unkown":
            print(f"Current location - {location}")
        else:
            print("Current location - Possibly over ocean or unknown area")
    else:
        raise Exception("Failed to conncet")
    
def main():
    print("Calling iss ....")
    try:
        call_iss()
    except Exception as e:
        print(str(e))
    finally:
        print("Program Ended")

if __name__ == "__main__":
    main()