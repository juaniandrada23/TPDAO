import datetime
from datetime import timedelta

fecha1 = datetime.datetime.now()
fecha2 = datetime.datetime(2023,11,10)
nueva_fecha = fecha2 + timedelta(days=5)

#print(type(conv))
print(nueva_fecha.strftime('%Y-%m-%d'))
