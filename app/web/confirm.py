import asyncio
import json

import httpx
from nicegui import ui
from web.components.menu import menu


@ui.page("/confirm/{user}")
async def confirm(user: str):
    async def get_guest():
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://localhost:8000/guest/?id={user}")
            if response.status_code == 200:
                if response.json()["is_confirmed"]:
                    ui.navigate.to("/gifts")
                return response.json()
            elif response.status_code == 422:
                ui.notify("Erro: Convidado não encontrado", color="red")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def update_guest(name: str, phone: str, description: str):
        data = {
            "id": user,
            "name": name,
            "phone": phone,
            "is_confirmed": True,
            "description": description,
        }
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"http://localhost:8000/guest/",
                json=data,
            )

            if response.status_code == 200:
                ui.notify("Presença confirmada com sucesso!", color="green")
                await asyncio.sleep(2)

                await ui.run_javascript(
                    f"""
                    localStorage.setItem("current_user", '{json.dumps(data)}');
                    window.location.href = '/web/gifts';                    
                    """
                )
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    current_user = await get_guest()
    menu()
    with ui.element("div").classes(
        "flex items-center gap-6 w-full justify-center mt-40 h-screen p-4"
    ):

        with ui.element("div").classes(
            "w-96 h-96 overflow-hidden rounded-lg shadow-lg relative"
        ):
            ui.image("app/web/assets/casal.jpeg").classes(
                "absolute top-0 left-0 w-full h-auto"
            )

        with ui.element("div").classes("flex"):
            with ui.element("div").classes("flex flex-col gap-4 w-full max-w-[400px]"):
                ui.label("Confirmar presença").classes("text-bold text-lg")
                ui.label(
                    "Verifique se seus dados estão correto. Se não, preencha-o corretamente."
                )
                name = ui.input(label="Nome").value = current_user.get("name", "")
                phone = ui.input(label="Telefone").value = current_user.get("phone", "")
                description = ui.input(label="Descrição").value = current_user.get(
                    "description", ""
                )

                ui.button(
                    text="Confirmar",
                    icon="check",
                    on_click=lambda: update_guest(name, phone, description),
                    color=None,
                ).classes("bg-[#6b6d4a] text-white w-full")
