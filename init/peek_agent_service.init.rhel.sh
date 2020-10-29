#!/bin/sh
#
# peek_agent_service_pof Peek Agent for PowerOn Fusion
#
# chkconfig:   2345 20 80
# description: Peek Agent for PowerOn Fusion
#

### BEGIN INIT INFO
# Provides: peek_agent_service_pof
# Required-Start:
# Required-Stop:
# Should-Start:
# Should-Stop:
# Default-Start: 3 4 5
# Default-Stop: 0 1 2 6
# Short-Description: Peek Agent for PowerOn Fusion
# Description: Peek Agent for PowerOn Fusion
### END INIT INFO

# Source function library.
. /etc/rc.d/init.d/functions

HOME=/users/enmac
DIR=${HOME}/peek_agent_service_pof
DAEMON_NAME=peek_agent_service_pof
DAEMON_USER=enmac

LAUNCHER="$DIR/run_peek_agent_service.sh"

# Change the next 3 lines to suit where you install your script and what you want to call it
exec="$DIR/run_peek_agent_service.pyc"
prog="$DAEMON_NAME"


[ -e /etc/sysconfig/$prog ] && . /etc/sysconfig/$prog

lockfile=/var/lock/subsys/$prog

start() {
    echo -n $"Starting $prog: "
    # if not running, start it up here, usually something like "daemon $exec"
    su - $DAEMON_USER -c "$LAUNCHER" && success || failure

    retval=$?
    echo
    [ $retval -eq 0 ] && touch $lockfile
    return $retval
}

stop() {
    echo -n $"Stopping $prog: "
    # stop it here, often "killproc $prog"
    pkill -9 -f ${exec} && success || failure
    retval=$?
    echo
    [ $retval -eq 0 ] && rm -f $lockfile
    return $retval
}

restart() {
    stop
    start
}

rh_status() {
    # run checks to determine if the service is running or use generic status
    if pgrep -lf ${exec}; then
        echo "$prog is running"
        true
    else
        echo "$prog is stopped"
        false
    fi
}

rh_status_q() {
    rh_status >/dev/null 2>&1
}


case "$1" in
    start)
        rh_status_q && exit 0
        $1
        ;;
    stop)
        rh_status_q || exit 0
        $1
        ;;
    restart)
        $1
        ;;
    status)
        rh_status
        ;;
    *)
        echo $"Usage: $0 {start|stop|status|restart}"
        exit 2
esac
exit $?

