import logging
import random
from flask import Flask
from flask import request
from flask_cors import CORS

from helper import read_json, write_json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

logging.basicConfig(filename='app.log', level=logging.DEBUG)

@app.route('/check/user')
def create_user():
    username = request.args.get("username").lower()
    app.logger.info(f'Received Request with username: {username}')

    names = read_json()

    if names == {}:
        return { "message": "invalid" }, 200

    if username in names.keys():
        # set the login to true
        if not names[username]["login"]:
            names[username]["login"] = True
            write_json(names)

            app.logger.info("Response: Valid")
            return { "message": "valid" }, 200
        
        app.logger.info("Response: Completed")
        return { "message": "completed" }, 200

    app.logger.info("Response: Invalid")
    return { "message": "invalid" }, 200

@app.route('/roll')
def roll():
    username = request.args.get("username").lower()
    app.logger.info(f'Received Request with username: {username}')

    # read the json file
    names = read_json()

    # check if the username is part of family
    if names[username]["family"]:
        # create a list of all names possible (not chosen yet and excluding self)
        options = []
        for name in names:
            if name == username:
                continue

            if names[name]["chosen"]:
                continue
            
            options.append(name)
    
        # choose a random name
        random_name = random.choice(options)
        app.logger.info(f'Names available: {options}')
        app.logger.info(f'Random name chosen: {random_name}')

        # set the chosen to true for random name
        names[random_name]["chosen"] = True

        # overwrite the json file
        write_json(names)

        # return the random name
        return { "message": random_name.capitalize() }, 200
    
    # if the username is not part of family
    else:
        # create a list of all names possible (not chosen yet and excluding self and part of family)
        options = []
        for name in names:
            if name == username:
                continue
                
            if names[name]["chosen"]:
                continue
                
            if not names[name]["family"]:
                continue
                
            options.append(name)

        # choose a random name
        random_name = random.choice(options)
        app.logger.info(f'Names available: {options}')
        app.logger.info(f'Random name chosen: {random_name}')

        # set the chosen to true for random name
        names[random_name]["chosen"] = True

        # overwrite the json file
        write_json(names)

        # return the random name
        return { "message": random_name.capitalize() }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)