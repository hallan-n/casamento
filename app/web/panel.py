import httpx
from nicegui import ui
from web.components.menu import menu
from web.utils import is_login


@ui.page("/panel")
async def index():
    is_login()

    async def post_guest(name: str, phone: str, description: str, is_confirmed: bool):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:8000/guest/",
                json={
                    "name": name,
                    "phone": phone,
                    "description": description,
                    "is_confirmed": is_confirmed,
                },
                headers={"token": "token"},
            )
            if response.status_code == 200:
                ui.notify("Sucesso!", color="green")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    menu()

    with ui.element("div").classes("flex w-full justify-center mt-40 h-screen"):
        with ui.element("div").classes("flex flex-col gap-4 w-full max-w-[400px]"):
            ui.label("Adicionar convidado").classes("text-bold text-lg")
            name = ui.input(label="Nome")
            phone = ui.input(label="Telefone")
            description = ui.input(label="Descrição")
            is_confirmed = ui.checkbox("Confirmado", value=False)
            ui.button(
                text="Adicionar",
                icon="add",
                on_click=lambda: post_guest(
                    name.value, phone.value, description.value, is_confirmed.value
                ),
                color=None,
            ).classes("bg-[#6b6d4a] text-white w-full")
