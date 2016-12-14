from peek_agent.plugin.AgentPluginLoader import agentPluginLoader
from peek_platform.sw_install.PluginSwInstallManagerBase import PluginSwInstallManagerBase


class PluginSwInstallManager(PluginSwInstallManagerBase):
    def notifyOfPluginVersionUpdate(self, pluginName, targetVersion):
        agentPluginLoader.loadPlugin(pluginName)


pluginSwInstallManager = PluginSwInstallManager()
