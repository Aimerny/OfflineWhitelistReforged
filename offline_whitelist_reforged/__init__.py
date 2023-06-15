from mcdreforged.api.types import PluginServerInterface

from offline_whitelist_reforged.plugin import Plugin

plugin: Plugin


def on_load(server: PluginServerInterface, old):
    global plugin
    plugin = Plugin(server)
