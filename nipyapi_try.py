import nipyapi

nipyapi.config.nifi_config.host = 'http://eurepprodnifi.sirioninc.net:8443/nifi-api'

print(nipyapi.canvas.get_root_pg_id())