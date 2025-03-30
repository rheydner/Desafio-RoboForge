#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait

ev3 = EV3Brick()

# Configuração dos motores e sensores
motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)
sensor_ultrassonico = UltrasonicSensor(Port.S1)
sensor_cor = ColorSensor(Port.S2)

# Constantes
DISTANCIA_ALVO = 200  # Distância desejada da parede (mm)
VELOCIDADE_BASE = 200  # Velocidade base dos motores
KP = 1.5  # Ganho proporcional para controle PID

def seguir_parede():
    while True:
        distancia = sensor_ultrassonico.distance()
        erro = DISTANCIA_ALVO - distancia
        ajuste = erro * KP
        
        motor_esquerdo.run(VELOCIDADE_BASE + ajuste)
        motor_direito.run(VELOCIDADE_BASE - ajuste)
        
        # Verificar cor no chão
        cor = sensor_cor.color()
        if cor == Color.RED:
            # Curva de 90° (gira no próprio eixo)
            motor_esquerdo.run(300)
            motor_direito.run(-300)
            wait(800)  # Ajuste conforme necessário para 90°
            break
        elif cor == Color.YELLOW:
            ev3.screen.print("Aguardando comando...")
            while not any(ev3.buttons.pressed()):
                wait(10)
            wait(1000)
            ev3.screen.clear()
        elif cor == Color.GREEN:
            motor_esquerdo.stop()
            motor_direito.stop()
            ev3.screen.print("Parado!")
            return  # Encerra o programa

# Loop principal
while True:
    seguir_parede()
    wait(10)