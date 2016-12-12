'''
 *
 *  Copyright Synerty Pty Ltd 2013
 *
 *  This software is proprietary, you are not free to copy
 *  or redistribute this code in any format.
 *
 *  All rights to this software are reserved by 
 *  Synerty Pty Ltd
 *
 * Website : http://www.synerty.com
 * Support : support@synerty.com
 *
'''
import logging

from peek_platform.file_config.PeekFileConfigABC import PeekFileConfigABC
from peek_platform.file_config.PeekFileConfigPeekServerClientMixin import \
    PeekFileConfigPeekServerClientMixin
from peek_platform.file_config.PeekFileConfigPlatformABC import \
    PeekFileConfigPlatformABC

logger = logging.getLogger(__name__)


class PeekAgentConfig(PeekFileConfigABC,
                      PeekFileConfigPeekServerClientMixin,
                      PeekFileConfigPlatformABC):
    """
    This class creates a basic agent configuration
    """

    @property
    def platformVersion(self):
        import peek_agent
        return peek_agent.__version__


peekAgentConfig = PeekAgentConfig()
