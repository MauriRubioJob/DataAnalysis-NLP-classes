import datetime


current = datetime.datetime.now()
print(current)

custom = datetime.datetime(year=2021, month=1, day=1, hour=12)
print(custom)


if current > custom:
    print("Today is after the 1st of January 2021")
else:
    print("Before 1st of January 2021")


difference = custom - current
print(type(difference))


fifty_days = datetime.timedelta(days=50, hours=12)
ten_days = datetime.timedelta(days=10)

sixty_days = fifty_days + ten_days

hundred_twenty_days = sixty_days * 2

print(current + hundred_twenty_days)
