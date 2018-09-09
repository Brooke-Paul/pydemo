class DateNoInstance:
    pass


if __name__ == '__main__':
    date = DateNoInstance.__new__(DateNoInstance)
    data = {"year": "2018", "month": "09", "day": "10"}
    for key, value in data.items():
        setattr(date, key, value)

    print("当前年份：" + date.year)
    print("当前月份：" + date.month)
    print("当前天数：" + date.day)
