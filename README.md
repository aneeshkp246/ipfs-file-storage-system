# BlockShareCloud : Blockchain-Based Decentralized Cloud Storage System

This project implements a simple decentralized cloud file sharing system using Flask, IPFS, and Blockchain technology. Users can upload files, which are stored securely on IPFS with metadata recorded on a blockchain for traceability.

## Setup

### 1. Clone the repository:
```bash
git clone https://github.com/aneeshkp246/ipfs-file-storage-system
cd ipfs-file-storage-system
```
### 2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
# On Windows use `venv\Scripts\activate`
```
### 3. Install the dependencies:
```bash
pip install -r requirements.txt
```
### 4. Create the necessary directories: 
```bash
mkdir uploads downloads
```
### 5. Ensure IPFS is running:
```bash
ipfs daemon
```
### 6. Run the application:
```bash
python app.py
```
### 7. To access the application, open your browser and go to:
```bash
http://127.0.0.1:5000/
```

## Features
- **File Upload:** Users can upload files via a simple web interface, and these files are stored on IPFS.
- **Blockchain Storage:** Metadata such as the file name and IPFS hash is stored on a simple blockchain for traceability.
- **File Download:** Users can download files by providing the IPFS hash, and the file is served with its original name and extension.
- **Flask Web Framework:** The application is built with Flask, offering an easy-to-use structure.
- **IPFS for Decentralized Storage:** Files are stored in a distributed manner using IPFS.

## How It Works

### 1. File Upload:

- When a user uploads a file, it is saved temporarily in the uploads folder.
- The file is uploaded to IPFS, and its hash is returned.
- The hash and the original file name are recorded on the blockchain.

### 2. Blockchain:

- A simple blockchain implementation records details about each file (IPFS hash and file name).
- The blockchain ensures the integrity and traceability of the file metadata.

### 3. File Download:

- The user provides the IPFS hash to download the file.
- The system fetches the file from IPFS and saves it to the downloads folder.
- The downloaded file is renamed to its original file name with the correct extension based on metadata stored in the blockchain.

## Example Usage

### Uploading a File:
1. Go to the web interface.
2. Upload a file through the provided form.
3. After uploading, you will receive an IPFS hash for the file.

### Downloading a File:
1. Provide the IPFS hash in the download form.
2. The system retrieves the file from IPFS and serves it for download with its original name and extension.

## Notes
- Make sure the IPFS daemon is running locally on port 5001 (default for IPFS).
- The blockchain is a simple in-memory structure and does not persist between server restarts.
