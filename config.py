from environs import Env

env = Env()
env.read_env()

bot_token = env.str("bot_token")
localhost = env.str("localhost")

# pg_user = env.str("pg_user")
# pg_password = env.str("pg_password")
# pg_name = env.str("pg_name")
# pg_host = env.str("pg_host")
# pg_port = env.str("pg_port")
# pg_url = f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_name}"
