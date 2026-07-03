import json

try:
    with open("sprout_config.json", "r") as file:
        print("[SUCCESS] Config loaded successfully!")
        config = json.load(file)
except FileNotFoundError:
    print("[WARNING] Config missing. Generating factory settings")
    default_config = {
        "node_id": "Sprout_01",
        "moisture_min": 30,
        "active": True
    }
    with open("sprout_config.json", "w") as file:
        json.dump(default_config, file, indent=4)
        config = default_config