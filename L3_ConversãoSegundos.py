segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
totalSegs = int(segundos)

dias = totalSegs // 86400
restododias = totalSegs % 86400
horas = restododias // 3600
restodohoras = restododias % 3600
minutos = restodohoras // 60
segundosfinais = restodohoras % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundosfinais, "segundos.")

                     
