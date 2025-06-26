import asyncio

import httpx
from nicegui import ui
from web.components.menu import menu
from web.utils import is_login


@ui.page("/panel")
async def index():
    is_login(ui)

    menu()
    with ui.element("div").classes("flex w-full justify-center mt-40 h-screen"):
        ui.label("Painel")
