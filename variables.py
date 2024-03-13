from datetime import datetime, timedelta

# Get current time
now = datetime.utcnow()
minus_hour = now + timedelta(days=-1)
plus_hour = now + timedelta(hours=1)

# Format the time string in the desired format
formatted_time = now.strftime("%Y%m%dT%H:%M-0000")


def function_formatted_time(init_time):
  return init_time.strftime("%Y%m%dT%H:%M-0000")

oasis_api_string_url='http://oasis.caiso.com/oasisapi/SingleZip?'
oasis_api_string_queryname='PRC_LMP'
oasis_api_string_startdatetime=function_formatted_time(minus_hour)
oasis_api_string_enddatetime=function_formatted_time(plus_hour)
oasis_api_string_marketid='DAM'
oasis_api_string_node='BAYSHOR2_1_N001'