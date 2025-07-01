
from nicegui import ui
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
        <link href="https://fonts.googleapis.com/css2?family=Funnel+Sans:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Funnel Sans', sans-serif;
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
        </style>
    """
    )
