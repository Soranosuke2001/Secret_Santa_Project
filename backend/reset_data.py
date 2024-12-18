import json

if __name__ == "__main__":
    with open("data.json", "w") as f:
        default = {
            "sora": {
                "name": "sora", 
                "login": False, 
                "family": True, 
                "paired": False
            },
            "yura": {
                "name": "yura", 
                "login": False, 
                "family": True, 
                "paired": False
            },
            "billy": {
                "name": "billy", 
                "login": False, 
                "family": True, 
                "paired": False
            },
            "eiko": {
                "name": "eiko", 
                "login": False, 
                "family": True, 
                "paired": False
            },
            "sayoko": {
                "name": "sayoko",
                "login": False,
                "family": True,
                "paired": False,
            },
            "takanobu": {
                "name": "takanobu",
                "login": False,
                "family": True,
                "paired": False,
            },
            "ayano": {
                "name": "ayano",
                "login": False,
                "family": False,
                "paired": False,
            },
            "satoshi": {
                "name": "satoshi",
                "login": False,
                "family": False,
                "paired": False,
            },
            "aika": {
                "name": "aika", 
                "login": False, 
                "family": False, 
                "paired": False
            },
            "ritsuki": {
                "name": "ritsuki",
                "login": False,
                "family": False,
                "paired": False,
            },
        }

        json.dump(default, f, indent=4)
