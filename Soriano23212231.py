"""
Práctica 2: Modelado y control del sistema cardiovascular mediante
el modelo Windkessel

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Judith Valeria Soriano Angeles
Número de control: 23212231
Correo institucional: l23212231@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""


# Librerías para cálculo numérico y generación de gráficas
import sys

import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy import signal
import control as ctrl
import pandas as pd

# Datos de la simulación
u = np.array(pd.read_excel('signal.xlsx',header=None))
u = np.reshape(u,-1)
x0,t0,tend,dt,w,h = 0,0,15,1E-3,10,5
N = round((tend-t0)/dt)+1 # Número de muestras
t = np.linspace(t0,tend,N) # Vector de tiempo


# Componentes del circuito RLC
def cardio (Z,R,L,C):
    num=[L*R, R*Z]
    den=[C*L*R*Z, L*(Z+R), R*Z]
    sys=ctrl.tf(num,den)
    L=np.roots(den)
    return sys,L

#Funcion de transferencia HIPOTENSO
Z,R,L,C= 0.010, 1.000, 0.001, 3.500
syshipo,L=cardio(Z,R,L,C)
print(f"Función de transferencia para sistema hipotenso: {syshipo}")
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2 = {L[1]:.3e}\n")

#Funcion de transferencia NORMOTENSO
Z,R,L,C= 0.010, 1.000, 0.001, 1.500
sysnormo,L=cardio(Z,R,L,C)
print(f"Función de transferencia para sistema normotenso (control): {sysnormo}")
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2 = {L[1]:.3e}\n")

#Funcion de transferencia HIPERTENSO
Z,R,L,C= 0.010, 1.000, 0.001, 1
syshiper,L=cardio(Z,R,L,C)
print(f"Función de transferencia para sistema hipertenso (control): {syshiper}")
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2 = {L[1]:.3e}\n")

#Respuesta del sistema en lazo abierto
_,PpN = ctrl.forced_response(sysnormo,t,u,x0)
_,PpL = ctrl.forced_response(syshipo,t,PpN,x0)
_,PpH = ctrl.forced_response(syshiper,t,PpN,x0)

#Colores
clr1 = np.array([246, 36, 119])/255;
clr2 = np.array([255, 173, 238])/255;
clr3 = np.array([146, 0, 58])/255;


#Componentes del Controlador 
def controlador(kI,kP,kD,sys):
    Cr=1E-6
    Re=1/(Cr*kI)
    Rr=kP*Re
    Ce=kD/Rr
    numPID=[Re*Rr*Ce*Cr, (Re*Ce + Rr*Cr),1]
    denPID=[Re*Cr,0]
    PID=ctrl.tf(numPID,denPID)
    sysPID=ctrl.feedback(ctrl.series(PID,sys),1,sign =-1)
    return sysPID

hipoPID=controlador(143640.987936279, 62.298991995503, 0.000828720466709219, syshipo)
print(f"Función de transferencia del sistema hipotenso en lazo cerrado: {hipoPID}") 

hiperPID=controlador(3845842.36679008, 1611.19356315767, 0.0226422629299059, syshiper)
print(f"Función de transferencia del sistema hipertenso en lazo cerrado: {hiperPID}")

#Respuestas del sistema de control en lazo cerrado
_,PID1 = ctrl.forced_response(hipoPID,t,PpN,x0)
_,PID2 = ctrl.forced_response(hiperPID,t,PpN,x0)

#Respuestas: Simulaciones numericas
fg=plt.figure(1)
fg.set_size_inches(w,h)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.plot(t,PpN,'-',color=clr1,label='Normotenso')
plt.plot(t,PpL,'--',color=clr2,label='Hipotenso')
plt.plot(t,PpH,':',linewidth=2.5,color=clr3,label='Hipertenso')
plt.xlim(0,15); plt.xticks(np.arange(0,16,1))
plt.ylim(-0.4,1.2); plt.yticks(np.arange(-0.6,1.6,0.2))
plt.xlabel('t[s]')
plt.ylabel ('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5,-0.25), loc='center', ncol=3,frameon=False)
fg.savefig('individuos_python.pdf',bbox_inches='tight')
plt.show()

fg=plt.figure(2)
fg.set_size_inches(w,h)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.plot(t,PpL,'-',color=clr1,label='Hipotenso')
plt.plot(t,PpN,'--',color=clr2,label='Normotenso')
plt.plot(t,PID1,':',linewidth=2.5,color=clr3,label='Controlador')
plt.xlim(0,15); plt.xticks(np.arange(0,16,1))
plt.ylim(-0.4,1.2); plt.yticks(np.arange(-0.6,1.6,0.2))
plt.xlabel('t[s]')
plt.ylabel ('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5,-0.25), loc='center', ncol=3,frameon=False)
fg.savefig('Hipotenso_python.pdf',bbox_inches='tight')
plt.show()

fg=plt.figure(3)
fg.set_size_inches(w,h)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Times New Roman'
plt.plot(t,PpN,'-',color=clr1,label='Normotenso')
plt.plot(t,PpH,'--',color=clr2,label='Hipertenso')
plt.plot(t,PID2,':',linewidth=2.5,color=clr3,label='Controlador')
plt.xlim(0,15); plt.xticks(np.arange(0,16,1))
plt.ylim(-0.4,1.2); plt.yticks(np.arange(-0.6,1.6,0.2))
plt.xlabel('t[s]')
plt.ylabel ('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5,-0.25), loc='center', ncol=3,frameon=False)
fg.savefig('Hipertenso_python.pdf',bbox_inches='tight')
plt.show()