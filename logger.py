import logging

date_format = '%Y-%m-%d %H:%M:%S'
message_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(
    level=logging.DEBUG,
    format=message_format,
    datefmt=date_format
)

mpl_logger = logging.getLogger('matplotlib')
mpl_logger.setLevel(logging.WARNING)

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
console_handler = logging.StreamHandler()
errors_file_handler = logging.FileHandler('logs/errors.log')
all_logs_file_handler = logging.FileHandler('logs/all.log')

# Set levels for handlers
console_handler.setLevel(logging.WARN)
errors_file_handler.setLevel(logging.WARN)
all_logs_file_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
console_format = logging.Formatter(message_format, datefmt=date_format)
file_format = logging.Formatter(message_format, datefmt=date_format)

# Add formats to handlers
console_handler.setFormatter(console_format)
errors_file_handler.setFormatter(file_format)
all_logs_file_handler.setFormatter(file_format)

# Add handlers to the logger
# logger.addHandler(console_handler)
logger.addHandler(errors_file_handler)
logger.addHandler(all_logs_file_handler)
