from nicegui import ui
from web.components.menu import menu
from web.utils import reset_css

@ui.page("/")
async def index():
    reset_css()
    menu()
    with ui.element("div"):
        with ui.element("div").classes(
            "relative w-screen h-screen "
            "bg-[url('https://raw.githubusercontent.com/hallan-n/cdn-free/main/prewedding/29.jpg')] "
            "bg-cover bg-no-repeat "
            "bg-[length:160%] bg-[position:20%_40%] "
            "lg:bg-[url('assets/mask2.png')] "
            "lg:bg-contain lg:bg-left lg:bg-[length:auto] lg:bg-[position:left_center]"
        ):
            ui.element("div").classes("absolute inset-0 bg-olive-1 lg:-z-10 lg:opacity-100 opacity-50")
            with ui.element("div").classes(
                'relative z-[999] w-full h-full flex items-center '
                'lg:justify-end justify-center max-w-[1200px] mx-auto'
            ):
                with ui.element("div").classes('w-full max-w-[400px] text-2xl text-white text-center mb-24'):
                    ui.image("app/web/assets/logo_full.svg")
                    ui.image("app/web/assets/divider.svg")
                    ui.label("Save the Date").classes('mt-4 lg:[text-shadow:none] [text-shadow:2px_2px_10px_rgba(0,0,0)]')
                    ui.label("Sábado, 04 de Outubro, às 16h!").classes('text-bold mt-4 lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0)]')
                    ui.label("Gostaríamos de convidá-lo(a)").classes('mt-4').classes('lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0)]')
                    ui.label("para celebrar conosco este").classes('mt-4').classes('lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0)]')
                    ui.label("momento especial de união.").classes('mt-4').classes('lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0)]')
                    with ui.link('', '#info').classes('block mt-4 text-white'):
                        ui.label("Confira as informações do casamento").classes('mt-12').classes('lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0)]')
                        ui.icon('arrow_downward').classes(
                            'text-5xl lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0)]'
                        )
                    

        with ui.element("div").classes("bg-olive-1 w-screen h-screen p-4").props("id=info"):
            with ui.element("div").classes('w-full h-full max-w-[1200px] mx-auto'):
                ui.label("Nosso Grande Dia").classes('text-2xl text-bold text-white py-10')
                with ui.element('div').classes('flex md:flex-row flex-col md:justify-between justify-center items-center md:max-h-[500px]'):
                    ui.html('📅 O nosso casamento começará às 16h, na <b>Paróquia Santo André Apóstolo</b>, onde vamos celebrar esse momento tão especial junto com você! <br><br>📍R. Santo André, 387 - André Carloni, Serra - ES, 29161-851 <br><br>Depois da cerimônia, vamos para um cerimonial chamado <b>Cerimonial Espaço Encantado</b> com piscina, churrasco e muita alegria!<br><br>📍R. Santo André, 387 - André Carloni, Serra - ES, 29161-851 ').classes('w-full md:w-1/2 text-2xl text-white')
                    with ui.element('div').classes('flex justify-center flex-row gap-2'):
                        ui.element('iframe').props('src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3786388.8542359457!2d-52.8339299!3d-21.8717675!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xb8197538b6138d%3A0x5d3f1bfb8067acca!2sPar%C3%B3quia%20e%20Matriz%20Santo%20Andr%C3%A9%20Ap%C3%B3stolo%20-%20Andr%C3%A9%20Carloni!5e0!3m2!1spt-BR!2sbr!4v1716234567890!5m2!1spt-BR!2sbr"').classes('w-full md:h-[248px] h-[150px]')

                        ui.element('iframe').props('src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3745.2415276423044!2d-40.2720102!3d-20.1656667!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xb81f3bdba0168b%3A0xe82de3395125e518!2sCerimonial%20Espa%C3%A7o%20Encantado!5e0!3m2!1spt-BR!2sbr!4v1752612397445!5m2!1spt-BR!2sbr"').classes('w-full md:h-[248px] h-[150px] md:mt-2')

                    

                # 🎉 Logo depois da cerimônia, seguiremos para o cerimonial, onde vamos aproveitar muito: vai ter piscina, bebidas geladas e um delicioso churrasco para todo mundo relaxar, dar boas risadas e comemorar juntos até o final!

                # 💖 Venha preparado para viver uma tarde e noite inesquecíveis ao nosso lado!

        with ui.element("div").classes("bg-olive-1 w-screen h-screen").props('id=roteiro'):
            with ui.element("div").classes('max-w-[1200px] mx-auto pt-20 p-4'):
    
 
                with ui.column().classes('w-full mt-12'):
                    def step(icon_name, title, description):
                        with ui.column().classes('relative pl-12'):
                            with ui.row().classes('items-center absolute top-0 left-0'):
                                ui.icon(icon_name, size='lg').classes('w-16 h-16 rounded-full bg-white p-1 flex-shrink-0')
                                ui.label(title).classes('text-lg font-semibold text-gray-900 text-white')

                            ui.element('div').classes('absolute top-14 left-9 w-0.5 bg-white').style('height: calc(100% - 2rem)')

                            ui.html(description).classes('ms-10 mt-16 text-gray-700 whitespace-normal text-white text-justify')

                    step(
                        'event_available',
                        'Convite',
                        '✨ <strong>Bem-vindo!</strong> ✨<br>'
                        'É uma alegria ter você aqui.<br>'
                        'Para usar o nosso site direitinho, confira o link exclusivo que enviamos.<br>'
                        'e confirme sua presença no nosso grande dia.<br>'
                        'Sua presença vai tornar esse momento ainda mais especial! 💖'
                    )

                    step(
                        'card_giftcard',
                        'Presentes',
                        '🎁 <strong>Sobre os presentes:</strong><br>'
                        'O mais importante é ter você celebrando com a gente!<br>'
                        'Mas, se quiser nos presentear, deixamos algumas opções:<br>'
                        '1️⃣ Escolha um presente no nosso site e marque o que gostaria de nos dar.<br>'
                        '2️⃣ Se preferir, leve o presente pessoalmente no dia do casamento.<br>'
                        '3️⃣ Ou, se for mais prático, contribua com qualquer valor através do nosso Pix.<br>'
                        'Fique à vontade para escolher a forma mais confortável pra você! 💕'
                    )

                    step(
                        'favorite',
                        'Prewedding',
                        '📸 <strong>Nosso Prewedding:</strong><br>'
                        'Aproveite para ver um pouquinho do nosso amor antes do grande dia!<br>'
                        'Preparamos algumas fotos especiais para dividir esse momento com você.<br>'
                        'Esperamos que goste de cada detalhe! 💑✨'
                    )

                    step(
                        'done_all',
                        'Finalizado',
                        '✅ <strong>Tudo pronto!</strong><br>'
                        'Agora é só aguardar o grande dia.<br>'
                        'Agradecemos de coração por fazer parte dessa história! 💍❤️'
                    )

        ui.element("div").classes("bg-olive-1 w-screen h-[350px]")