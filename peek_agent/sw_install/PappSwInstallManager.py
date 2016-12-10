from peek_agent.papp.PappAgentLoader import pappAgentLoader
from peek_platform import PappSwInstallManagerBase


class PappSwInstallManager(PappSwInstallManagerBase):
    def notifyOfPappVersionUpdate(self, pappName, targetVersion):
        pappAgentLoader.loadPapp(pappName)


pappSwInstallManager = PappSwInstallManager()
