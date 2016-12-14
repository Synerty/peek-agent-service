from peek_agent.plugin.PluginAgentLoader import pluginAgentLoader
from peek_platform.sw_install.PluginSwInstallManagerBase import PluginSwInstallManagerBase


class PluginSwInstallManager(PluginSwInstallManagerBase):
    def notifyOfPluginVersionUpdate(self, pluginName, targetVersion):
        pluginAgentLoader.loadPlugin(pluginName)


pluginSwInstallManager = PluginSwInstallManager()
