from settings import ALLOWED_IMG_EXTENSIONS


def allowed_file(filename: str) -> bool:
    """
    Validates the uploaded file
    Currently very basic... :)
    :param filename: The filename
    :return: True if allowed, else False
    """
    extension = filename.split(".")[-1]
    return extension in ALLOWED_IMG_EXTENSIONS
