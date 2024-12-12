from Types import DataType

RatingType = dict[str, float]


class XmlCalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}
        self.good_students_count: int = 0

    def calc(self) -> RatingType:
        for key in self.data:
            # self.rating[key] = 0.0
            is_good_student = True  # Предполагаем, что студент — хорошист
            for subject in self.data[key]:
                score = subject[1]
                # self.rating[key] += score
                if score < 76:
                    is_good_student = False
            # self.rating[key] /= len(self.data[key])

            if is_good_student:
                self.good_students_count += 1  # Увеличиваем счётчик хорошистов

        return self.good_students_count
