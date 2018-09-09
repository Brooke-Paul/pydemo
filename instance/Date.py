class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


if __name__ == '__main__':
    date = Date("2018", "09", "10")
    print("当前年份：" + date.year)
    print("当前月份：" + date.month)
    print("当前天数：" + date.day)
