from datetime import datetime, timedelta

# Get current time
now = datetime.utcnow()
minus_time = now + timedelta(hours=-1)
plus_time = now + timedelta(days=+2)

# Format the time string in the desired format
formatted_time = now.strftime("%Y%m%dT%H:%M-0000")


def function_formatted_time(init_time):
  return init_time.strftime("%Y%m%dT%H:%M-0000")

oasis_api_string_url='http://oasis.caiso.com/oasisapi/SingleZip?'
oasis_api_string_queryname='PRC_LMP'
oasis_api_string_startdatetime=function_formatted_time(minus_time)
oasis_api_string_enddatetime=function_formatted_time(plus_time)
oasis_api_string_marketid='DAM'
oasis_api_string_node='EMBRCDR_2_N104,STATIN-L_7_N001,CATALYST_7_N002'
syspathlocal='C:\\Users\\JSNZE\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\site-packages'