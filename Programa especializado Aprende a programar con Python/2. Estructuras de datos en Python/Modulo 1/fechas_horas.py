import datetime

#objecto de date
date = datetime.date(2019, 4, 30)

#atributo año del objeto fecha
date.year

#atributo mes del objeto fecha
date.month

#atributo dia del objeto fecha
date.day

#
#devuelve el dia de la semana. el lunes es el cero y el domingo es el 6
date.weekday()

#devuelve el dia de la semana. el lunes es el uno y el domingo es el 7
date.isoformat()

#devuelve una tupla con tres elementos : año, numero de semana, dia de la semana
date.isocalendar()

#devuelve la fecha como un string con el formato "YYY-MM-DD"
date.isoformat()

#fecha minima
date_min = datetime.date.min

#fecha maxima
date_max = datetime.date.max

#el dia de hoy
today = datetime.date.today()

#el dia de ayer
yesterday = today - datetime.timedelta(days=1)

#resta de dos fechas
delta = today - yesterday

#
#datetime objecto
date_and_time = datetime.datetime(2019, 10, 10, 9, 15, 30)

#atributo año de la fecha y hora
date_and_time.year

#atributo mes de la fecha u hora
date_and_time.month

#atributo dia de la fecha y hora
date_and_time.day

#atributo hora de la fecha y hora
date_and_time.hour

#atributo minuto de la fecha y hora
date_and_time.minute

#atributo segundo de la fecha y hora
date_and_time.second

#atributo microsegundos de la fecha y hora
date_and_time.microsecond

#obtengo un objeto date a partir del objeto datetime
date_and_time.date()

#la fecha y hora actual (local)
now= datetime.datetime.now()

#la fecha u hjora actual en utc
now = datetime.datetime.utcnow()

#
#Objeto tipo hora
time = datetime.time(10, 20, 35)

#atributo hora de la hora
time.hour

#atributo minuto de la hora
time.minute

#atributo segundo de la hora
time.second

#atributo microsegundo de la hora
time.microsecond

#hora minima
time_min = datetime.time.min

#hora maxima
time_max = datetime.time.max

