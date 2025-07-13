from nicegui import ui
from web.components.menu import menu

@ui.page("/prewedding")
async def index():

    menu()

    ui.add_head_html("""
    <style>
        body { overflow: hidden; }
        .img-limit { 
            height: calc(100vh - 64px);
            position: relative;
        }

        .nav-button {
            background: transparent;
            transition: background 0.3s ease;
        }

        .nav-button:hover.left {
            background: linear-gradient(to right, rgba(0,0,0,0.7), transparent);
        }
        .nav-button:hover.right {
            background: linear-gradient(to left, rgba(0,0,0,0.7), transparent);
        }
    </style>
    """)

    images = [f'assets/prewedding/{i}.jpg' for i in range(1, 40)]
    current_index = {'index': 0}
    with ui.element('div').classes(
        'max-w-[1200px] img-limit mx-auto flex flex-col items-center justify-center relative pt-2'
    ):

        image_element = ui.element('img').props(
            f'src="{images[current_index["index"]]}"'
        ).classes('h-full w-full object-contain')

        def show_image():
            image_element.props(f'src="{images[current_index["index"]]}"')

        def next_image():
            current_index['index'] = (current_index['index'] + 1) % len(images)
            show_image()

        def previous_image():
            current_index['index'] = (current_index['index'] - 1) % len(images)
            show_image()

        with ui.element('div').classes(
            'nav-button left absolute left-0 top-0 bottom-0 w-24 cursor-pointer flex items-center justify-center pt-2'
        ).on('click', previous_image):
            ui.icon('arrow_back_ios').classes('text-white text-3xl')

        with ui.element('div').classes(
            'nav-button right absolute right-0 top-0 bottom-0 w-24 cursor-pointer flex items-center justify-center pt-2'
        ).on('click', next_image):
            ui.icon('arrow_forward_ios').classes('text-white text-3xl')
