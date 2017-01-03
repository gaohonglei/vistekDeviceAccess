# **********************************************************************
#
# Copyright (c) 2003-2015 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.1
#
# <auto-generated>
#
# Generated from file `Process.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if 'Process' not in _M_Ice.__dict__:
    _M_Ice.Process = Ice.createTempClass()
    class Process(Ice.Object):
        '''An administrative interface for process management. Managed servers must
implement this interface.

A servant implementing this interface is a potential target
for denial-of-service attacks, therefore proper security precautions
should be taken. For example, the servant can use a UUID to make its
identity harder to guess, and be registered in an object adapter with
a secured endpoint.'''
        def __init__(self):
            if Ice.getType(self) == _M_Ice.Process:
                raise RuntimeError('Ice.Process is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Ice::Process')

        def ice_id(self, current=None):
            return '::Ice::Process'

        def ice_staticId():
            return '::Ice::Process'
        ice_staticId = staticmethod(ice_staticId)

        def shutdown(self, current=None):
            '''Initiate a graceful shut-down.'''
            pass

        def writeMessage(self, message, fd, current=None):
            '''Write a message on the process' stdout or stderr.

Arguments:
    message The message.

    fd 1 for stdout, 2 for stderr.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Process)

        __repr__ = __str__

    _M_Ice.ProcessPrx = Ice.createTempClass()
    class ProcessPrx(Ice.ObjectPrx):

        '''Initiate a graceful shut-down.'''
        def shutdown(self, _ctx=None):
            return _M_Ice.Process._op_shutdown.invoke(self, ((), _ctx))

        '''Initiate a graceful shut-down.'''
        def begin_shutdown(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.Process._op_shutdown.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Initiate a graceful shut-down.'''
        def end_shutdown(self, _r):
            return _M_Ice.Process._op_shutdown.end(self, _r)

        '''Write a message on the process' stdout or stderr.

Arguments:
    message The message.

    fd 1 for stdout, 2 for stderr.'''
        def writeMessage(self, message, fd, _ctx=None):
            return _M_Ice.Process._op_writeMessage.invoke(self, ((message, fd), _ctx))

        '''Write a message on the process' stdout or stderr.

Arguments:
    message The message.

    fd 1 for stdout, 2 for stderr.'''
        def begin_writeMessage(self, message, fd, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Ice.Process._op_writeMessage.begin(self, ((message, fd), _response, _ex, _sent, _ctx))

        '''Write a message on the process' stdout or stderr.

Arguments:
    message The message.

    fd 1 for stdout, 2 for stderr.'''
        def end_writeMessage(self, _r):
            return _M_Ice.Process._op_writeMessage.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Ice.ProcessPrx.ice_checkedCast(proxy, '::Ice::Process', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Ice.ProcessPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::Ice::Process'
        ice_staticId = staticmethod(ice_staticId)

    _M_Ice._t_ProcessPrx = IcePy.defineProxy('::Ice::Process', ProcessPrx)

    _M_Ice._t_Process = IcePy.defineClass('::Ice::Process', Process, -1, (), True, False, None, (), ())
    Process._ice_type = _M_Ice._t_Process

    Process._op_shutdown = IcePy.Operation('shutdown', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Process._op_writeMessage = IcePy.Operation('writeMessage', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_int, False, 0)), (), None, ())

    _M_Ice.Process = Process
    del Process

    _M_Ice.ProcessPrx = ProcessPrx
    del ProcessPrx

# End of module Ice