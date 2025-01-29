import sys
import logging

from baml_client.sync_client import b
from baml_client.types import Resume
import baml_util as bu

def scan_receipt_url(url: str):
    """
    Submit a receipt image URL to be scanned and processed.

    - **Returns**: The filename, format, and metadata of the image.
    """

    try:
        output = bu.extract_appointment_from_url(url)
    except Exception as e:
        logging.error(e)
        return {"error": f"Failed to extract receipt from image: {e}"}
    return output

def main():
    """Main entry point for the script."""
    print(scan_receipt_url("https://baml-testing-idp-image-to-json.s3.us-east-1.amazonaws.com/appointment.jpg"))


if __name__ == '__main__':
    sys.exit(main())





__author__ = "Ednalyn C. De Dios, et al."
__copyright__ = "Copyright 2025, IDP with BAML Project"
__credits__ = ["Vaibahv @ BoundaryML"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Ednalyn C. De Dios"
__email__ = "ednalyn.dedios@gmail.com"
__status__ = "Prototype"