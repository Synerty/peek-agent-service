import logging
from typing import Type

from papp_base.PappCommonEntryHookABC import PappCommonEntryHookABC
from papp_base.agent.PappAgentEntryHookABC import PappAgentEntryHookABC
from peek_agent.papp.PeekAgentPlatformHook import PeekAgentPlatformHook
from peek_platform.papp.PappLoaderABC import PappLoaderABC

logger = logging.getLogger(__name__)

class PappAgentLoader(PappLoaderABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        assert cls._instance is None, "PappAgentLoader is a singleton, don't construct it"
        cls._instance = PappLoaderABC.__new__(cls)
        return cls._instance

    @property
    def _entryHookFuncName(self) -> str:
        return "peekAgentEntryHook"

    @property
    def _entryHookClassType(self):
        return PappAgentEntryHookABC

    @property
    def _platformServiceNames(self) -> [str]:
        return ["agent"]


    def _loadPappThrows(self, pappName: str, EntryHookClass: Type[PappCommonEntryHookABC],
                        pappRootDir: str) -> None:
        # Everyone gets their own instance of the papp API
        platformApi = PeekAgentPlatformHook()

        pappMain = EntryHookClass(pappName=pappName,
                                  pappRootDir=pappRootDir,
                                  platform=platformApi)

        # Load the papp
        pappMain.load()

        # Start the Papp
        pappMain.start()

        self._loadedPapps[pappName] = pappMain


pappAgentLoader = PappAgentLoader()
