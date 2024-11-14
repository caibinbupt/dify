from app import DifyApp, initialize_extensions
from config import Config

from core.tools.provider.builtin.wecom.tools.wecom_group_bot import WecomGroupBotTool
from services.model_provider_service import ModelProviderService

app = DifyApp(__name__)
app.config.from_object(Config())
initialize_extensions(app)

ctx = app.app_context()
ctx.push()

tool_parameters = {
    'content': 'Dify Tool 测试',
    'hook_key': 'bae3f274-5b5a-4e15-b308-df08739437db'
}

wt = WecomGroupBotTool()

tool_parameters = {
    'content': 'Dify Tool 测试',
    'hook_key': 'bae3f274-5b5a-4e15-b308-df08739437db'
}

ret = wt._invoke('1b1aa07c-d423-4cd8-93e1-689fced6e6c9', tool_parameters)

print(ret)   #type=<MessageType.TEXT: 'text'> message='Text message sent successfully' meta=None save_as=''


# wt = WecomGroupBotTool()
#
# tool_parameters = {
#     'content': 'Dify Tool 测试',
#     'hook_key': 'bae3f274-5b5a-4e15-b308-df08739437db'
# }
#
# ret = wt._invoke('1b1aa07c-d423-4cd8-93e1-689fced6e6c9', tool_parameters)
# print(ret)   #type=<MessageType.TEXT: 'text'> message='Text message sent successfully' meta=None save_as=''

