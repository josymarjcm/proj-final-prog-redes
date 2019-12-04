# -*- coding: utf-8 -*-
import datetime
import json
import serial
import time
import requests

ser = serial.Serial("")
ser.flushInput()
ip_servidor = "http://10.24.13.102:5000/"

"""
Lê os dados que o Arduino envia para a porta serial.
"""
while True:
    try:
        ser_bytes = ser.readline()          # Leitura e decodificação dos bytes da porta serial
        data = ser_bytes.decode("UTF-8")

        data = data.split(" ")              # Facilita a extração do conteúdo

        if len(data) == 3:
            # Manda para o servidor no tempo estipulado
            time.sleep(15)
            r = requests.post("{}inserir_gas/{}".format(ip_servidor, data[2]))
            time.sleep(5)
            r = requests.post("{}inserir_humidade/{}".format(ip_servidor, data[0]))
            time.sleep(5)
            r = requests.post("{}inserir_temperatura/{}".format(ip_servidor, data[1]))
    except:
        pass

    time.sleep(0.1)

ser.close()
