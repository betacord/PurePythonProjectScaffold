from dataclasses import dataclass


@dataclass
class Lecturer:
    """Any conceptual class

    :param first_name: First name of the lecturer
    :type first_name: str
    :param last_name: Last name of the lecturer
    :type last_name: str
    :param position: Position of the lecturer
    :type position: str
    :param test_attr: any test attribute
    :type test_attr: class: `object`
    """

    first_name: str
    last_name: str
    position: str
    test_attr: object

    def get_description(self, quota: str) -> str:
        """Method returning description of lecturer

        :param quota: quota char
        :type quota: str
        :return: Full description
        :rtype: str
        """
        return f'First name: {quota}{self.first_name}{quota}, last name: {quota}{self.last_name}{quota}.'
