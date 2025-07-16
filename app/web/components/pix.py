from nicegui import ui
from web.utils import reset_css
    
def pix_code():
    async def copy_code():
        await ui.run_javascript("navigator.clipboard.writeText('00020126580014BR.GOV.BCB.PIX013603925632-85ab-4f9b-a880-958c96299e495204000053039865802BR5925Hallan Guilherme Santos d6009SAO PAULO62140510NfTF2VbpxO6304F289')", timeout=30)
        ui.notify('Código PIX copiado!')

    with ui.dialog() as modal, ui.card().classes('p-8 w-full max-w-[400px]'):
        with ui.element('div').classes('flex justify-end w-full'):
            ui.icon('close', size='md').on('click', modal.close).classes('cursor-pointer hover:text-zinc-400')
        ui.label('Código PIX').classes('text-bold text-2xl')
        ui.label('Escaneie o código e nos presenteie ❤️')
        ui.element('img').props('src="https://raw.githubusercontent.com/hallan-n/cdn-free/main/prewedding/qrcode.png"')
        ui.label('Ou copie a chave PIX!') 
        with ui.element('div').classes('flex flex-row flex-nowrap justify-between bg-zinc-200 rounded-lg w-full'):
            ui.input(value='00020126580014BR.GOV.BCB.PIX013603925632-85ab-4f9b-a880-958c96299e495204000053039865802BR5925Hallan Guilherme Santos d6009SAO PAULO62140510NfTF2VbpxO6304F289').props('readonly').classes('px-4')
            ui.button('Copiar', color=None).on(
                'click', copy_code
            ).classes('bg-olive-1 text-white')
        return modal
