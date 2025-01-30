class Human:
    """
    Клас опису людини

    Attributes:
        gender (str): cтать
        age (int): вік
        first_name (str): ім'я
        last_name (str): прізвище
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        """
        Ініціалізує екземпляр класу Human

        Parameters:
            gender (str): стать
            age (int): вік
            first_name (str): ім'я
            last_name (str): прізвище
        """
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        Повертає представлення об'єкта Human у str.

        Returns:
            str: інформація про людину
        """
        return f"{self.first_name} {self.last_name}, Вік: {self.age}, {self.gender}"


class Student(Human):
    """
    Клас опису студента, успадкований від класу Human

    Attributes:
        record_book (str): номер студентського квитка
    """

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        """
        Ініціалізує екземпляр класу Student

        Parameters:
            gender (str): стать студента
            age (int): вік студента
            first_name (str): ім'я студента
            last_name (str): прізвище студента
            record_book (str): номер студентського квитка
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        """
        Повертає представлення об'єкта Student у str

        Returns:
            str: інформація про студента
        """
        return f"Студент: {super().__str__()}, Студ. квиток: {self.record_book}"


class GroupError(Exception):
    """
    Виняток, що виникає при спробі додати до групи більше ніж 10 студентів
    """

    def __str__(self):
        return "Група заповнена! (max 10)"


class Group:
    """
    Клас опису групи студентів з обмеженням на кількість студентів

    Attributes:
        number (str): номер групи
        group (set): студенти які є в групі
    """

    def __init__(self, number: str):
        """
        Ініціалізує екземпляр класу Group

        Parameters:
            number (str): номер групи
        """
        self.number = number
        self.group = set()
        self.max_size = 10

    def add_student(self, student: Student):
        """
        Додає студента до групи

        Parameters:
            student (Student): об'єкт класу Student, який додається до групи

        Raises:
            GroupError: якщо група вже містить максимальну кількість студентів
        """
        if len(self.group) >= self.max_size:
            raise GroupError()
        self.group.add(student)

    def delete_student(self, last_name: str):
        """
        Видаляє студента з групи за прізвищем

        Parameters:
            last_name (str): прізвище студента, якого потрібно видалити
        """
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name: str) -> Student | None:
        """
        Знаходить студента по прізвищу

        Parameters:
            last_name (str): прізвище студента

        Returns:
            Student | None: об'єкт класу Student - якщо знайдений, або None
        """
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        """
        Повертає представлення об'єкта Group у str

        Returns:
            str: інформація про групу та студентів у ній
        """
        all_students = "\n".join(str(student) for student in self.group)
        return f"Номер групи: {self.number}\nСтуденти:\n{all_students}"


st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")

st11 = Student("Male", 20, "Test", "Name", "AN153")

gr = Group("PD1")

try:
    for i in range(10):
        st = Student("Male", 20 + i, f"Ім'я {i + 1}", "Прізвище" + str(i + 1), "AN15" + str(i + 1))
        gr.add_student(st)
    gr.add_student(st11)
except GroupError as e:
    print(f"Помилка: {e}")

print(gr)
