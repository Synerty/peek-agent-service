from peek_agent.papp.PappAgentLoader import pappAgentLoader
from peek_platform.sw_install.PappSwInstallManagerBase import PappSwInstallManagerBase


class PappSwInstallManager(PappSwInstallManagerBase):
    def notifyOfPappVersionUpdate(self, pappName, targetVersion):
        pappAgentLoader.loadPapp(pappName)


pappSwInstallManager = PappSwInstallManager()
