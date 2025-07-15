from nicegui import ui
from web.utils import reset_css


def menu(current_user=None):
    reset_css()
    async def copy_code():
        await ui.run_javascript("navigator.clipboard.writeText('00020126580014BR.GOV.BCB.PIX013603925632-85ab-4f9b-a880-958c96299e495204000053039865802BR5925Hallan Guilherme Santos d6009SAO PAULO62140510NfTF2VbpxO6304F289')", timeout=30)
        ui.notify('Código PIX copiado!')

    with ui.dialog() as modal, ui.card().classes('p-8 w-full max-w-[400px]'):
        with ui.element('div').classes('flex justify-end w-full'):
            ui.icon('close', size='md').on('click', modal.close).classes('cursor-pointer hover:text-zinc-400')
        ui.label('Código PIX').classes('text-bold text-2xl')
        ui.label('Escaneie o código!')
        ui.image('https://raw.githubusercontent.com/hallan-n/cdn-free/main/prewedding/qrcode.png')
        ui.label('Ou copie a chave PIX!') 
        with ui.element('div').classes('flex flex-row flex-nowrap justify-between bg-zinc-200 rounded-lg w-full'):
            ui.input(value='00020126580014BR.GOV.BCB.PIX013603925632-85ab-4f9b-a880-958c96299e495204000053039865802BR5925Hallan Guilherme Santos d6009SAO PAULO62140510NfTF2VbpxO6304F289').props('readonly').classes('px-4')
            ui.button('Copiar', color=None).on(
                'click', copy_code
            ).classes('bg-olive-1 text-white')


    with ui.header().classes("bg-olive-1 p-4 shadow"):
        with ui.row().classes(
            "flex items-center justify-center sm:justify-between w-full mx-auto max-w-[1200px]"
        ):
            ui.image("app/web/assets/logo.svg").classes("w-12")
            with ui.element("div").classes(
                "flex gap-3 justify-between sm:w-auto w-full items-center"
            ):
                ui.link("Início", "/").classes("cursor-pointer text-white no-underline")
                ui.label('PIX').classes('cursor-pointer hover:text-zinc-200').on('click', modal.open)
                ui.link("Pre Wedding", "/prewedding").classes("cursor-pointer text-white no-underline")
                ui.link("Lista de presentes", "/gifts").classes(
                    "cursor-pointer text-white no-underline"
                )
                if current_user:
                    with ui.dropdown_button(
                        text=current_user.get("name"),
                        icon="account_circle",
                        color=None,
                        auto_close=True,
                    ):
                        ui.item(f'ID: {current_user.get("id")}')
                        ui.item(f'Telefone: {current_user.get("phone")}')
                        ui.item(
                            f'Cofirmou: {'Sim' if current_user.get("is_confirmed") else 'Não'}'
                        )
                        ui.button(
                            text="Sair",
                            icon="logout",
                            color='red'
                        ).classes("text-white w-full").on_click(
                            lambda: ui.run_javascript(
                                """
                                localStorage.removeItem('current_user');
                                window.location.href = '/web/gifts';
                                """
                            )
                        )
