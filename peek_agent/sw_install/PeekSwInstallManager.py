from peek_agent.plugin.PluginAgentLoader import pluginAgentLoader
from peek_platform.sw_install.PeekSwInstallManagerBase import PeekSwInstallManagerBase

__author__ = 'synerty'


class PeekSwInstallManager(PeekSwInstallManagerBase):

    def _stopCode(self):
        pluginAgentLoader.unloadAllPlugins()

    def _upgradeCode(self):
        pass

    def _startCode(self):
        pluginAgentLoader.loadAllPlugins()


peekSwInstallManager = PeekSwInstallManager()
