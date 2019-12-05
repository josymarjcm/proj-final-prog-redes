# -*- coding: utf-8 -*-
import threading
import datetime
import json
import serial
import time
import sys
import requests

ser = serial.Serial("/dev/ttyACM0")
ser.flushInput()
ip_servidor = "http://10.25.3.133:5000/"

try:
    r = requests.get(ip_servidor)
except:
    print("Servidor offline!")
    sys.exit(0)

def envia_gas(valor):
    time.sleep(15)
    print("Enviando valor do gás...")
    r = requests.post("{}api/inserir_gas/{}".format(ip_servidor, valor))

def envia_humidade(valor):
    time.sleep(20)
    print("Enviando valor da humidade...")
    r = requests.post("{}api/inserir_humidade/{}".format(ip_servidor, valor))

def envia_temperatura(valor):
    time.sleep(25)
    print("Enviando valor da temperatura...")
    r = requests.post("{}api/inserir_temperatura/{}".format(ip_servidor, valor))

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
            t1 = threading.Thread(target = envia_gas, args = (data[2], )).start()
            t2 = threading.Thread(target = envia_humidade, args = (data[0], )).start()
            t3 = threading.Thread(target = envia_temperatura, args = (data[1], )).start()
            data = ""
    except Exception as ex:
        pass

    time.sleep(0.1)

ser.close()
