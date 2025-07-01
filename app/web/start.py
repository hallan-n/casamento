import web.confirm
import web.gifts
import web.home
import web.login
import web.panel
from fastapi import FastAPI
from nicegui import ui


def init(fastapi_app: FastAPI) -> None:
    ui.run_with(
        fastapi_app,
        mount_path="/web",
        title="Casamento",
        favicon="app/web/assets/favicon.svg",
    )
