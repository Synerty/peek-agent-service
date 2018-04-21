import platform

import peek_agent
from peek_platform.sw_install.PeekSwInstallManagerABC import PeekSwInstallManagerABC
from peek_platform.util.LogUtil import setupServiceLogOutput

try:
    import win32serviceutil
    import win32service
    import win32event
except ImportError as e:
    if platform.system() is "Windows":
        raise

from twisted.internet import reactor

from peek_agent import run_peek_agent


class PeekSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "peek_agent"
    _svc_display_name_ = "Peek Agent " + peek_agent.__version__

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

        reactor.addSystemEventTrigger('after', 'shutdown', self._notifyOfStop)

    def _notifyOfStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def _notifyOfStart(self, _):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        reactor.callFromThread(reactor.stop)

    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        reactor.callLater(1, self._notifyOfStart)
        run_peek_agent.main()
        reactor.run()


# Patch the restart method for windows services
class _Restart:
    def _restartProcess(self):
        reactor.callFromThread(reactor.stop)


# Patch the restart call for windows
PeekSwInstallManagerABC.restartProcess = _Restart._restartProcess


# end patch

def main():
    setupServiceLogOutput(PeekSvc._svc_name_)
    win32serviceutil.HandleCommandLine(PeekSvc)


if __name__ == '__main__':
    main()
