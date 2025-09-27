import reflex as rx

config = rx.Config(
    app_name="frontend",
    frontend_port=3000,
    backend_port=7999,
    api_url="http://127.0.0.1:7999",
    deploy_url="http://127.0.0.1:3000",
    backend_host="127.0.0.1",
    plugins=[
        rx.plugins.sitemap.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
