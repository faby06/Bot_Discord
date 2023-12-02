import discord  #Se importa la libreria de discord 
import asyncio  #Se importa la libreria para  la espera de mensajes del usuario que permite que el bot realice otras tareas mientras espera la interacción del usuario
from sympy import symbols, integrate, simplify, diff #Importa funciones para realizar los calculos de la calculadota como son las derivadas interegrales etc.

# Token del bot para poder conectarlo 
TOKEN = 'MTE4MDM0NzI2NzA2OTI2MzkwMw.G4ciTp.aEwFpadl1YsTt6cZsQu6ZvX97duYfRhjOiyYeY'  
# Crear una instancia del cliente de Discord
client = discord.Client(intents=discord.Intents.default())

# Evento que se ejecuta cuando el bot se conecta
@client.event
async def on_ready():
    print(f'Bot conectado como {client.user.name}')

# Evento que se ejecuta cuando se recibe un mensaje
@client.event
async def on_message(message):
    # Evitar que el bot responda a sus propios mensajes
    if message.author == client.user:
        return

    # Comando de saludo y opciones
    if message.content.lower() == 'hola':
        await message.channel.send('¡Hola! Soy un bot calculadora.\nElige una opción:')
        await message.channel.send('1. Sumar\n'
                                   '2. Derivar\n'
                                   '3. Integrar\n'
                                   '4. Tutorial de derivadas e integrales\n'
                                   '5. Formulario de derivadas e integrales\n')

    # Comandos para opciones numéricas 1, 2, 3, 4, 5
    elif message.content.lower() in ['1', '2', '3', '4', '5']:
        opcion_elegida = message.content.lower()

        # Opción 1: Sumar
        if opcion_elegida == '1':
            await message.channel.send('Has elegido la opción Sumar. Ingresa dos números separados por espacio para sumar.')
            await message.channel.send('Ejemplo: `3 5`')
            
              # Espera a que el usuario proporcione dos números para sumar
            def check(m):
                return m.author == message.author and len(m.content.split()) == 2 and all(part.isdigit() for part in m.content.split())

            try:
                respuesta_usuario = await client.wait_for('message', check=check, timeout=30)
                numeros = [int(part) for part in respuesta_usuario.content.split()]
                resultado = sum(numeros)  # Calcula la suma de los dos números con la función sum
                await message.channel.send(f'La suma de {numeros[0]} + {numeros[1]} es: {resultado}\n')
                await message.channel.send('¡ADIOS! Espero que vuelvas pronto')

            except asyncio.TimeoutError:
                await message.channel.send('Tiempo de espera agotado. La operación ha sido cancelada.')

        # Opción 2: Derivar
        elif opcion_elegida == '2':
            await message.channel.send('Has elegido la opción Derivar. Ingresa una expresión matemática para derivar.')
            await message.channel.send('Ejemplo: `2*x` o `5*x**2 + 6` o x**2 o 5*x**2 + 6*x**3')
            # Resto del código para la derivada...
            def check(m):
                return m.author == message.author

            try:
                respuesta_usuario = await client.wait_for('message', check=check, timeout=30)
                expresion = respuesta_usuario.content

                # Parsear la expresión y calcular la derivada
                x = symbols('x')
                derivada = diff(expresion, x)
                derivada_simplificada = simplify(derivada)

                await message.channel.send(f'La derivada de {expresion} con respecto a x es: {derivada_simplificada}')

            except asyncio.TimeoutError:
                await message.channel.send('Tiempo de espera agotado. La operación ha sido cancelada.')
            

        # Opción 3: Integrar
        elif opcion_elegida == '3':
            await message.channel.send('Has elegido la opción Integrar. Ingresa una expresión matemática para integrar.')
            await message.channel.send('Ejemplo: `2*x` o `5*x**2 + 6`')
            # Resto del código para la integral...
            def check(m):
                return m.author == message.author

            try:
                respuesta_usuario = await client.wait_for('message', check=check, timeout=30)
                expresion = respuesta_usuario.content

                # Parsear la expresión y calcular la integral
                x = symbols('x')
                integral = integrate(expresion, x)
                integral_simplificada = simplify(integral)

                await message.channel.send(f'La integral de {expresion} con respecto a x es: {integral_simplificada} + C')

            except asyncio.TimeoutError:
                await message.channel.send('Tiempo de espera agotado. La operación ha sido cancelada.')
        

        # Opción 4: Tutorial
        elif opcion_elegida == '4':
            await message.channel.send('Has elegido la opción de Tutorial.')
            await message.channel.send('Aqui tienes dos canales de youtube')
            await message.channel.send('Derivadas: https://www.youtube.com/watch?v=uK4-s0ojHFg&list=PLeySRPnY35dG2UQ35tPsaVMYkQhc8Vp__')
            await message.channel.send('Integrales: https://www.youtube.com/watch?v=msDiFIjvHks&list=PL9SnRnlzoyX39hvLuyYgFEIdCXFXI3xaU')

        # Opción 5: Formulario
        elif opcion_elegida == '5':
            await message.channel.send('Has elegido la opción de Formulario.')
            # Cargar la imagen desde el archivo local
            formulario_path = 'tabla_derivadas.png' # Cambia esto con el nombre de tu imagen
            with open(formulario_path, 'rb') as f:
                formulario_imagen = discord.File(f)
            # Enviar la imagen al canal
            await message.channel.send(file=formulario_imagen)

# Ejecutar el bot con el token proporcionado
client.run(TOKEN)