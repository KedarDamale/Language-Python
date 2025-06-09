# ========================================================
# DETAILED EXPLANATION OF `requests` MODULE IN PYTHON
# ========================================================

# The requests module is a powerful, user-friendly HTTP library for Python.
# It allows sending HTTP requests (GET, POST, PUT, DELETE, etc.) to interact with web services or APIs.

import requests  # This is a third-party module. Install via: pip install requests

# ------------------------------------------
# ✅ 1. HTTP GET Request (Fetching Data)
# ------------------------------------------

# Let's use a public API: PokeAPI to demonstrate GET request
# It returns data about Pokémon in JSON format

base_url = "https://pokeapi.co/api/v2/pokemon/"

# Define the name of the Pokémon
pokemon_name = input("Enter Pokémon name: ").strip().lower()

# Create the full endpoint URL
url = f"{base_url}{pokemon_name}"

# Send GET request
response = requests.get(url)  # This sends a GET request to the server

# Check the response status
if response.status_code == 200:
    print("✅ Request was successful!")
    
    # Convert JSON response into a Python dictionary
    data = response.json()

    # Display basic information
    print("\n========= Pokémon Info =========")
    print(f"Name       : {data['name']}")
    print(f"ID         : {data['id']}")
    print(f"Height     : {data['height']} decimetres")
    print(f"Weight     : {data['weight']} hectograms")

    # List Abilities
    print("\nAbilities:")
    for item in data['abilities']:
        print(f" - {item['ability']['name']} {'(Hidden)' if item['is_hidden'] else ''}")

    # List Types
    print("\nTypes:")
    for item in data['types']:
        print(f" - {item['type']['name']}")

    # Sprite Image
    print(f"\nSprite URL : {data['sprites']['front_default']}")
else:
    print(f"❌ Error! Status code: {response.status_code}")

# ------------------------------------------
# ✅ 2. Exploring `requests` Response Object
# ------------------------------------------

# Response Object has many attributes:
# response.status_code    → HTTP Status (200 OK, 404 Not Found, etc.)
# response.text           → Raw text content (HTML/JSON as string)
# response.json()         → Parse JSON into Python dict
# response.content        → Raw bytes (used for images or files)
# response.headers        → Dictionary of response headers
# response.url            → Final URL (after redirection)
# response.ok             → True if status_code is 200–399
# response.elapsed        → Time taken to get response
# response.encoding       → Encoding (usually 'utf-8')

print("\n========= Meta Info =========")
print(f"Raw Text       : {response.text[:80]}...")  # Only printing first 80 characters
print(f"Final URL      : {response.url}")
print(f"Content-Type   : {response.headers['Content-Type']}")
print(f"Request OK?    : {response.ok}")
print(f"Response Time  : {response.elapsed.total_seconds()}s")

# ------------------------------------------
# ✅ 3. Error Handling — Always Use This!
# ------------------------------------------

# Best Practice: wrap requests in try-except block to handle network failures

try:
    r = requests.get("https://pokeapi.co/api/v2/pokemon/invalidmon")
    r.raise_for_status()  # Raises HTTPError for bad responses
except requests.exceptions.HTTPError as e:
    print(f"🛑 HTTP error occurred: {e}")
except requests.exceptions.ConnectionError:
    print("🔌 Connection error! Check your internet or the URL.")
except requests.exceptions.Timeout:
    print("⏱️ Timeout error! The server took too long to respond.")
except requests.exceptions.RequestException as e:
    print(f"❗ General error: {e}")

# ------------------------------------------
# ✅ 4. Other HTTP Methods (POST, PUT, DELETE)
# ------------------------------------------

# For APIs that accept data input, we use POST/PUT
# For now we just show syntax since PokeAPI is read-only

# POST Example (e.g., sending JSON data):
# payload = {"name": "Kedar", "score": 98}
# r = requests.post("http://example.com/submit", json=payload)

# PUT Example (update resource):
# r = requests.put("http://example.com/user/1", json=updated_data)

# DELETE Example (delete resource):
# r = requests.delete("http://example.com/user/1")

# ------------------------------------------
# ✅ 5. Headers, Params, Timeouts, etc.
# ------------------------------------------

# Custom headers (e.g., Auth token)
# headers = {'Authorization': 'Bearer YOUR_TOKEN_HERE'}
# r = requests.get(url, headers=headers)

# Query parameters
# r = requests.get("http://example.com/data", params={"page": 2, "size": 10})

# Set timeout (avoid hanging forever)
# r = requests.get("http://example.com", timeout=5)

# Download binary files (like images or PDFs)
# img = requests.get("http://example.com/image.jpg")
# with open("image.jpg", "wb") as f:
#     f.write(img.content)

# ========================================================
# SUMMARY: What You've Learned
# ========================================================

# ✅ Making GET requests with `requests.get()`
# ✅ Handling JSON data with `.json()`
# ✅ Response attributes like status_code, text, headers
# ✅ Exception handling for failed HTTP calls
# ✅ POST, PUT, DELETE method usage
# ✅ Adding headers, query parameters, and timeouts
# ✅ Downloading images/files

# This makes you capable of building any API-interacting client in Python!
