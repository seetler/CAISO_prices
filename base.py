import sys
sys.path.append('C:\\Users\\JSNZE\\OneDrive\\Desktop\\packages')

import requests
import os
from datetime import datetime, timedelta
import zipfile
from apvariable import *


oasis_api_string= f"http://oasis.caiso.com/oasisapi/SingleZip?resultformat=6&queryname={oasis_api_string_queryname}&version=1&startdatetime={oasis_api_string_startdatetime}&enddatetime={oasis_api_string_enddatetime}&market_run_id={oasis_api_string_marketid}&node={oasis_api_string_node}"

print(oasis_api_string)


# Print the formatted time
print(formatted_time)

def download_file(url, local_folder):
  """
  Downloads a file from a URL and saves it to a local folder.

  Args:
      url (str): The URL of the file to download.
      local_folder (str): The path to the local folder where the file 
                          should be saved.
  """

  # Get the filename from the URL
  filename = "s.zip"

  # Create the local filepath
  local_filepath = os.path.join(local_folder, filename)

  # Send the GET request
  response = requests.get(oasis_api_string, stream=True)

  # Check for successful response (status code 200)
  if response.status_code == 200:
    # Create the local folder if it doesn't exist
    os.makedirs(local_folder, exist_ok=True)

    # Open the local file in write-binary mode
    with open(local_filepath, "wb") as f:
      for chunk in response.iter_content(chunk_size=1024):
        if chunk:  # filter out keep-alive new chunks
          f.write(chunk)
    print(f"File downloaded successfully: {local_filepath}")
  else:
    print(f"Download failed: Status code {response.status_code}")

# Example usage
url = "https://example.com/file.txt"  # Replace with your actual URL
local_folder = "downloads"  # Replace with your desired folder path

download_file(url, local_folder)



def unzip_file_no_with(filepath, destination_folder):
  """
  Unzips a downloaded file to a specified destination folder without using 'with'.

  **Caution:** This approach is less recommended than using 'with' due to potential 
  resource management issues. Use with caution and for learning purposes only.

  Args:
      filepath (str): The path to the downloaded zip file.
      destination_folder (str): The path to the folder where the extracted 
                                 files should be saved.
  """
  zip_ref = zipfile.ZipFile(filepath, 'r')
  try:
    zip_ref.extractall(destination_folder)
    print(f"Files extracted successfully to: {destination_folder}")
  finally:
    zip_ref.close()  # Ensure proper file closure even in case of exceptions

# Example usage
downloaded_file = "data.zip"  # Replace with your downloaded file name
destination_folder = "extracted_files"  # Replace with your desired folder

unzip_file_no_with("downloads/s.zip", destination_folder)