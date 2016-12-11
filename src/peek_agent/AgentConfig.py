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
from ConfigParser import SafeConfigParser, NoOptionError, NoSectionError

import os
import logging
logger = logging.getLogger(__name__)



class AgentConfig(object):
    """
    This class creates a basic agent configuration
    """

    defaultFileChmod = 0600
    defaultDirChmod = 0700

    _initValAgentHomeName = None

    #### Peek Defaults ###
    _diskStorage = 'disk_storage'

    _homePath = 'home_path'
    _tmpPath = 'tmp_path'

    # ------------ LOGGING SECTION -------------
    _loggingSection = "logging"

    _loggingLevelKey = "default_level"
    _loggingLevelDefault = "INFO"

    # ------------ GENERIC AGENT SECTION -------------
    _agentSection = "agent"

    _agentName = "agent_name"
    _initValAgentName = None

    _agentVersion = "agent_version"

    _agentAutoUpdate = "agent_auto_update"
    _defaultAgentAutoUpdate = "true"

    _agentSymlinkName = "agent_symlink_dir"
    _initValAgentSymlinkName = "peek_agent"

    # ------------ PEEK SERVER SECTION -------------
    _peekServerSection = 'peek_server'

    _peekServerPort = "port"
    _defaultPeekPort = "8000"

    _peekServerHost = "host"
    _defaultPeekHost = "127.0.0.1"

    _peekModelSetName = "model_set_name"
    _initValModelSetName = None

    @classmethod
    def initialise(cls, modelSetName,
                   agentHomeName="peek_agent",
                   agentName="peek_agent",
                   agentSymlinkName="peek_agent"):
        cls._initValModelSetName = modelSetName
        cls._initValAgentName = agentName
        cls._initValAgentHomeName = agentHomeName
        cls._initValAgentSymlinkName = agentSymlinkName

    def __init__(self):
        '''
        Constructor
        '''
        assert self._initValModelSetName != None, ("Call AgentConfig.initialise()"
                                                   " on agent startup")

        appHome = os.environ.get("PEEK_AGENT_HOME",
                                 '~/%s.home' % self._initValAgentHomeName)

        self.homePath = os.path.expanduser(appHome)
        if not os.path.isdir(self.homePath):
            assert (not os.path.exists(self.homePath))
            os.makedirs(self.homePath, self.defaultDirChmod)

        self._configFilePath = os.path.join(self.homePath, 'config.cfg')

        self._hp = '%(' + self._homePath + ')s'

        if not os.path.exists(self._configFilePath):
            self._writeDefaults()

        # Update the agent name
        self._setStr(self._agentSection, self._agentName, self._initValAgentName)

    def _cfg(self):
        parser = SafeConfigParser()
        if not parser.read(self._configFilePath):
            raise Exception(
                "Failed to parse config file %s" % self._configFilePath)
        return parser

    def _save(self, parser):
        parser.write(open(self._configFilePath, 'w'))

    def _writeDefaults(self):
        parser = SafeConfigParser()
        parser.add_section(self._diskStorage)
        parser.set(self._diskStorage, self._homePath, self.homePath)

        parser.add_section(self._peekServerSection)
        parser.set(self._peekServerSection, self._peekServerPort, self._defaultPeekPort)
        parser.set(self._peekServerSection, self._peekServerHost, self._defaultPeekHost)

        self._save(parser)
        os.chmod(self._configFilePath, self.defaultFileChmod)

    def _chkDir(self, path):
        if not os.path.isdir(path):
            assert (not os.path.exists(path))
            os.makedirs(path, self.defaultDirChmod)
        return path

    def _getDir(self, key, defaultDir):
        parser = self._cfg()
        try:
            return self._chkDir(parser.get(self._diskStorage, key))
        except NoOptionError:
            parser.set(self._diskStorage, key, self._hp + '/' + defaultDir)
            self._save(parser)
            return self._chkDir(parser.get(self._diskStorage, key))

    def _getStr(self, section, key, defaultVal):
        parser = self._cfg()
        try:
            return parser.get(section, key)

        except NoSectionError:
            parser.add_section(section)
            self._save(parser)
            return self._getStr(section, key, defaultVal)

        except NoOptionError:
            parser.set(section, key, defaultVal)
            self._save(parser)
            return self._getStr(section, key, defaultVal)

    def _getInt(self, section, key, defaultVal):
        try:
            strVal = self._getStr(section, key, str(defaultVal))
            return int(strVal)
        except ValueError as e:
            logger.exception(e)
            logger.error("Config section=%s, key=%s couldn't be converted to int"
                         " returning default of %s", section, key, defaultVal)
            return defaultVal


    def _setStr(self, section, key, value):
        self._getStr(section, key, value)

    ### DISK SECTION ###

    @property
    def tmpPath(self):
        return self._getDir(self._tmpPath, 'tmp')

    ### LOGGING SECTION ###

    @property
    def loggingLevel(self):
        lvl =  self._getStr(self._loggingSection,
                            self._loggingLevelKey,
                            self._loggingLevelDefault)

        if lvl in logging._levelNames:
            return lvl

        logger.warn("Logging level %s is not valid, defauling to INFO", lvl)
        return logging.INFO


    ### GENERIC AGENT SECTION ###

    @property
    def agentName(self):
        return self._getStr(self._agentSection, self._agentName, self._initValAgentName)

    # --- Agent Version
    @property
    def agentVersion(self):
        return self._getStr(self._agentSection, self._agentVersion, "0.0.0")

    @agentVersion.setter
    def agentVersion(self, value):
        parser = self._cfg()
        parser.set(self._agentSection, self._agentVersion, value)
        self._save(parser)

    # --- Agent Version
    @property
    def agentAutoUpdate(self):
        return "true" == self._getStr(self._agentSection,
                                      self._agentAutoUpdate,
                                      self._defaultAgentAutoUpdate)

    # --- Agent Version
    @property
    def agentSymlinkName(self):
        return self._getStr(self._agentSection,
                            self._agentSymlinkName,
                            self._initValAgentSymlinkName)

    ### SERVER SECTION ###
    @property
    def peekServerPort(self):
        return int(self._getStr(self._peekServerSection,
                                self._peekServerPort, self._defaultPeekPort))

    @property
    def peekServerHost(self):
        return self._getStr(self._peekServerSection,
                            self._peekServerHost, self._defaultPeekPort)

    @property
    def modelSetName(self):
        return self._getStr(self._peekServerSection,
                            self._peekModelSetName,
                            self._initValModelSetName)
