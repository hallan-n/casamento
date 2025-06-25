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
        </style>
    """
    )
