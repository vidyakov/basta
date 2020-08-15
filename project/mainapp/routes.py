from .controllers import IndexPage, ContactPage


MAINAPP_ROUTES = {
    '/': IndexPage(),
    '/contact/': ContactPage()
}
