import sys

from demo_cli.models.student import Student


def main() -> int:
    student = Student('Janusz', 'Badziewiak', '129776')
    student.index_number = '0'

    return 0


if __name__ == '__main__':
    sys.exit(main())
