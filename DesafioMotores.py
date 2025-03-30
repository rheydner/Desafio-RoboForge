#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

# Configuração correta dos ports
motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)

def mover_frente(velocidade, tempo):
    motor_esquerdo.run(velocidade)
    motor_direito.run(velocidade)
    wait(tempo)

def girar_90_graus():
    motor_esquerdo.run(400)
    motor_direito.run(-400)
    wait(450)  # Tempo calibrado para 90°
    motor_esquerdo.stop()
    motor_direito.stop()

# Loop principal otimizado
while True:
    for _ in range(4):  # 4 lados do quadrado
        mover_frente(200, 2000)  # Move por 2 segundos
        girar_90_graus()         # Gira 90° após cada lado