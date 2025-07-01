from nicegui import ui
from web.utils import is_login
from web.components.menu import menu


@ui.page("/panel")
async def index():
    is_login()
    menu()

    ui.label("Painel de Administração").classes("text-2xl font-bold mb-4")