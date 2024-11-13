import os
import platform
from datetime import datetime

import os
import platform
from datetime import datetime

data = {
    "Logged Info at": datetime.now().isoformat(),
    "OS Name": os.name,
    "Platform": platform.system(),
    "Platform Release": platform.release(),
    "Platform Version": platform.version(),
    "Machine": platform.machine(),
    "Processor": platform.processor(),
    "Current User": os.getlogin(),
    "Current Working Directory": os.getcwd(),
    "Environment Variables": dict(os.environ),
    "CPU Count": os.cpu_count(),
    "Process ID": os.getpid(),
    "Parent Process ID": os.getppid()
}
