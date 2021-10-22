# -*- coding: UTF-8 -*-

import os
import time
from datetime import datetime
from dateutil.tz import gettz

st = os.stat("s4_os_2_path.py")
print(st)

tpe_tz = gettz("Asia/Taipei")

# time.localtime([ sec ]): convert number of seconds to local time
time_local = time.localtime(st.st_mtime)
print()
print(time.strftime("%Y-%m-%d %H:%M:%S %z", time_local))

print("datetime tzinfo: " , datetime.now().tzinfo) # default tz=None

# datetime.fromtimestamp(timestamp, tz): create datetme object from timestamp
mtime = datetime.fromtimestamp(st.st_mtime, tpe_tz)
print(mtime.strftime("%Y-%m-%d %H:%M:%S %z"))
