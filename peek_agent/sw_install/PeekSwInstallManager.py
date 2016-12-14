from peek_agent.plugin.AgentPluginLoader import agentPluginLoader
from peek_platform.sw_install.PeekSwInstallManagerBase import PeekSwInstallManagerBase

__author__ = 'synerty'


class PeekSwInstallManager(PeekSwInstallManagerBase):

    def _stopCode(self):
        agentPluginLoader.unloadAllPlugins()

    def _upgradeCode(self):
        pass

    def _startCode(self):
        agentPluginLoader.loadAllPlugins()


peekSwInstallManager = PeekSwInstallManager()
