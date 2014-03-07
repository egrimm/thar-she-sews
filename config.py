config = {

    # webapp2 sessions
    'webapp2_extras.sessions': {'secret_key': '_MURPHY_THE_WHALE_'},

    # webapp2 authentication
    'webapp2_extras.auth': {'user_model': 'users',
                            'cookie_name': 'session_name'},

    # jinja2 templates
    'webapp2_extras.jinja2': {'template_path': ['templates']},

    'app_name': 'Thar She Sews',

} # end config