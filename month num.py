import datetime
month_name = "Jan"
datetime_object = datetime.datetime.strptime(month_name, "%b")
month_number = datetime_object.month
print(month_number)
month_number = "3"
datetime_object = datetime.datetime.strptime(month_number, "%m")
month_name = datetime_object.strftime("%b")
print(month_name)