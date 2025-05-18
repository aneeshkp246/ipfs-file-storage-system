from flask import Flask, request, render_template, send_file
import os
from ipfs import IPFSClient
from blockchain import Blockchain

app = Flask(__name__)
ipfs_client = IPFSClient()
blockchain = Blockchain()
UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'

# Ensure upload and download directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    print(f"[Upload] File saved locally: {file_path}")
    
    # Upload to IPFS
    ipfs_hash = ipfs_client.upload_file(file_path)
    print(f"[Upload] File uploaded to IPFS: {ipfs_hash}")
    
    # Store in blockchain
    blockchain.create_block(len(blockchain.chain), {'file_name': file.filename, 'ipfs_hash': ipfs_hash})
    return 'File uploaded and stored in IPFS! Hash: ' + ipfs_hash

@app.route('/download', methods=['POST'])
def download_file():
    ipfs_hash = request.form['ipfs_hash']
    print(f"[Download] Requested IPFS hash: {ipfs_hash}")
    
    # Search for the block with the given IPFS hash to retrieve the original filename
    original_filename = None
    for block in blockchain.chain:
        if block.data.get('ipfs_hash') == ipfs_hash:
            original_filename = block.data.get('file_name')
            break
    
    if original_filename is None:
        print("[Download] Error: IPFS hash not found in the blockchain.")
        return 'Error: IPFS hash not found in the blockchain.'

    # Download the file from IPFS and save it locally in the 'downloads' folder
    file_path = ipfs_client.download_file(ipfs_hash, DOWNLOAD_FOLDER)
    print(f"[Download] File downloaded from IPFS to: {file_path}")

    if not os.path.exists(file_path):
        print(f"[Download] Error: File {ipfs_hash} not found in local storage!")
        return f'Error: File {ipfs_hash} not found in local storage!'

    # Rename the downloaded file to its original filename with extension
    final_file_path = os.path.join(DOWNLOAD_FOLDER, original_filename)
    os.rename(file_path, final_file_path)
    print(f"[Download] File renamed to: {final_file_path}")

    # Serve the file for download with the original filename and extension
    return send_file(final_file_path, as_attachment=True, download_name=original_filename)

if __name__ == '__main__':
    app.run(debug=True)