import socket
from uuid import getnode as get_mac
from flask import Flask,jsonify,render_template

# Get device details
def get_device_details():
	hostname = socket.gethostname()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	s.close()
	MAC_address = get_mac()
	MAC_address = (':'.join(("%012X" % MAC_address)[i:i+2] for i in range(0, 12, 2)) ).replace(":", "-")
	return hostname,ip,MAC_address
	
app = Flask(__name__)

@app.route("/")
def hello():
     return render_template('index.html')

# Returns device hostname,IP and MAC address
@app.route("/details")
def details():
    hostname,ip,mac = get_device_details()
    out = "Hola Phil I'm " + hostname + " and my MAC ID is " + mac + " & my IP address is "+ip
    return out

@app.route("/health")
def health():
    return jsonify(
        status="up"
    )

@app.route("/home")
def home():
    return "Hola Pappi! This is your first gitops argocd project."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
	