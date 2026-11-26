import math
import time

# --- Constants ---
EARTH_RADIUS_KM = 6371  # Mean radius of Earth in kilometers

# --- Helper Functions ---
def deg_to_rad(degrees):
    """Converts degrees to radians."""
    return degrees * math.pi / 180

def rad_to_deg(radians):
    """Converts radians to degrees."""
    return radians * 180 / math.pi

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculates the distance between two points on Earth using the Haversine formula.
    Returns distance in kilometers.
    """
    # Convert latitudes and longitudes from degrees to radians
    lat1_rad, lon1_rad = deg_to_rad(lat1), deg_to_rad(lon1)
    lat2_rad, lon2_rad = deg_to_rad(lat2), deg_to_rad(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = EARTH_RADIUS_KM * c
    return distance

def calculate_bearing(lat1, lon1, lat2, lon2):
    """
    Calculates the initial bearing (direction) from point 1 to point 2.
    Returns bearing in degrees (0-360, where 0 is North, 90 East, etc.).
    """
    # Convert latitudes and longitudes from degrees to radians
    lat1_rad, lon1_rad = deg_to_rad(lat1), deg_to_rad(lon1)
    lat2_rad, lon2_rad = deg_to_rad(lat2), deg_to_rad(lon2)

    dlon = lon2_rad - lon1_rad

    y = math.sin(dlon) * math.cos(lat2_rad)
    x = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(dlon)

    bearing_rad = math.atan2(y, x)
    bearing_deg = rad_to_deg(bearing_rad)
    
    # Normalize bearing to 0-360 degrees
    bearing_deg = (bearing_deg + 360) % 360
    return bearing_deg

def get_cardinal_direction(bearing_deg):
    """Converts a bearing in degrees to a cardinal direction string."""
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    # Add 22.5 to shift the sectors so N is centered around 0, NE around 45, etc.
    index = int((bearing_deg + 22.5) / 45)
    return directions[index]

# --- Main Simulation ---
def main():
    # --- TrekBro: Define your camp location (home point) ---
    # These are example coordinates (e.g., near Beyşehir Lake, Turkey)
    # In a real TrekBro system, this would be saved when you set up camp.
    camp_lat, camp_lon = 37.8136, 30.5660  # Example: Beyşehir Lake, Turkey
    print(f"TrekBro Camp Location Set: Latitude {camp_lat:.4f}, Longitude {camp_lon:.4f}\n")

    # --- Simulate current location (user moving away from camp) ---
    # We start slightly away from camp to demonstrate movement.
    current_lat, current_lon = camp_lat + 0.05, camp_lon + 0.08 # About 8-10 km away
    
    print("Simulating your journey. TrekBro will guide you back to camp.")
    print("-----------------------------------------------------------\n")

    # Simulate movement for a few steps
    for i in range(1, 6):
        # --- TrekBro: Calculate distance and bearing to camp ---
        # This is the core offline navigation logic.
        distance_to_camp = haversine_distance(current_lat, current_lon, camp_lat, camp_lon)
        bearing_to_camp = calculate_bearing(current_lat, current_lon, camp_lat, camp_lon)
        cardinal_direction = get_cardinal_direction(bearing_to_camp)

        print(f"Step {i}:")
        print(f"  Your current location: Lat {current_lat:.4f}, Lon {current_lon:.4f}")
        # This is the core TrekBro guidance:
        print(f"  TrekBro says: Camp is {distance_to_camp:.2f} km away, bearing {bearing_to_camp:.1f}° ({cardinal_direction}).")
        print(f"  -> Keep moving {cardinal_direction} to return to camp.")
        print("-" * 50)

        # Simulate moving closer to camp (or in a different direction)
        # In a real system, current_lat/lon would come from a GPS sensor.
        current_lat -= 0.01  # Move south
        current_lon -= 0.015 # Move west
        
        time.sleep(1.5) # Pause for readability

    print("\nSimulation complete. TrekBro's offline guidance helps you never get lost!")

if __name__ == "__main__":
    main()
