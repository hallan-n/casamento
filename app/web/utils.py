import json

from nicegui import app, ui

app.add_static_files("/assets", "app/web/assets")


async def get_current_user():
    current_user = await ui.run_javascript(
        'localStorage.getItem("current_user");', timeout=30
    )
    return json.loads(current_user) if current_user else None


def is_login():
    ui.run_javascript(
        """
        if (!localStorage.getItem('access_token')) {
            window.location.href = '/web';
        }
        """
    )


def reset_css():
    ui.add_head_html(
        """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
    """
    )
    ui.add_head_html(
        """
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .nicegui-content {
            padding: 0;
            margin: 0;
        }
        .home {
            height: 100vh;
            width: 100vw;
            background-image: url('assets/mask.png');
            background-size: contain;      
            background-repeat: no-repeat;
            background-position: left top;
            z-index: 100;
                    
        }
        .bg-olive-1{
            background-color: #86895d;
        }
        @media (max-width: 800px) {
            .home {
                display: none;
            }
        }
        body {
            font-family: 'Poppins', sans-serif;
        }
    </style>
    """
    )
