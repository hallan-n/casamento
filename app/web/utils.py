import json

from nicegui import app, ui

app.add_static_files("/assets", "app/web/assets")


import re

async def get_current_user():
    current_user = await ui.run_javascript(
        'localStorage.getItem("current_user");', timeout=30
    )
    if current_user:
        current_user = re.sub(r'[\x00-\x1f\x7f]', '', current_user)
        return json.loads(current_user)
    return {}


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
        html {
            scroll-behavior: smooth;
        }
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .nicegui-content {
            padding: 0;
            margin: 0;
        }
        .home-lg {
            background-image: url('assets/mask2.png');
            background-size: contain;      
            background-repeat: no-repeat;          
        }
        .home-sm {
            display: none;
            height: 100vh;
            width: 100vw;
            background-image: url('https://raw.githubusercontent.com/hallan-n/cdn-free/main/prewedding/29.jpg');
            background-size: cover;      
            background-repeat: no-repeat;
            background-size: 160%;
            background-position: 20% 40%;
            opacity: 40%;               
        }
        .home-content {
            z-index: auto;
        }
        .bg-olive-1{
            background-color: #86895d;
        }
        @media (max-width: 1353px) {
            .home-lg { display: none; }
            .home-sm { display: block; }
            .home-content { z-index: 100; }
        }
        body {
            font-family: 'Poppins', sans-serif;
        }
    </style>
    """
    )
