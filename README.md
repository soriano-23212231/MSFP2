[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=soriano-23212231/MSFP2)
# Práctica 2: Modelado y control del sistema cardiovascular mediante el modelo Windkessel

## Información de la estudiante

Soriano Angeles Judith Valeria [23212231]; l23212231@tectijuana.edu.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Calcular la función de transferencia del modelo Windkessel para las condiciones de hipotensión, normotensión e hipertensión.
2. Determinar el modelo de ecuaciones diferenciales ordinarias que describe la dinámica del sistema cardiovascular.
3. Representar mediante una analogía eléctrica los parámetros de impedancia, inertancia, resistencia y capacitancia del sistema.
4. Simular la respuesta de los individuos hipotenso, normotenso e hipertenso en Simulink/MATLAB.
5. Sintonizar los controladores de las señales hipotensa e hipertensa mediante la herramienta Tune de Simulink para aproximar su respuesta a la del individuo normotenso.
6. Graficar las respuestas del sistema cardiovascular y las señales controladas mediante un cuaderno computacional de MATLAB.
7. Corroborar mediante Python las respuestas obtenidas en las simulaciones de MATLAB/Simulink.

## Descripción detallada del sistema

En esta práctica se presenta el modelo Windkessel del sistema cardiovascular, representado mediante una analogía eléctrica que considera la impedancia Z, la inertancia L, la resistencia R y la capacitancia C para describir la dinámica de la presión arterial. Se simulan tres condiciones fisiológicas: hipotensión, normotensión e hipertensión, modificando la capacitancia del modelo para cada individuo. La respuesta normotensa se utiliza como referencia para sintonizar los controladores de las condiciones hipotensa e hipertensa en Simulink/MATLAB. Las respuestas del sistema y de los controladores se representan gráficamente y se corroboran mediante simulaciones numéricas en Python.

Palabras clave: Modelo Windkessel; Sistema cardiovascular; Controlador PID; Función de transferencia; Modelo matemático; Simulaciones numéricas.

## Lista de archivos incluidos en el repositorio

1. Cuaderno computacional de MATLAB [.mlx y .pdf].
2. Modelo de Simulink [.slx]: Condiciones hipotensa, normotensa e hipertensa, modelo de ecuaciones y controladores sintonizados con Tune.
3. Archivo de Python [.py] para corroborar las respuestas de MATLAB/Simulink.
4. Figuras de las simulaciones en MATLAB (3) [.pdf]: Individuos hipotenso, normotenso e hipertenso; controlador del individuo hipotenso; controlador del individuo hipertenso.
5. Figuras de las simulaciones en Python [.pdf].
6. Análisis matemático realizado a mano: Modelo de ecuaciones y funciones de transferencia para cada condición [.pdf].
7. Ilustración del sistema fisiológico realizada en BioRender.

## Referencias

[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2025. Permalink: https://biomath.xyz/course/

[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 4, Page 93.

[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.
