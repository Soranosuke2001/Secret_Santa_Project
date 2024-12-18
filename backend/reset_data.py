import json

if __name__ == "__main__":
    with open("data.json", "w") as f:
        default = {
            "sora": {
                "name": "sora",
                "login": False,
                "family": True,
                "chosen": False
            },
            "yura": {
                "name": "yura",
                "login": False,
                "family": True,
                "chosen": False
            },
            "billy": {
                "name": "billy",
                "login": False,
                "family": True,
                "chosen": False
            },
            "eiko": {
                "name": "eiko",
                "login": False,
                "family": True,
                "chosen": False
            },
            "sayoko": {
                "name": "sayoko",
                "login": False,
                "family": True,
                "chosen": False
            },
            "takanobu": {
                "name": "takanobu",
                "login": False,
                "family": True,
                "chosen": False
            },
            "aika": {
                "name": "aika",
                "login": False,
                "family": False,
                "chosen": False
            },
            "ritsuki": {
                "name": "ritsuki",
                "login": False,
                "family": False,
                "chosen": False
            },
            "ayano": {
                "name": "ayano",
                "login": False,
                "family": False,
                "chosen": False
            },
            "satoshi": {
                "name": "satoshi",
                "login": False,
                "family": False,
                "chosen": False
            }
        }

        json.dump(default, f, indent=4)
