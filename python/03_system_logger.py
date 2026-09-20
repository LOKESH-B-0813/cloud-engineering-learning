 # 03_system_logger.py - Persistent Diagnostic Logging Utility
# Evolution of 02_live_system_metrics.py: Directs metrics to an automated log file.

import datetime
import shutil
import socket

# System metadata
server_name = socket.gethostname()
disk_limit = 80.0
is_production = True
log_filename = "system_health.log"
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
