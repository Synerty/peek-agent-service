import logging

from rapui.vortex.VortexClient import VortexClient

logger = logging.getLogger(__name__)


class ModData:
    peekVortexClient = VortexClient()


def sendPayloadToPeekServer(payload):
    vortexMsg = payload.toVortexMsg()
    return sendVortexMsgToPeekServer(vortexMsg)


def sendVortexMsgToPeekServer(vortexMsg):
    return ModData.peekVortexClient.sendEncodedPayload(vortexMsg)


def addReconnectPayload(vortexMsg):
    return ModData.peekVortexClient.addReconnectPayload(vortexMsg)


def connectVortexClient(agentConfig):
    serverPort = agentConfig.peekServerPort
    serverHost = agentConfig.peekServerHost

    logger.info('Connecting to Peek Server %s:%s', serverHost, serverPort)
    return ModData.peekVortexClient.connect(serverHost, serverPort)
