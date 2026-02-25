from flask import Flask
import os
app=Flask(__name__)

@app.route('/')
def hello():
     return f"سلام! من رو k3s دارم اجرا میشم. ورژن: {os.environ.get('VERSION', '1.0')}"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
