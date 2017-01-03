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
# Generated from file `Current.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy
import Ice_ObjectAdapterF_ice
import Ice_ConnectionF_ice
import Ice_Identity_ice
import Ice_Version_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Start of module Ice
__name__ = 'Ice'

if '_t_Context' not in _M_Ice.__dict__:
    _M_Ice._t_Context = IcePy.defineDictionary('::Ice::Context', (), IcePy._t_string, IcePy._t_string)

if 'OperationMode' not in _M_Ice.__dict__:
    _M_Ice.OperationMode = Ice.createTempClass()
    class OperationMode(Ice.EnumBase):
        '''The OperationMode determines the retry behavior an
invocation in case of a (potentially) recoverable error.'''

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    OperationMode.Normal = OperationMode("Normal", 0)
    OperationMode.Nonmutating = OperationMode("Nonmutating", 1)
    OperationMode.Idempotent = OperationMode("Idempotent", 2)
    OperationMode._enumerators = { 0:OperationMode.Normal, 1:OperationMode.Nonmutating, 2:OperationMode.Idempotent }

    _M_Ice._t_OperationMode = IcePy.defineEnum('::Ice::OperationMode', OperationMode, (), OperationMode._enumerators)

    _M_Ice.OperationMode = OperationMode
    del OperationMode

if 'Current' not in _M_Ice.__dict__:
    _M_Ice.Current = Ice.createTempClass()
    class Current(object):
        '''Information about the current method invocation for servers. Each
operation on the server has a Current as its implicit final
parameter. Current is mostly used for Ice services. Most
applications ignore this parameter.'''
        def __init__(self, adapter=None, con=None, id=Ice._struct_marker, facet='', operation='', mode=_M_Ice.OperationMode.Normal, ctx=None, requestId=0, encoding=Ice._struct_marker):
            self.adapter = adapter
            self.con = con
            if id is Ice._struct_marker:
                self.id = _M_Ice.Identity()
            else:
                self.id = id
            self.facet = facet
            self.operation = operation
            self.mode = mode
            self.ctx = ctx
            self.requestId = requestId
            if encoding is Ice._struct_marker:
                self.encoding = _M_Ice.EncodingVersion()
            else:
                self.encoding = encoding

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_Ice.Current):
                return NotImplemented
            else:
                if self.adapter != other.adapter:
                    return False
                if self.con != other.con:
                    return False
                if self.id != other.id:
                    return False
                if self.facet != other.facet:
                    return False
                if self.operation != other.operation:
                    return False
                if self.mode != other.mode:
                    return False
                if self.ctx != other.ctx:
                    return False
                if self.requestId != other.requestId:
                    return False
                if self.encoding != other.encoding:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_Ice._t_Current)

        __repr__ = __str__

    _M_Ice._t_Current = IcePy.defineStruct('::Ice::Current', Current, (), (
        ('adapter', (), _M_Ice._t_ObjectAdapter),
        ('con', (), _M_Ice._t_Connection),
        ('id', (), _M_Ice._t_Identity),
        ('facet', (), IcePy._t_string),
        ('operation', (), IcePy._t_string),
        ('mode', (), _M_Ice._t_OperationMode),
        ('ctx', (), _M_Ice._t_Context),
        ('requestId', (), IcePy._t_int),
        ('encoding', (), _M_Ice._t_EncodingVersion)
    ))

    _M_Ice.Current = Current
    del Current

# End of module Ice
