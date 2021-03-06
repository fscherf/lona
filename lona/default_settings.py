import os

MAX_WORKERS = 10

# routing
ROUTING_TABLE = 'lona.default_routes.routes'

# templating
CORE_TEMPLATE_DIRS = [
    os.path.join(os.path.dirname(__file__), 'templates'),
]

TEMPLATE_DIRS = []

FRONTEND_TEMPLATE = 'lona/frontend.html'
ERROR_403_TEMPLATE = 'lona/403.html'
ERROR_404_TEMPLATE = 'lona/404.html'
ERROR_500_TEMPLATE = 'lona/500.html'

TEMPLATE_EXTRA_CONTEXT = {}

# static files
STATIC_DIRS = []
STATIC_URL_PREFIX = '/static/'
STATIC_FILES_SERVE = True
STATIC_FILES_STYLE_TAGS_TEMPLATE = 'lona/style_tags.html'
STATIC_FILES_SCRIPT_TAGS_TEMPLATE = 'lona/script_tags.html'
STATIC_FILES_SYMBOLS_TEMPLATE = 'lona/lona-symbols.js'
STATIC_FILES_ENABLED = []
STATIC_FILES_DISABLED = []
STATIC_FILES_CLIENT_URL = '/lona/lona.js'

CLIENT_RECOMPILE = False

# state
SERVER_STATE_ATOMIC = True

# views
CORE_FRONTEND_VIEW = 'lona.default_views.FrontendView'
FRONTEND_VIEW = ''

# error views
CORE_ERROR_403_VIEW = 'lona.default_views.Error403View'
CORE_ERROR_404_VIEW = 'lona.default_views.Error404View'
CORE_ERROR_500_VIEW = 'lona.default_views.Error500View'

ERROR_403_VIEW = ''
ERROR_404_VIEW = ''
ERROR_500_VIEW = ''

# middlewares
CORE_MIDDLEWARES = [
    'lona.middlewares.LonaMessageMiddleware',
]

MIDDLEWARES = []

# hooks
STARTUP_HOOKS = []
SHUTDOWN_HOOKS = []

# shell
CORE_COMMANDS = [
    'lona.shell.commands.lona_server_state.LonaServerStateCommand',
    'lona.shell.commands.lona_connections.LonaConnectionsCommand',
    'lona.shell.commands.lona_settings.LonaSettingsCommand',
    'lona.shell.commands.lona_routes.LonaRoutesCommand',
    'lona.shell.commands.lona_views.LonaViewsCommand',
    'lona.shell.commands.lona_info.LonaInfoCommand',
]

COMMANDS = []
