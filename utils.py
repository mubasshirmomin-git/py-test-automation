
class Utils:
    """
    class for utility methods
    """
    @staticmethod
    def convertNULLtoInteger(value):
        """
        This function will convert value to integer if it has integer value
        otherwise if will return 0 but not error
        """
        return value if value.isdigit() else 0
