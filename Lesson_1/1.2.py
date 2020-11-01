n = int(input("Введите время в секундах "))

mins = 60
hours = 60 * 60

hour = n // hours
minute = (n - (hour * hours)) // mins
secs = n - ((hour * hours) + (minute * mins))

print('{0}:{1}:{2}'.format((str(hour).zfill(2)),
                            str(minute).zfill(2),
                            str(secs).zfill(2)))

# Ниже код без использования .zfill, но мне он показался слишком "кривым"
# print('{0}:{1}:{2}'.format(("0" + str(hour) if hour < 10 else hour),
#                            "0" + str(minute) if minute < 10 else minute,
#                            "0" + str(secs) if secs < 10 else secs))