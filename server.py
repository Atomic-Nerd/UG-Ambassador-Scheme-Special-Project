from flask import Flask, jsonify, request

app = Flask(__name__)

maze_file = "maze.txt" 

with open(maze_file, "r", encoding="utf-8") as f:
    maze_2d = [list(line.rstrip("\n")) for line in f]

class User:
    def __init__(self, username):
        self.username = username
        self.pos = Coords(1,1)
        self.finished = False 

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

user_dict = {}

@app.route('/register', methods=['POST'])
def register():
    # Get JSON data safely
    data = request.get_json(silent=True) or {}
    username = data.get('username', None)

    # Use the request IP
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    if ip in user_dict:
        return jsonify({"status": "failed", "reason": "IP already registered"}), 400
    elif not username:
        return jsonify({"status": "failed", "reason": "Missing username"}), 400
    else:
        user_dict[ip] = User(username)
        return jsonify({"status": "success", "message": f"User {username} registered"}), 201
    
@app.route('/map', methods=['GET'])
def map():
    # Get client IP
    ip = request.remote_addr
    
    if ip not in user_dict:
        return jsonify({"status": "failed", "reason": "IP not registered"}), 403
    
    # Return professional JSON structure
    response = {
        "status": "success",
        "data": {
            "map": maze_2d,
            "user" : user_dict[ip].username
        }
    }
    return jsonify(response), 200

# Global error handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({"status": "error", "error": "Not Found"}), 404

# Internal error handler
@app.errorhandler(500)
def server_error(e):
    return jsonify({"status": "error", "error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run()