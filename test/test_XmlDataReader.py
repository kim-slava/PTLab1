import pytest
from src.Types import DataType
from src.XmlDataReader import XmlDataReader


class TestXmlDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        xml_content = """<?xml version="1.0" encoding="UTF-8" ?>
<root>
  <student name="Иванов Константин Дмитриевич">
    <математика>91</математика>
    <химия>100</химия>
    <физика>85</физика>
    <литература>90</литература>
  </student>
  <student name="Петров Петр Семенович">
    <математика>76</математика>
    <химия>78</химия>
    <литература>80</литература>
    <физика>90</физика>
  </student>
  <student name="Сидоров Сидр Сидорович">
    <математика>82</математика>
    <химия>79</химия>
    <литература>88</литература>
    <программирование>91</программирование>
  </student>
  <student name="Кузнецова Анна Викторовна">
    <математика>92</математика>
    <литература>84</литература>
    <физика>78</физика>
    <химия>93</химия>
  </student>
  <student name="Михайлов Сергей Олегович">
    <математика>75</математика>
    <химия>82</химия>
    <физика>70</физика>
    <математика>88</математика>
  </student>
</root>
"""
        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100), ("физика", 85), ("литература", 90)
            ],
            "Петров Петр Семенович": [
                ("математика", 76), ("химия", 78), ("литература", 80), ("физика", 90)
            ],
            "Сидоров Сидр Сидорович": [
                ("математика", 82), ("химия", 79), ("литература", 88), ("программирование", 91)
            ],
            "Кузнецова Анна Викторовна": [
                ("математика", 92), ("литература", 84), ("физика", 78), ("химия", 93)
            ],
            "Михайлов Сергей Олегович": [
                ("математика", 75), ("химия", 82), ("физика", 70), ("математика", 88)
            ]
        }
        return xml_content, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("students.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XmlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]