import requests
import os
import json

class IPFSClient:
    def __init__(self, host='127.0.0.1', port=5001):
        self.api_url = f'http://{host}:{port}/api/v0'

    def upload_file(self, file_path):
        """
        Upload a file to IPFS
        Returns the IPFS hash of the uploaded file
        """
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(f'{self.api_url}/add', files=files)
            
            if response.status_code != 200:
                raise Exception(f"IPFS upload failed with status code: {response.status_code}")
            
            # Parse the JSON response to get the hash
            result = json.loads(response.text)
            return result['Hash']

    def download_file(self, ipfs_hash, download_folder):
        """
        Download a file from IPFS by its hash
        Returns the path to the downloaded file
        """
        # Create the download folder if it doesn't exist
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
            
        # Download the file from IPFS
        response = requests.post(
            f'{self.api_url}/cat', 
            params={'arg': ipfs_hash},
            stream=True
        )
        
        if response.status_code != 200:
            raise Exception(f"IPFS download failed with status code: {response.status_code}")
        
        # Save the file to the specified path
        file_path = os.path.join(download_folder, ipfs_hash)
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    
        return file_path