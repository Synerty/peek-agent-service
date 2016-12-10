from peek_agent.papp.PappAgentLoader import pappAgentLoader
from peek_platform.sw_install.PeekSwInstallManagerBase import PeekSwInstallManagerBase

__author__ = 'synerty'


class PeekSwInstallManager(PeekSwInstallManagerBase):

    def _stopCode(self):
        pappAgentLoader.unloadAllPapps()

    def _upgradeCode(self):
        pass

    def _startCode(self):
        pappAgentLoader.loadAllPapps()


peekSwInstallManager = PeekSwInstallManager()
