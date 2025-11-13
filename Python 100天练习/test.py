from datetime import datetime
from zoneinfo import ZoneInfo
 
utc_time = datetime.now(ZoneInfo("UTC"))
beijing_time = utc_time.astimezone(ZoneInfo("Asia/Shanghai"))
print(f"UTC: {utc_time:%y-%m-%d %H:%M} | Beijing: {beijing_time:%Y-%m-%d %H:%M}")
