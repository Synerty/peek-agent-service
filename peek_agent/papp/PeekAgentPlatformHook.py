from typing import Optional

from papp_base.agent.PeekAgentPlatformHookABC import PeekAgentPlatformHookABC


class PeekAgentPlatformHook(PeekAgentPlatformHookABC):
    def getOtherPappApi(self, pappName: str) -> Optional[object]:
        return None
