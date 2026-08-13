# datetime is a built in function in python used to get date and time
import datetime
current_date = datetime.datetime.today().date()
current_time=datetime.datetime.today().time()
current_datetime= datetime.datetime.today()
print(current_date)
print(current_time)
print(current_datetime)
format_datetime=datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S-%f")
print(format_datetime)