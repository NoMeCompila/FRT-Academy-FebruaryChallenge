
<h1>
<p align="center">
  Free Range Testers Academy February Challenge
</p>
</h1>
<p align="center">
  <img src="https://img-c.udemycdn.com/user/200_H/69063786_13e8_4.jpg" alt="FRT-img">
</p>
<div align="center">
      <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/267_Python_logo-512.png" style="width: 40px;">
      <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Selenium_Logo.png" style="width: 40px;">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/2048px-Pytest_logo.svg.png" style="width: 50px;">
</div>
<p align="center">
  En este proyecto se pone en práctica selenium webdriver junto con la libreria pytest para realizar la automatización de pruebas de búsquedas en freerangetesters.com
  y como principal objetivo es manejar listas de web locators.
</p>

## Descripción del proyecto

Este proyecto es parte del 2do desafío de la academia free range testers y última vez en un buen tiempo que usaré selenium con python ya que ingresé aca para poder aprender otras
tecnologías fuera de selenium como son serenity, cypress, etc

## Lenguajes y librerías utilizadas
- python 3.10
- selenium
- pytest
- webdriver-manager
- pytest-html

## Requisitos

- Python 3.x o superior
- Conexión a internet

### comandos para instalar las librerias necesarias

- entorno virtual de python
```
pip install pipenv
```
- selenium
```
pipenv install selenium
```
- pytest
```
pipenv install pytest
```
- reportes html
```
pipenv install pytest-html
```

## Conceptos Utilizados
- POM
- POO
- asserts con pytest
- Data Provider
- Creación de reportes
- Múltiple Browsers

## Funcionamiento

1) navega a freerangetesters.com y verifica el título correcto
2) Se situa en la barra de busqueda y escribe el tema a buscar (Selenium)
3) Da enter en la barra de búsqueda 
4) Verifica que el título sea el correspondiente al tema buscado
5) Verifica que la palabra buscada se enceuntre dentro de cada entrada del blog

## Instrucciones de uso

Una vez que tenemos todo instalado y configurado podemos setear las opciones de busqueda (archivo data/search_data.json) y también el navegador (archivo Browsers/config.json) 
simplemente cambiamos el valor de la propiedad browser que por defecto viene con Chrome por las demas que acepta ("Edge", "Headless Chrome", "Firefox").
para ejecutar la búsqueda en paralelo de las 3 opciones y generar un reporte html ejecutamos el siguiente script en el entorno virtual de la terminal de python:

```
py.test -m free --html=reporte.html
```

## Contribuciones

Me pueden contactar por el discord de freerangetesters aparezco como Fer Caballero y la foto de nirvana o por linkedin que esta en mi inicio de perfil de github  de perfil, soy Jr TAE y recién estoy aprendiendo, 
acepto cualquier sugerencia o crítica constructiva que crean necesario hacerme saber, así como también si quieren preguntarme algo que no sepan de python o selenium 
me pueden contactar  

## Autor

Fernando Caballero 2023 Corrientes Argentina


