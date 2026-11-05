events = [
    {'date': '2019-12', 'event': 'name1'},
    {'date': '2019-12', 'event': 'name2'},
    {'date': '2019-11', 'event': 'name3'},
    {'date': '2019-11', 'event': 'name4'},
    {'date': '2020-10', 'event': 'name5'},
    {'date': '2020-10', 'event': 'name6'},
    {'date': '2020-11', 'event': 'name5'},
    {'date': '2020-11', 'event': 'name6'},
    {'date': '2020-12', 'event': 'name7'},
    {'date': '2020-12', 'event': 'name8'},
    {'date': '2020-12', 'event': 'name9'},
]

result = {}
for item in events:
    year_str, month_str = item['date'].split('-')
    year, month = int(year_str), int(month_str)

    result.setdefault(year, {}).setdefault(month, []).append(item['event'])

print(result)