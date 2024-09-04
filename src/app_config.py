from dynaconf import Dynaconf

app_settings = Dynaconf(
    envvar_prefix='INV_APP',
    settings_files=['settings.toml', 'settings-dev.toml'],
    environments=True,
    load_dotenv=True,
    default_env='default',
    env='development',
    merge_enabled=True,
)
