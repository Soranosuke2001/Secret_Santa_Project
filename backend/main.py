from flask import Flask, request
from flask_cors import CORS

from helper import read_log_config
from db_functions import create_db, delete_db, set_default, connect_db, check_user, get_random_name, get_chosen

logger = read_log_config()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

DB_SESSION = connect_db(logger)


@app.route('/user')
def user():
    username = request.args.get("username").lower()
    logger.info(f'Received Request with username: {username}')

    result = check_user(DB_SESSION, username)

    if result == "invalid":
        logger.info("Response: Invalid")
        return { "message": "invalid" }, 200

    if result == "completed":
        logger.info("Response: Completed")
        random_name = get_chosen(DB_SESSION, username)

        return { "message": "completed", "gifting": random_name.capitalize() }, 200

    logger.info("Response: Valid")
    return { "message": "valid" }, 200


@app.route('/roll')
def roll():
    username = request.args.get("username").lower()
    logger.info(f'Received Request with username: {username}')

    random_name = get_random_name(DB_SESSION, username)

    # choose a random name
    logger.info(f'Random name chosen: {random_name}')
    return { "message": random_name.capitalize() }, 200


if __name__ == "__main__":
    delete_db()
    create_db()
    set_default(DB_SESSION)
    app.run(host="0.0.0.0", port=8080, debug=True)