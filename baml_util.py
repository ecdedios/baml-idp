from baml_py import Image
from baml_client import b


def extract_appointment_from_url(url: str):
    """
    Extracts an image of a receipt stored at a URL.

    Args:
        url (str): The URL of the receipt image.

    Returns:
        dict: The receipt data. See the baml_src/idp.baml file for the structure of the appointment data.

    Raises:
        BamlValidationError: If the llm read of the image could not be parsed into the expected data model.
    """
    img = Image.from_url(url)
    output = b.ExtractAppointmentFromImage(img)
    return output


def extract_appointment_from_base64(base64: str):
    """Extract a receipt from a base 64 image file.

    Args:
        base64 (str): Base64 string encoded image

    Returns:
        dict: The receipt data. See the baml_src/idp.baml file for the structure of the appointment data.

    Raises:
        BamlValidationError: If the llm read of the image could not be parsed into the expected data model.
    """

    img_64 = Image.from_base64("image/png", base64)
    output = b.ExtractAppointmentFromImage(img_64)
    return output