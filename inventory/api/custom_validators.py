from bson.objectid import ObjectId
from pydantic import validator

class CustomValidators:
    @classmethod
    @validator("name")
    def validate_name(cls, value):
        """Validate that a name contains only alphabetic characters.

        Args:
            value (str): The input name to be validated.

        Raises:
            ValueError: If the name contains non-alphabetic characters.

        Returns:
            str: The validated name.
        """
        if not value.isalpha():
            raise ValueError("Name must contain only alphabetic characters")
        return value

    @classmethod
    @validator("email")
    def validate_email(cls, value):
        """Validate the format of an email address.

        Args:
            value (str): The input email address to be validated.

        Raises:
            ValueError: If the email address has an invalid format.

        Returns:
            str: The validated email address.
        """
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format")
        return value

    @classmethod
    @validator("phone_number")
    def validate_phone_number(cls, value):
        """Validate the format of a phone number.

        Args:
            value (str): The input phone number to be validated.

        Raises:
            ValueError: If the phone number has an invalid format.

        Returns:
            str: The validated phone number.
        """
        if not value.replace(" ", "").replace("-", "").isdigit():
            raise ValueError("Invalid phone number format")
        return value

    @classmethod
    @validator("zipcode")
    def validate_zipcode(cls, value):
        """Validate the format of a ZIP code.

        Args:
            value (str): The input ZIP code to be validated.

        Raises:
            ValueError: If the ZIP code has an invalid format.

        Returns:
            str: The validated ZIP code.
        """
        if not value.isdigit() or not (len(value) == 5 or len(value) == 9):
            raise ValueError("Invalid ZIP code format")
        return value

    @classmethod
    @validator("ssn")
    def validate_ssn(cls, value):
        """Validate the format of a Social Security Number (SSN).

        Args:
            value (str): The input SSN to be validated.

        Raises:
            ValueError: If the SSN has an invalid format.

        Returns:
            str: The validated SSN.
        """
        if not value.isdigit() or len(value) != 9:
            raise ValueError("Invalid Social Security Number (SSN) format")
        return value

    # Additional Validators for Models
    @classmethod
    @validator("year")
    def validate_year(cls, value):
        """Validate that a year is within a specified range.

        Args:
            value (int): The input year to be validated.

        Raises:
            ValueError: If the year is outside the valid range.

        Returns:
            int: The validated year.
        """
        if value < 1886 or value > 2050:
            raise ValueError("Invalid year. Must be between 1886 and 2050.")
        return value

    @classmethod
    @validator("vin")
    def validate_vin(cls, value):
        """Validate the format of a Vehicle Identification Number (VIN).

        Args:
            value (str): The input VIN to be validated.

        Raises:
            ValueError: If the VIN has an invalid format.

        Returns:
            str: The validated VIN.
        """
        if not value.isalnum() or len(value) != 17:
            raise ValueError("Invalid VIN format. Must be alphanumeric and 17 characters long.")
        return value.upper()

    @classmethod
    @validator("id")
    def validate_object_id(cls, value):
        """Validate the format of a MongoDB ObjectId.

        Args:
            value (str): The input ObjectId to be validated.

        Raises:
            ValueError: If the ObjectId has an invalid format.

        Returns:
            str: The validated ObjectId.
        """
        try:
            ObjectId(value)
        except ValueError:
            raise ValueError(f"Invalid ObjectId: {value}")
        return value
