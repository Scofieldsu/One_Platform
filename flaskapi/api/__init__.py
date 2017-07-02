# encoding = utf-8
from uuid import uuid4
from flask import Blueprint
from jsonrpc.backend.flask import JSONRPCAPI
from jsonrpc.dispatcher import Dispatcher


class MyJsonRpcApi(JSONRPCAPI):

    def as_blueprint(self, name=None, url='/'):
        blueprint = Blueprint(name if name else str(uuid4()), __name__)
        blueprint.add_url_rule(
            url, view_func=self.jsonrpc, methods=['POST'])
        blueprint.add_url_rule(
            '/map', view_func=self.jsonrpc_map, methods=['GET'])
        return blueprint


dispatcher = Dispatcher()
api = MyJsonRpcApi(dispatcher)
api_add = api.dispatcher.add_method
api_class = api.dispatcher.add_class