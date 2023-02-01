from demo_cli.models.student import Student


def test_student_dataclass_should_be_initialized_correctly() -> None:
    student = Student('Janusz', 'Badziewiak', '999876')

    assert (
        student.first_name == 'Janusz'
        and student.last_name == 'Badziewiak'
        and student.index_number == '999876'
    )
