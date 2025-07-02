from functools import partial

import httpx
from nicegui import ui
from web.components.menu import menu
from web.utils import is_login


@ui.page("/panel")
async def index():
    token = await ui.run_javascript('localStorage.getItem("access_token");', timeout=30)

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
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def put_guest(
        id: str, name: str, phone: str, description: str, is_confirmed: bool
    ):
        async with httpx.AsyncClient() as client:
            response = await client.put(
                "http://localhost:8000/guest/",
                json={
                    "id": id,
                    "name": name,
                    "phone": phone,
                    "description": description,
                    "is_confirmed": is_confirmed,
                },
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Convidado atualizado com sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def delete_guest(id: str):
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"http://localhost:8000/guest/?id={id}",
                headers={"token": token},
            )
            if response.status_code == 200:
                ui.notify("Convidado excluido com sucesso!", color="green")
                await ui.run_javascript("window.location.reload();")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    menu()

    with ui.element("div").classes("w-full mt-10"):
        with ui.element("div").classes(
            "flex flex-row max-w-[1200px] mx-auto w-full h-screen gap-6 justify-center"
        ):
            with ui.element("div").classes("flex flex-col gap-4 w-full max-w-[400px]"):
                ui.label("Adicionar convidado").classes("text-bold text-lg")
                add_name = ui.input(label="Nome")
                add_phone = ui.input(label="Telefone")
                add_description = ui.input(label="Descrição")
                add_is_confirmed = ui.checkbox("Confirmado", value=False)
                ui.button(
                    text="Adicionar",
                    icon="add",
                    on_click=lambda: post_guest(
                        add_name.value,
                        add_phone.value,
                        add_description.value,
                        add_is_confirmed.value,
                    ),
                    color=None,
                ).classes("bg-[#6b6d4a] text-white w-full")

            guests = await get_guest()

            with ui.element("div").classes("w-full h-full max-h-[500px] max-w-[720px]"):
                ui.label("Lista de convidados").classes("text-bold text-lg")
                with ui.column().classes("overflow-y-scroll h-full"):
                    for item in guests:
                        with ui.row().classes(
                            "items-center justify-between w-full border p-4 sm:min-w-[680px] min-h-32 flex-nowrap"
                        ):
                            with ui.label().classes("flex flex-nowrap gap-1"):
                                ui.input("ID").props("readonly").classes(
                                    "w-24"
                                ).value = item["id"]
                                name = ui.input("Nome", value=item["name"]).classes(
                                    "w-24"
                                )
                                phone = ui.input(
                                    "Telefone", value=item["phone"]
                                ).classes("w-24")
                                description = ui.input(
                                    "Descrição", value=item["description"]
                                ).classes("w-24")
                                is_confirmed = ui.checkbox(
                                    "Confirmado", value=item["is_confirmed"]
                                )

                            with ui.row().classes("flex flex-row flex-nowrap gap-2"):
                                ui.button(icon="check", color=None).classes(
                                    "bg-[#6b6d4a] text-white"
                                ).on_click(
                                    partial(
                                        lambda _=None, i=None, n=None, p=None, d=None, c=None: put_guest(
                                            i, n.value, p.value, d.value, c.value
                                        ),
                                        i=item["id"],
                                        n=name,
                                        p=phone,
                                        d=description,
                                        c=is_confirmed,
                                    )
                                )

                                ui.button(icon="delete", color=None).classes(
                                    "bg-[#6b6d4a] text-white"
                                ).on_click(
                                    partial(
                                        lambda _=None, i=None: delete_guest(i),
                                        i=item["id"],
                                    )
                                )
