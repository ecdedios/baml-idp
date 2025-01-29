import sys
import logging

from baml_client.sync_client import b
from baml_client.types import Resume
import baml_util as bu

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/appointment")
def scan_appointment_url(url: str):
    """
    Submit an image URL of an appointment reminder card to be scanned and processed.

    - **Returns**: The filename, format, and metadata of the image.
    """

    try:
        output = bu.extract_appointment_from_url(url)
    except Exception as e:
        logging.error(e)
        return {"error": f"Failed to extract appointment details from image: {e}"}
    return output

@app.post("/nutrition")
def scan_nutrition_url(url: str):
    """
    Submit an image URL of a nutritional value label to be scanned and processed.

    - **Returns**: The filename, format, and metadata of the image.
    """

    try:
        output = bu.extract_nutrition_from_url(url)
    except Exception as e:
        logging.error(e)
        return {"error": f"Failed to extract nutritional value details from image: {e}"}
    return output

@app.post("/package")
def scan_package_url(url: str):
    """
    Submit an image URL of a drop off package receipt to be scanned and processed.

    - **Returns**: The filename, format, and metadata of the image.
    """

    try:
        output = bu.extract_package_from_url(url)
    except Exception as e:
        logging.error(e)
        return {"error": f"Failed to extract drop off package receipt information from image: {e}"}
    return output

@app.post("/tool")
def scan_image_url(url: str):
    """
    Submit an image URL to be scanned and processed.

    - **Returns**: The filename, format, and metadata of the image.
    """

    try:
        output = bu.extract_info_from_url(url)
    except Exception as e:
        logging.error(e)
        return {"error": f"Failed to extract information from image: {e}"}
    return output

def main():
    """Main entry point for the script."""
    print(scan_appointment_url("https://baml-testing-idp-image-to-json.s3.us-east-1.amazonaws.com/appointment.jpg"))
    print("\n\n")
    print(scan_nutrition_url("https://baml-testing-idp-image-to-json.s3.us-east-1.amazonaws.com/nutrition.jpg"))
    print("\n\n")
    print(scan_package_url("https://baml-testing-idp-image-to-json.s3.us-east-1.amazonaws.com/package.jpg"))


if __name__ == '__main__':
    sys.exit(main())





__author__ = "Ednalyn C. De Dios, et al."
__copyright__ = "Copyright 2025, IDP with BAML Project"
__credits__ = ["Vaibhav @ BoundaryML - https://www.linkedin.com/in/vaigup/"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Ednalyn C. De Dios"
__email__ = "ednalyn.dedios@gmail.com"
__status__ = "Prototype"