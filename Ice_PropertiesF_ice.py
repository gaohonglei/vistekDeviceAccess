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
# Generated from file `PropertiesF.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy

# Start of module Ice
_M_Ice = Ice.openModule('Ice')
__name__ = 'Ice'

if 'Properties' not in _M_Ice.__dict__:
    _M_Ice._t_Properties = IcePy.declareClass('::Ice::Properties')

if 'PropertiesAdmin' not in _M_Ice.__dict__:
    _M_Ice._t_PropertiesAdmin = IcePy.declareClass('::Ice::PropertiesAdmin')
    _M_Ice._t_PropertiesAdminPrx = IcePy.declareProxy('::Ice::PropertiesAdmin')

# End of module Ice
