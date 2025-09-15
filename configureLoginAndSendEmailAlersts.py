import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

smtp_handler = logging.handlers.SMTPHandler(
    mailhost=("smtp.gmail.com","587"),
    fromaddr='<sender email>',
    toaddrs="<receiver email>",
    subject="Critical Error Detected",
    credentials=('sender email','<password>'),
    secure=()
)
smtp_handler.setLevel(logging.CRITICAL)
smtp_handler.setFormatter(formatter)

logger.addHandler(smtp_handler)

try:
    raise ValueError('A Critical error occured')
except ValueError as e:
    logger.critical(f"ValueError : {e}",exc_info=True)