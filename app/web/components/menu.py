from nicegui import ui
from web.utils import reset_css


def menu(current_user=None):
    reset_css()

    with ui.header().classes("bg-olive-1 p-4 shadow"):
        with ui.row().classes(
            "flex items-center justify-center sm:justify-between w-full mx-auto max-w-[1200px]"
        ):
            ui.image("app/web/assets/logo.svg").classes("w-12")
            with ui.element("div").classes(
                "flex gap-3 justify-between sm:w-auto w-full items-center"
            ):
                ui.link("Início", "/").classes("cursor-pointer text-white no-underline")
                ui.link("Administração", "/login").classes(
                    "cursor-pointer text-white no-underline"
                )
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
