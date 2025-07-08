import asyncio
import json

import httpx
from consts import API_URL
from nicegui import ui
from web.components.menu import menu


@ui.page("/confirm/{user}")
async def confirm(user: str):
    async def get_guest():
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/guest/?id={user}")
            if response.status_code == 200:
                if response.json()["is_confirmed"]:
                    await ui.run_javascript(
                        f"""
                        localStorage.setItem("current_user", '{json.dumps(response.json())}');
                        window.location.href = '/web/gifts';                    
                        """,
                        timeout=30,
                    )
                return response.json()
            elif response.status_code == 422:
                ui.notify("Erro: Convidado não encontrado", color="red")
            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    async def update_guest(name: str, phone: str, description: str, companion_1,companion_2, companion_3, companion_4,companion_5):
        data = {
            "id": user,
            "name": name,
            "phone": phone,
            "is_confirmed": True,
            "description": description,
            "max_companion": current_user["max_companion"],
            "companion_1": companion_1.value,
            "companion_2": companion_2.value,
            "companion_3": companion_3.value,
            "companion_4": companion_4.value,
            "companion_5": companion_5.value
        }

        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{API_URL}/guest/",
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
        "flex items-center gap-6 w-full justify-center h-screen"
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
                description = ui.input(label="Descrição").value = current_user.get("description", "")

                companion_1,companion_2, companion_3, companion_4,companion_5 = None, None, None, None, None

                if current_user.get("max_companion") >= 1:
                    ui.label(f'Você pode levar até {current_user.get("max_companion")} acompanhantes').classes('mt-2 text-bold')
                    companion_1 = ui.input(label="Acompanhante 1", value=current_user.get("companion_1"))\
                        .classes(f'{'' if current_user.get("max_companion") >= 1 else 'hidden'}')
                    companion_2 = ui.input(label="Acompanhante 2", value=current_user.get("companion_2"))\
                        .classes(f'{'' if current_user.get("max_companion") >= 2 else 'hidden'}')
                    companion_3 = ui.input(label="Acompanhante 3", value=current_user.get("companion_3"))\
                        .classes(f'{'' if current_user.get("max_companion") >= 3 else 'hidden'}')
                    companion_4 = ui.input(label="Acompanhante 4", value=current_user.get("companion_4"))\
                        .classes(f'{'' if current_user.get("max_companion") >= 4 else 'hidden'}')
                    companion_5 = ui.input(label="Acompanhante 5", value=current_user.get("companion_5"))\
                        .classes(f'{'' if current_user.get("max_companion") > 5 else 'hidden'}')
                ui.button(
                    text="Confirmar",
                    icon="check",
                    on_click=lambda: update_guest(name,phone,description,companion_1,companion_2, companion_3, companion_4,companion_5),
                    color=None,
                ).classes("bg-[#6b6d4a] text-white w-full")
