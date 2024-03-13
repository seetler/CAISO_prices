import sys
from variables import *

sys.path.append(syspathlocal)

import requests
import os
from datetime import datetime, timedelta
from zipfile import ZipFile
import zipfile
import pandas as pd


oasis_api_string= f"http://oasis.caiso.com/oasisapi/SingleZip?resultformat=6&queryname={oasis_api_string_queryname}&version=1&startdatetime={oasis_api_string_startdatetime}&enddatetime={oasis_api_string_enddatetime}&market_run_id={oasis_api_string_marketid}&node={oasis_api_string_node}"

print(oasis_api_string)

def download_file(local_folder):

  filename = "temp.zip"

  local_filepath = os.path.join(local_folder, filename)
  response = requests.get(oasis_api_string, stream=True)


  if response.status_code == 200:
    os.makedirs(local_folder, exist_ok=True)

    with open(local_filepath, "wb") as f:
      for chunk in response.iter_content(chunk_size=1024):
        if chunk:  # filter out keep-alive new chunks
          f.write(chunk)
    print(f"File downloaded successfully: {local_filepath}")
  else:
    print(f"Download failed: Status code {response.status_code}")


local_folder = "downloads"  # Replace with your desired folder path
download_file(local_folder)





# pd.read_csv('downloads/ba.csv')


def unzip_and_rename(zip_file_path, new_csv_name):
  """
  Unzips a zip file, renames the first encountered CSV file inside, 
  and overwrites existing files with the same name.

  Args:
      zip_file_path: Path to the zip file.
      new_csv_name: The desired name for the extracted CSV file (without extension).
  """
  with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    for member in zip_ref.namelist():
      if member.lower().endswith('.csv'):
        csv_filename = os.path.basename(member)
        new_filename = f"{new_csv_name}.csv"
        # Extract to the same directory as the zip file (overwrite if exists)
        zip_ref.extract(member, os.path.dirname(zip_file_path))
        try:
          os.remove('downloads/renamed_data.csv')
        except Exception:
          pass



        # Rename the extracted file
        os.rename(os.path.join(os.path.dirname(zip_file_path), csv_filename), 
                  os.path.join(os.path.dirname(zip_file_path), new_filename))
        break  # Only rename the first encountered CSV

# Example usage
zip_file_path = "downloads/temp.zip"
new_csv_name = "renamed_data"
unzip_and_rename(zip_file_path, new_csv_name)
print(f"CSV file extracted and renamed to {new_csv_name}.csv (Overwrites existing)")

now = datetime.utcnow()

pdcsvname='bas.csv'
data2 = pd.read_csv('downloads/renamed_data.csv')
df3=data2.drop(['INTERVALSTARTTIME_GMT', 'INTERVALENDTIME_GMT'], axis='columns')
df3['timestamp'] = now
df3.to_csv(pdcsvname, index=False, header=False)

print(f"Readied to {pdcsvname}")
# sudo apt install python3-pandas