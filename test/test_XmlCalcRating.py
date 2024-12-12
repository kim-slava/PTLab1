import pytest
from src.Types import DataType
from src.XmlCalcRating import XmlCalcRating
from src.XmlDataReader import XmlDataReader

RatingsType = dict[str, float]


class TestXmlCalcRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91),
                ("химия", 100),
                ("русский язык", 85),
                ("литература", 90)
            ],
            "Петров Петр Семенович": [
                ("математика", 76),
                ("химия", 72),
                ("литература", 80),
                ("физика", 90)
            ],
            "Сидоров Сидр Сидорович": [
                ("математика", 82),
                ("химия", 79),
                ("литература", 88),
                ("программирование", 91)
            ],
            "Кузнецова Анна Викторовна": [
                ("математика", 92),
                ("литература", 84),
                ("физика", 78),
                ("химия", 93)
            ],
            "Михайлов Сергей Олегович": [
                ("математика", 75),
                ("химия", 82),
                ("физика", 70),
                ("математика", 88)
            ]
        }

        # Ожидаемое количество хорошистов: 3
        good_students_count = 3

        return data, good_students_count

    def test_init_xml_calc_rating(self,
                                  input_data: tuple[DataType, int]) -> None:
        calc_rating = XmlCalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, int]) -> None:
        calc_rating = XmlCalcRating(input_data[0])
        good_students_count = calc_rating.calc()

        # Проверяем, что количество хорошистов совпадает с ожидаемым
        assert good_students_count == input_data[1]
