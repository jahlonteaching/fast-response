import asyncio

from nicegui import ui
from app.model import ProcesadorCorreo


procesador = ProcesadorCorreo()

# Interfaz gráfica
ui.label('📨 Procesador de Correos').classes('text-3xl font-bold mb-6 text-center')

with ui.card().classes('w-full max-w-2xl mx-auto shadow-2xl p-6 bg-white rounded-2xl'):
    ui.label('✉️ Ingresar contenido del correo').classes('text-xl font-semibold mb-2')

    contenido_input = ui.textarea(label='Contenido', placeholder='Escribe aquí el mensaje recibido...').classes('w-full mb-4 h-40')
    respuesta_output = ui.textarea(label='Respuesta generada').props('readonly').classes('w-full mb-4 h-40')

    def on_generar_click():
        async def generar_respuesta_async():
            respuesta_output.value = await procesador.generar_respuesta(contenido_input.value)

        asyncio.create_task(generar_respuesta_async())

    ui.button('🧠 Generar respuesta', on_click=on_generar_click).classes('mb-6 bg-blue-600 text-white hover:bg-blue-700')

    ui.separator().classes('my-4')

    ui.label('📤 Enviar respuesta').classes('text-xl font-semibold mb-2')
    asunto_input = ui.input(label='Asunto').classes('w-full mb-2')
    destinatario_input = ui.input(label='Destinatario').classes('w-full mb-4')

    def on_enviar_click():
        procesador.enviar_respuesta(asunto_input.value, respuesta_output.value, destinatario_input.value)
        ui.notify(f'Correo enviado a {destinatario_input.value}', type='positive')

    ui.button('🚀 Enviar respuesta', on_click=on_enviar_click).classes('bg-green-600 text-white hover:bg-green-700')

ui.run()
