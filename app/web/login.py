import asyncio

import httpx
from consts import API_URL
from nicegui import ui
from web.components.menu import menu
from web.utils import reset_css


@ui.page("/login")
async def index():
    ui.run_javascript(
        """
    if (localStorage.getItem('access_token')) {
        window.location.href = '/web/panel';
    }
    """
    )
    reset_css()

    async def post_login(user: str, password: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{API_URL}/auth/", json={"user": user, "password": password}
            )
            if response.status_code == 200:
                ui.notify("Sucesso!", color="green")
                await asyncio.sleep(2)

                ui.run_javascript(
                    f"""
                    localStorage.setItem("access_token", "{response.json()['access_token']}");
                    window.location.href = "panel";
                """
                )

            else:
                ui.notify(f"Erro: {response.json()['detail']}", color="red")

    menu()
    with ui.element("div").classes("flex w-full justify-center mt-40 h-screen"):
        with ui.element("div").classes("flex flex-col gap-4 w-full max-w-[400px]"):
            ui.label("Login").classes("text-bold text-lg")
            user = ui.input(label="Usuário")
            pwd = ui.input(label="Senha", password=True)
            ui.button(
                text="Entrar",
                icon="send",
                on_click=lambda: post_login(user.value, pwd.value),
                color=None,
            ).classes("bg-[#6b6d4a] text-white w-full")
