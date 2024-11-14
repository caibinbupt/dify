from configs import dify_config
from app_factory import create_flask_app_with_configs

from services.model_provider_service import ModelProviderService
from core.model_runtime.entities.model_entities import ModelType

app = create_flask_app_with_configs()
app.secret_key = dify_config.SECRET_KEY
from extensions import ext_database, ext_redis
ext_database.init_app(app)
ext_redis.init_app(app)

ctx = app.app_context()
ctx.push()

mps = ModelProviderService()

tenant_id='c9c54227-a09d-4484-9999-a538e740cd2e'  #缺省的工作空间

plist = mps.get_provider_list(tenant_id)
print(plist)

pplist = mps.get_models_by_provider(tenant_id, 'openai')
print(pplist)

dlist = mps.provider_manager.get_default_model(tenant_id, ModelType.LLM) #缺省模型
print(dlist)


