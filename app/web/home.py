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
                'lg:justify-end justify-center max-w-[1200px] mx-auto p-6'
            ):
                with ui.element("div").classes('w-full max-w-[400px] text-2xl text-white text-center mb-44'):
                    ui.image("app/web/assets/logo_full.svg")
                    ui.image("app/web/assets/divider.svg")
                    ui.label("Save the Date").classes('mt-2 lg:[text-shadow:none] [text-shadow:2px_2px_10px_rgba(0,0,0)]')
                    ui.label("Sábado, 04 de Outubro, às 16h!").classes('text-bold mt-2 lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0,3)]')
                    ui.label("Gostaríamos de convidá-lo(a)").classes('mt-2').classes('lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0,3)]')
                    ui.label("para celebrar conosco este").classes('mt-2').classes('lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0,3)]')
                    ui.label("momento especial de união.").classes('mt-2').classes('lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0,3)]')
                    with ui.link('', '#info').classes('block mt-4 text-white text-md'):
                        ui.label("Confira as informações do casamento").classes('mt-8').classes('lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0,3)]')
                        ui.icon('arrow_downward').classes(
                            'text-5xl lg:[text-shadow:none] [text-shadow:1px_1px_15px_rgba(0,0,0)]'
                        )
                    

        with ui.element("div").classes("bg-olive-1 w-screen h-screen p-4").props("id=info"):
            with ui.element("div").classes('w-full h-full max-w-[1200px] mx-auto'):
                ui.label("Nosso Grande Dia").classes('text-2xl text-bold text-white pt-24 py-10')
                with ui.element('div').classes('flex flex-nowrap md:flex-row flex-col gap-4 justify-between items-center'):
                    ui.html('''
                        📅 O nosso casamento começará às 16h, na <b>Paróquia Santo André Apóstolo</b>, onde vamos celebrar esse momento tão especial junto com você! <br>
                        <a href="https://maps.app.goo.gl/6g5qokyjxQN5AKo6A" target="_blank" class="text-blue-200 underline hover:text-blue-300">📍R. Santo André, 387 - André Carloni, Serra - ES, 29161-851</a><br><br>
                        Depois da cerimônia, vamos para um cerimonial chamado <b>Cerimonial Espaço Encantado</b> com piscina, churrasco e muita alegria!<br>
                        <a href="https://maps.app.goo.gl/pUR7XXg8yEPora3A8" target="_blank" class="text-blue-200 underline hover:text-blue-300">
                            📍Beco Dois - Barro Branco, Serra - ES, 29170-721
                        </a><br><br><a href="#roteiro" class="underline hover:text-zinc-300">Confira o roteiro</a>
                    ''').classes('w-full md:w-1/2 text-2xl text-white text-justify')

  
                    with ui.element('div').classes('grid md:grid-cols-2 grid-cols-4 gap-4'):
                        ui.element('img').classes('md:w-56 md:h-56 w-36 h-36 object-cover rounded-lg').props('src="https://raw.githubusercontent.com/hallan-n/cdn-free/main/prewedding/igreja.png"')
                        ui.element('img').classes('md:w-56 md:h-56 w-36 h-36 object-cover rounded-lg').props('src="https://lh3.googleusercontent.com/gps-cs-s/AC9h4noZVt7n0O5IPq1MxZZMTXzE5lgGEuV1vLqADf_mQELws7mQMmINcmkNnkthVTyrRU9BWLVX8Ig7acfhRmKhSdJg0LmNM_984uIw_Np5ATbncU5e1An4xTjBVvdedwmqFCn_2EW-NA=s680-w680-h510-rw"')
                        ui.element('img').classes('md:w-56 md:h-56 w-36 h-36 object-cover rounded-lg').props('src="https://lh3.googleusercontent.com/p/AF1QipNqi_aE1LQRxEdKSKNuT_l-ELmWT-A2K7x_1BdZ=s680-w680-h510-rw"')
                        ui.element('img').classes('md:w-56 md:h-56 w-36 h-36 object-cover rounded-lg').props('src="https://lh3.googleusercontent.com/gps-cs-s/AC9h4nq5UNITCt_MQ2qUGtjxtksWUBLSiPKX1ysnduqFuLp5XktnvlruYU5Z7MJphuJ5lFpxGsLpQupY1Wi2z-KLAvh8g86lcjn-0z6bsG5mi2w9Sbs7jAV2uJ6rXA3km2UPJ89lW52Ky9Ke7CA=s680-w680-h510-rw"')
        
        
        with ui.element("div").classes("bg-olive-1 w-screen h-screen p-4").props('id=roteiro'):
            
            with ui.element("div").classes('max-w-[1200px] mx-auto'):                
                ui.label("Roteiro").classes('text-2xl text-bold text-white pt-12 pb-4')
 
                with ui.column().classes('w-full'):
                    def step(icon_name, title, description):
                        with ui.column().classes('relative pl-12'):
                            with ui.row().classes('items-center absolute top-0 left-0'):
                                ui.icon(icon_name, size='lg').classes('w-16 h-16 rounded-full bg-white p-1 flex-shrink-0')
                                ui.label(title).classes('text-2xl font-semibold text-gray-900 text-white')

                            ui.element('div').classes('absolute top-14 left-9 w-0.5 bg-white').style('height: calc(100% - 2rem)')

                            ui.html(description).classes('text-lg ms-10 mt-16 text-gray-700 whitespace-normal text-white text-justify')

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

        ui.element("div").classes("bg-olive-1 w-screen h-screen")