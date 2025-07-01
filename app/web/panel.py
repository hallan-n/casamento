import httpx
from nicegui import ui
from web.components.menu import menu
from web.utils import is_login


@ui.page("/panel")
async def index():

    token = await ui.run_javascript(
        'localStorage.getItem("access_token");', timeout=30
    )


    is_login()


    async def get_guest():
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "http://localhost:8000/guest/",
                headers={"token": token},
            )
            if response.status_code == 200:
                return response.json()
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

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
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Sucesso!", color="green")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    menu()

    with ui.tabs().classes('w-full') as tabs:
        tab1 = ui.tab('Gerenciar convidados')
        tab2 = ui.tab('Gerenciar presentes')

    with ui.tab_panels(tabs, value=tab1).classes('w-full'):
        with ui.tab_panel(tab1).classes('flex flex-row max-w-[1200px] mx-auto w-full h-screen gap-4 justify-center'):
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

            with ui.element("div").classes("flex flex-col gap-4 w-full max-w-[600px]"):
                guests = await get_guest()


                with ui.column():
                    ui.label('Lista de pessoas')
                    for item in guests:
                        with ui.row().classes('items-center justify-between w-full border p-2'):
                            with ui.label().classes("flex gap-1"):
                                name = ui.input('Nome').classes('w-24')
                                phone = ui.input('Telefone').classes('w-24')
                                description = ui.input('Descrição').classes('w-24')
                                is_confirmed = ui.checkbox("Confirmado", value=False)
                                
                            with ui.row():
                                ui.button(icon='edit')
                                ui.button(icon='add')
                                








        with ui.tab_panel(tab2).classes('flex max-w-[1200px] mx-auto w-full h-screen gap-4 justify-center'):
            ui.label('Conteúdo da Aba 2')
    # with ui.element("div").classes('flex max-w-[1200px] mx-auto w-full h-screen gap-4 justify-center mt-40'):
    #     with ui.element("div").classes("flex justify-center"):
    #         



    #     with ui.element("div").classes("flex justify-center"):
    #         with ui.element("div").classes("flex flex-col gap-4 w-full max-w-[400px]"):
    #             ui.label("Adicionar presente").classes("text-bold text-lg")
    #             name = ui.input(label="Nome")
    #             thumb = ui.input(label="Image URL")
    #             url = ui.input(label="Link do presente")
    #             price = ui.input(label="Preço")
    #             ui.button(
    #                 text="Adicionar",
    #                 icon="add",
    #                 on_click=lambda: post_guest(
    #                     name.value, phone.value, description.value, is_confirmed.value
    #                 ),
    #                 color=None,
    #             ).classes("bg-[#6b6d4a] text-white w-full")
