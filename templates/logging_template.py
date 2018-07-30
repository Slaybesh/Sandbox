import logging

log_filter = ''
log_level = logging.INFO
#region logging
logging_filter = logging.Filter(log_filter)

levels = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL}

formatter = logging.Formatter('%(levelname)s: line %(lineno)d: %(name)s: %(message)s')
formatter_date = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: line %(lineno)d: %(message)s", "%d.%m.%y %H:%M:%S")

file_handler = logging.FileHandler('{}.errorlog'.format(__name__))
file_handler.setLevel(logging.error)
file_handler.setFormatter(formatter_date)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(log_level)
stream_handler.addFilter(logging_filter)

error_stream_handler = logging.StreamHandler()
error_stream_handler.setFormatter(formatter)
error_stream_handler.setLevel(logging.ERROR)

loggers = {}
def get_logger(name):

    if name not in loggers:

        new_logger = logging.getLogger(name)

        new_logger.propagate = False
        new_logger.setLevel(log_level)
        new_logger.addHandler(file_handler)
        new_logger.addHandler(stream_handler)
        if log_filter:
            new_logger.addHandler(error_stream_handler)

        loggers[name] = new_logger

    return loggers[name]
#endregion logging
