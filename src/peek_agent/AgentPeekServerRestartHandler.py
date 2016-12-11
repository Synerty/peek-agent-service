'''
Created on 09/07/2014

@author: synerty
'''
import logging

from peek_agent.PeekVortexClient import addReconnectPayload
from rapui.vortex.Payload import Payload
from rapui.vortex.PayloadEndpoint import PayloadEndpoint

__author__ = 'peek'

logger = logging.getLogger(__name__)

# The filter we listen on
agentEchoFilt = {'key': "peek.agent.echo"}  # LISTEN / SEND


class AgentPeekServerRestartHandler(object):
    def __init__(self):
        self._ep = PayloadEndpoint(agentEchoFilt, self._process)
        self._lastPeekServerVortexUuid = None

        # When the vortex reconnects, this will make the server echo back to us.
        addReconnectPayload(Payload(filt=agentEchoFilt))

    def _process(self, payload, vortexUuid, **kwargs):
        if self._lastPeekServerVortexUuid is None:
            self._lastPeekServerVortexUuid = vortexUuid
            return

        if self._lastPeekServerVortexUuid == vortexUuid:
            return

        logger.info("Peek Server restart detected, restarting agent")
        from peek_agent.sw_update.AgentSwUpdateManager import AgentSwUpdateManager
        AgentSwUpdateManager.restartAgent()


__agentPeekServerRestartHandler = AgentPeekServerRestartHandler()
