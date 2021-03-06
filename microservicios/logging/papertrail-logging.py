import logging
import socket
from logging.handlers import SysLogHandler
class ContextFilter(logging.Filter):
    hostname = socket.gethostname()
    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True
syslog = SysLogHandler(address=('logsN.papertrailapp.com', XXXXX))
syslog.addFilter(ContextFilter())
format = '%(asctime)s %(hostname)s YOUR_APP: %(message)s'
formatter = logging.Formatter(format, datefmt='%b %d %H:%M:%S')
syslog.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(syslog)
logger.setLevel(logging.INFO)
logger.info("This is a message")
