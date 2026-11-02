import datetime

class Purchase:

    @staticmethod
    def get_date_and_time():
        date_and_time = []

        now = datetime.datetime.now()

        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]

        for item in date:
            name = item[0]
            value = item[1](now)

            date_and_time.append(f'{name}: {value}')

        return date_and_time