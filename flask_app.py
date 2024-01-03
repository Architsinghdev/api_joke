# Save this code in a file named `app.py`

from flask import Flask, request, jsonify

app = Flask(__name__)

def save_to_file(data):
    with open("received_info.txt", "a") as file:
        file.write(str(data) + "\n")

@app.route('/receive_info', methods=['POST'])
def receive_info():
    data = request.get_json()

    # You can process the received data as needed
    # For now, let's just print it and save it to a text file
    print("Received information:", data)

    # Save the information to a text file
    save_to_file(data)

    return jsonify({"message": "Information received successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
