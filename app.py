from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    try:
        pod_ip = socket.gethostbyname(hostname)
    except Exception:
        pod_ip = "unavailable"

    html = f"""
    <html>
    <head>
        <title>Python Web App on Kubernetes</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding-top: 60px;
            }}
            .card {{
                display: inline-block;
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            }}
            h1 {{
                color: #2c3e50;
            }}
            .label {{
                color: #7f8c8d;
                font-size: 14px;
            }}
            .value {{
                color: #2980b9;
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 15px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello from Kubernetes!</h1>
            <p class="label">Served by Pod Hostname</p>
            <p class="value">{hostname}</p>
            <p class="label">Pod IP Address</p>
            <p class="value">{pod_ip}</p>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
