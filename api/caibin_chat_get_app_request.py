from configs import dify_config
from app_factory import create_flask_app_with_configs

app = create_flask_app_with_configs()
app.secret_key = dify_config.SECRET_KEY
from extensions import ext_database, ext_redis
ext_database.init_app(app)
ext_redis.init_app(app)
ctx = app.app_context()
ctx.push()

client = app.test_client()

#resp=client.get('/chat/3w7xivLni2XLsy02')

header = {'user_id': '1b1aa07c-d423-4cd8-93e1-689fced6e6c9',
          'Content-Type': 'application/json'}  # caibinbupt@hotmail.com

# 获取具体的APP
resp = client.get("/console/api/apps/bcaedf15-d27d-4832-96f0-8bb29d112220", headers=header)
json_str = json.dumps(resp.get_json(), indent=4, ensure_ascii=False)
print(json_str)


# 获取APP列表
# resp = client.get("/console/api/apps", headers=header)
# json_str = json.dumps(resp.get_json(), indent=4, ensure_ascii=False)
# print(json_str)

#
# resp = client.get("/console/api/workspaces/current/model-providers", headers=header)
# print(resp.get_json())
#
# resp = client.get("/console/api/ping")
# print(resp)
