import json

def read_json():
    file_path = "data.json"
    try:
        with open(file_path, "r") as f:
            content = f.read()
            print(f"File content: {content}")
            return json.loads(content)
    except FileNotFoundError:
        print("File not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return {}
    except Exception as e:
        print(f'There was an error {e}')


def write_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
