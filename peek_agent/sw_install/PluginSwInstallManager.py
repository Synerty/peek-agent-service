from peek_agent.plugin.AgentPluginLoader import agentPluginLoader
from peek_platform.sw_install.PluginSwInstallManagerABC import PluginSwInstallManagerABC


class PluginSwInstallManager(PluginSwInstallManagerABC):
    def notifyOfPluginVersionUpdate(self, pluginName, targetVersion):
        agentPluginLoader.loadPlugin(pluginName)


pluginSwInstallManager = PluginSwInstallManager()
