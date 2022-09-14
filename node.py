import json
from flask import Flask, jsonify
from flask_cors import CORS
from utility.wallet import Wallet
from utility.blockchain import Blockchain

app = Flask(__name__)
wallet = Wallet()
blockchain = Blockchain(wallet.public_key)
CORS(app)

@app.route('/', methods=['GET'])
def get_ui():
    return 'Hello'

@app.route('/chain', methods=['GET'])
def get_chain():
    data = blockchain.get_data()
    return jsonify([block.__dict__ for block in data]), 200

if __name__ == '__main__':
    app.run(host='localhost', port='3000')