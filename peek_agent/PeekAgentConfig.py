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

from peek_platform import PeekFileConfigBase
from peek_platform import \
    PeekFileConfigPeekServerClientMixin
from peek_platform import \
    PeekFileConfigPlatformMixin

logger = logging.getLogger(__name__)


class PeekAgentConfig(PeekFileConfigBase,
                      PeekFileConfigPeekServerClientMixin,
                      PeekFileConfigPlatformMixin):
    """
    This class creates a basic agent configuration
    """


peekAgentConfig = PeekAgentConfig()