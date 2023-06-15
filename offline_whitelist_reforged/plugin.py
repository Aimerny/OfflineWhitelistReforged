from mcdreforged.api.types import PluginServerInterface
from offline_whitelist_reforged.util import load_whitelist
from offline_whitelist_reforged.command_handler import CommandHandler


class Plugin:

    @property
    def server(self):
        return self.__server

    @property
    def whitelist(self):
        return self.__whitelist

    @property
    def command_handler(self):
        return self.__command_handler

    def __init__(self, server: PluginServerInterface):
        self.__server = server
        self.__whitelist = load_whitelist()
        self.__command_handler = CommandHandler(server, self.__whitelist)
