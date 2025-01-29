from baml_py import Image
from baml_client import b


def extract_appointment_from_url(url: str):
    """
    Extracts an image of an appointment card stored at a URL.

    Args:
        url (str): The URL of an appointment card image.

    Returns:
        dict: The appointment card data. See the baml_src/idp.baml file for the structure of the appointment data.

    Raises:
        BamlValidationError: If the llm read of the image could not be parsed into the expected data model.
    """
    img = Image.from_url(url)
    output = b.ExtractAppointmentFromImage(img)
    return output

def extract_nutrition_from_url(url: str):
    """
    Extracts an image of a nutritional value label stored at a URL.

    Args:
        url (str): The URL of a nutritional value label image.

    Returns:
        dict: The nutrition data. See the baml_src/idp.baml file for the structure of the nutritional value data.

    Raises:
        BamlValidationError: If the llm read of the image could not be parsed into the expected data model.
    """
    img = Image.from_url(url)
    output = b.ExtractNutritionLabelFromImage(img)
    return output

def extract_package_from_url(url: str):
    """
    Extracts an image of a nutritional value label stored at a URL.

    Args:
        url (str): The URL of a nutritional value label image.

    Returns:
        dict: The receipt data. See the baml_src/idp.baml file for the structure of the nutritional value data.

    Raises:
        BamlValidationError: If the llm read of the image could not be parsed into the expected data model.
    """
    img = Image.from_url(url)
    output = b.ExtractDropOffPackageReceiptFromImage(img)
    return output

def extract_info_from_url(url: str):
    """
    Extracts details from an image at a URL.

    Args:
        url (str): The URL of a nutritional value label image.

    Returns:
        dict: The data. See the baml_src/idp.baml file for the structure of the nutritional value data.

    Raises:
        BamlValidationError: If the llm read of the image could not be parsed into the expected data model.
    """
    img = Image.from_url(url)
    output = b.ChooseATool(img)
    return output