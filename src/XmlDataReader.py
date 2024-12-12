from xml.etree import ElementTree as ET
from Types import DataType
from DataReader import DataReader


# class XmlDataReader(DataReader):
#     def __init__(self) -> None:
#         self.students: DataType = {}

#     def read(self, path: str) -> DataType:
#         tree = ET.parse(path)
#         root = tree.getroot()

#         for student in root:
#             student_name = student.tag.strip()
#             self.students[student_name] = []

#             for subject in student:
#                 subject_name = subject.tag.strip()
#                 score = int(subject.text.strip())
#                 self.students[student_name].append((subject_name, score))

#         return self.students
class XmlDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        # Парсинг XML-файла
        tree = ET.parse(path)
        root = tree.getroot()

        for student in root.findall("student"):
            # Получаем имя студента из атрибута
            student_name = student.attrib["name"]
            self.students[student_name] = []

            for subject in student:
                # Имя предмета — тег, оценка — текст внутри тега
                subject_name = subject.tag.strip()
                score = int(subject.text.strip())
                self.students[student_name].append((subject_name, score))

        return self.students
