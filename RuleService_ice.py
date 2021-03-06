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
# Generated from file `RuleService.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy
import Ice_Identity_ice
import Ice_Instrumentation_ice
import DBEntity_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Ice.Instrumentation
_M_Ice.Instrumentation = Ice.openModule('Ice.Instrumentation')

# Included module Vistek
_M_Vistek = Ice.openModule('Vistek')

# Included module Vistek.Data
_M_Vistek.Data = Ice.openModule('Vistek.Data')

# Start of module Vistek
__name__ = 'Vistek'

# Start of module Vistek.Data
__name__ = 'Vistek.Data'

if '_t_tagList' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data._t_tagList = IcePy.defineSequence('::Vistek::Data::tagList', (), IcePy._t_string)

if 'BootstrapViewNode' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data._t_BootstrapViewNode = IcePy.declareClass('::Vistek::Data::BootstrapViewNode')
    _M_Vistek.Data._t_BootstrapViewNodePrx = IcePy.declareProxy('::Vistek::Data::BootstrapViewNode')

if '_t_nodesList' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data._t_nodesList = IcePy.defineSequence('::Vistek::Data::nodesList', (), _M_Vistek.Data._t_BootstrapViewNode)

if 'BootstrapViewNode' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data.BootstrapViewNode = Ice.createTempClass()
    class BootstrapViewNode(Ice.Object):
        def __init__(self, text='', href='', tags=None, nodes=None):
            self.text = text
            self.href = href
            self.tags = tags
            self.nodes = nodes

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Vistek::Data::BootstrapViewNode')

        def ice_id(self, current=None):
            return '::Vistek::Data::BootstrapViewNode'

        def ice_staticId():
            return '::Vistek::Data::BootstrapViewNode'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_Vistek.Data._t_BootstrapViewNode)

        __repr__ = __str__

    _M_Vistek.Data.BootstrapViewNodePrx = Ice.createTempClass()
    class BootstrapViewNodePrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Vistek.Data.BootstrapViewNodePrx.ice_checkedCast(proxy, '::Vistek::Data::BootstrapViewNode', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Vistek.Data.BootstrapViewNodePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::Vistek::Data::BootstrapViewNode'
        ice_staticId = staticmethod(ice_staticId)

    _M_Vistek.Data._t_BootstrapViewNodePrx = IcePy.defineProxy('::Vistek::Data::BootstrapViewNode', BootstrapViewNodePrx)

    _M_Vistek.Data._t_BootstrapViewNode = IcePy.defineClass('::Vistek::Data::BootstrapViewNode', BootstrapViewNode, -1, (), False, False, None, (), (
        ('text', (), IcePy._t_string, False, 0),
        ('href', (), IcePy._t_string, False, 0),
        ('tags', (), _M_Vistek.Data._t_tagList, False, 0),
        ('nodes', (), _M_Vistek.Data._t_nodesList, False, 0)
    ))
    BootstrapViewNode._ice_type = _M_Vistek.Data._t_BootstrapViewNode

    _M_Vistek.Data.BootstrapViewNode = BootstrapViewNode
    del BootstrapViewNode

    _M_Vistek.Data.BootstrapViewNodePrx = BootstrapViewNodePrx
    del BootstrapViewNodePrx

if 'BootstrapViewRoot' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data.BootstrapViewRoot = Ice.createTempClass()
    class BootstrapViewRoot(Ice.Object):
        def __init__(self, text='', tags=None, nodes=None):
            self.text = text
            self.tags = tags
            self.nodes = nodes

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Vistek::Data::BootstrapViewRoot')

        def ice_id(self, current=None):
            return '::Vistek::Data::BootstrapViewRoot'

        def ice_staticId():
            return '::Vistek::Data::BootstrapViewRoot'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_Vistek.Data._t_BootstrapViewRoot)

        __repr__ = __str__

    _M_Vistek.Data.BootstrapViewRootPrx = Ice.createTempClass()
    class BootstrapViewRootPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Vistek.Data.BootstrapViewRootPrx.ice_checkedCast(proxy, '::Vistek::Data::BootstrapViewRoot', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Vistek.Data.BootstrapViewRootPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::Vistek::Data::BootstrapViewRoot'
        ice_staticId = staticmethod(ice_staticId)

    _M_Vistek.Data._t_BootstrapViewRootPrx = IcePy.defineProxy('::Vistek::Data::BootstrapViewRoot', BootstrapViewRootPrx)

    _M_Vistek.Data._t_BootstrapViewRoot = IcePy.declareClass('::Vistek::Data::BootstrapViewRoot')

    _M_Vistek.Data._t_BootstrapViewRoot = IcePy.defineClass('::Vistek::Data::BootstrapViewRoot', BootstrapViewRoot, -1, (), False, False, None, (), (
        ('text', (), IcePy._t_string, False, 0),
        ('tags', (), _M_Vistek.Data._t_tagList, False, 0),
        ('nodes', (), _M_Vistek.Data._t_nodesList, False, 0)
    ))
    BootstrapViewRoot._ice_type = _M_Vistek.Data._t_BootstrapViewRoot

    _M_Vistek.Data.BootstrapViewRoot = BootstrapViewRoot
    del BootstrapViewRoot

    _M_Vistek.Data.BootstrapViewRootPrx = BootstrapViewRootPrx
    del BootstrapViewRootPrx

if '_t_viewRoot' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data._t_viewRoot = IcePy.defineSequence('::Vistek::Data::viewRoot', (), _M_Vistek.Data._t_BootstrapViewRoot)

if '_t_dic' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data._t_dic = IcePy.defineDictionary('::Vistek::Data::dic', (), IcePy._t_string, IcePy._t_string)

if '_t_eventSourceList' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data._t_eventSourceList = IcePy.defineSequence('::Vistek::Data::eventSourceList', (), _M_Vistek.Data._t_dic)

if '_t_serviceList' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data._t_serviceList = IcePy.defineSequence('::Vistek::Data::serviceList', (), _M_Vistek.Data._t_dic)

if '_t_serviceAndEvent' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data._t_serviceAndEvent = IcePy.defineDictionary('::Vistek::Data::serviceAndEvent', (), IcePy._t_string, _M_Vistek.Data._t_serviceList)

if 'AsRuleEx' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data.AsRuleEx = Ice.createTempClass()
    class AsRuleEx(Ice.Object):
        def __init__(self, baseRule=None, deivceName='', deviceIP='', EventSourceName='', serviceName='', serviceIP='', SourceList=None, ServList=None):
            self.baseRule = baseRule
            self.deivceName = deivceName
            self.deviceIP = deviceIP
            self.EventSourceName = EventSourceName
            self.serviceName = serviceName
            self.serviceIP = serviceIP
            self.SourceList = SourceList
            self.ServList = ServList

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Vistek::Data::AsRuleEx')

        def ice_id(self, current=None):
            return '::Vistek::Data::AsRuleEx'

        def ice_staticId():
            return '::Vistek::Data::AsRuleEx'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_Vistek.Data._t_AsRuleEx)

        __repr__ = __str__

    _M_Vistek.Data.AsRuleExPrx = Ice.createTempClass()
    class AsRuleExPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Vistek.Data.AsRuleExPrx.ice_checkedCast(proxy, '::Vistek::Data::AsRuleEx', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Vistek.Data.AsRuleExPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::Vistek::Data::AsRuleEx'
        ice_staticId = staticmethod(ice_staticId)

    _M_Vistek.Data._t_AsRuleExPrx = IcePy.defineProxy('::Vistek::Data::AsRuleEx', AsRuleExPrx)

    _M_Vistek.Data._t_AsRuleEx = IcePy.declareClass('::Vistek::Data::AsRuleEx')

    _M_Vistek.Data._t_AsRuleEx = IcePy.defineClass('::Vistek::Data::AsRuleEx', AsRuleEx, -1, (), False, False, None, (), (
        ('baseRule', (), _M_Vistek.Data._t_AsRule, False, 0),
        ('deivceName', (), IcePy._t_string, False, 0),
        ('deviceIP', (), IcePy._t_string, False, 0),
        ('EventSourceName', (), IcePy._t_string, False, 0),
        ('serviceName', (), IcePy._t_string, False, 0),
        ('serviceIP', (), IcePy._t_string, False, 0),
        ('SourceList', (), _M_Vistek.Data._t_eventSourceList, False, 0),
        ('ServList', (), _M_Vistek.Data._t_serviceList, False, 0)
    ))
    AsRuleEx._ice_type = _M_Vistek.Data._t_AsRuleEx

    _M_Vistek.Data.AsRuleEx = AsRuleEx
    del AsRuleEx

    _M_Vistek.Data.AsRuleExPrx = AsRuleExPrx
    del AsRuleExPrx

if '_t_ruleList' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data._t_ruleList = IcePy.defineSequence('::Vistek::Data::ruleList', (), _M_Vistek.Data._t_AsRuleEx)

if '_t_ruleIdList' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data._t_ruleIdList = IcePy.defineSequence('::Vistek::Data::ruleIdList', (), IcePy._t_string)

if 'ruleEdit' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data.ruleEdit = Ice.createTempClass()
    class ruleEdit(Ice.Object):
        def __init__(self, Name='', EventLevel=0, IsAvtive=False, ServiceID='', StreamIndex=0, AnalysisService=''):
            self.Name = Name
            self.EventLevel = EventLevel
            self.IsAvtive = IsAvtive
            self.ServiceID = ServiceID
            self.StreamIndex = StreamIndex
            self.AnalysisService = AnalysisService

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Vistek::Data::ruleEdit')

        def ice_id(self, current=None):
            return '::Vistek::Data::ruleEdit'

        def ice_staticId():
            return '::Vistek::Data::ruleEdit'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_Vistek.Data._t_ruleEdit)

        __repr__ = __str__

    _M_Vistek.Data.ruleEditPrx = Ice.createTempClass()
    class ruleEditPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Vistek.Data.ruleEditPrx.ice_checkedCast(proxy, '::Vistek::Data::ruleEdit', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Vistek.Data.ruleEditPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::Vistek::Data::ruleEdit'
        ice_staticId = staticmethod(ice_staticId)

    _M_Vistek.Data._t_ruleEditPrx = IcePy.defineProxy('::Vistek::Data::ruleEdit', ruleEditPrx)

    _M_Vistek.Data._t_ruleEdit = IcePy.defineClass('::Vistek::Data::ruleEdit', ruleEdit, -1, (), False, False, None, (), (
        ('Name', (), IcePy._t_string, False, 0),
        ('EventLevel', (), IcePy._t_int, False, 0),
        ('IsAvtive', (), IcePy._t_bool, False, 0),
        ('ServiceID', (), IcePy._t_string, False, 0),
        ('StreamIndex', (), IcePy._t_int, False, 0),
        ('AnalysisService', (), IcePy._t_string, False, 0)
    ))
    ruleEdit._ice_type = _M_Vistek.Data._t_ruleEdit

    _M_Vistek.Data.ruleEdit = ruleEdit
    del ruleEdit

    _M_Vistek.Data.ruleEditPrx = ruleEditPrx
    del ruleEditPrx

if 'RuleService' not in _M_Vistek.Data.__dict__:
    _M_Vistek.Data.RuleService = Ice.createTempClass()
    class RuleService(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_Vistek.Data.RuleService:
                raise RuntimeError('Vistek.Data.RuleService is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Vistek::Data::RuleService')

        def ice_id(self, current=None):
            return '::Vistek::Data::RuleService'

        def ice_staticId():
            return '::Vistek::Data::RuleService'
        ice_staticId = staticmethod(ice_staticId)

        def GetRuleList(self, current=None):
            pass

        def GetRuleListByServiceID(self, serviceID, current=None):
            pass

        def GetRuleByIdList(self, list, current=None):
            pass

        def GetRuleByID(self, ID, current=None):
            pass

        def UpdateRule(self, rule, current=None):
            pass

        def DeleteRule(self, ruleID, current=None):
            pass

        def getServiceAndEventSource(self, current=None):
            pass

        def GetAllDevicesWithRuleList(self, current=None):
            pass

        def GetAllDevices(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Vistek.Data._t_RuleService)

        __repr__ = __str__

    _M_Vistek.Data.RuleServicePrx = Ice.createTempClass()
    class RuleServicePrx(Ice.ObjectPrx):

        def GetRuleList(self, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetRuleList.invoke(self, ((), _ctx))

        def begin_GetRuleList(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetRuleList.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_GetRuleList(self, _r):
            return _M_Vistek.Data.RuleService._op_GetRuleList.end(self, _r)

        def GetRuleListByServiceID(self, serviceID, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetRuleListByServiceID.invoke(self, ((serviceID, ), _ctx))

        def begin_GetRuleListByServiceID(self, serviceID, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetRuleListByServiceID.begin(self, ((serviceID, ), _response, _ex, _sent, _ctx))

        def end_GetRuleListByServiceID(self, _r):
            return _M_Vistek.Data.RuleService._op_GetRuleListByServiceID.end(self, _r)

        def GetRuleByIdList(self, list, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetRuleByIdList.invoke(self, ((list, ), _ctx))

        def begin_GetRuleByIdList(self, list, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetRuleByIdList.begin(self, ((list, ), _response, _ex, _sent, _ctx))

        def end_GetRuleByIdList(self, _r):
            return _M_Vistek.Data.RuleService._op_GetRuleByIdList.end(self, _r)

        def GetRuleByID(self, ID, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetRuleByID.invoke(self, ((ID, ), _ctx))

        def begin_GetRuleByID(self, ID, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetRuleByID.begin(self, ((ID, ), _response, _ex, _sent, _ctx))

        def end_GetRuleByID(self, _r):
            return _M_Vistek.Data.RuleService._op_GetRuleByID.end(self, _r)

        def UpdateRule(self, rule, _ctx=None):
            return _M_Vistek.Data.RuleService._op_UpdateRule.invoke(self, ((rule, ), _ctx))

        def begin_UpdateRule(self, rule, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Vistek.Data.RuleService._op_UpdateRule.begin(self, ((rule, ), _response, _ex, _sent, _ctx))

        def end_UpdateRule(self, _r):
            return _M_Vistek.Data.RuleService._op_UpdateRule.end(self, _r)

        def DeleteRule(self, ruleID, _ctx=None):
            return _M_Vistek.Data.RuleService._op_DeleteRule.invoke(self, ((ruleID, ), _ctx))

        def begin_DeleteRule(self, ruleID, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Vistek.Data.RuleService._op_DeleteRule.begin(self, ((ruleID, ), _response, _ex, _sent, _ctx))

        def end_DeleteRule(self, _r):
            return _M_Vistek.Data.RuleService._op_DeleteRule.end(self, _r)

        def getServiceAndEventSource(self, _ctx=None):
            return _M_Vistek.Data.RuleService._op_getServiceAndEventSource.invoke(self, ((), _ctx))

        def begin_getServiceAndEventSource(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Vistek.Data.RuleService._op_getServiceAndEventSource.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getServiceAndEventSource(self, _r):
            return _M_Vistek.Data.RuleService._op_getServiceAndEventSource.end(self, _r)

        def GetAllDevicesWithRuleList(self, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetAllDevicesWithRuleList.invoke(self, ((), _ctx))

        def begin_GetAllDevicesWithRuleList(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetAllDevicesWithRuleList.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_GetAllDevicesWithRuleList(self, _r):
            return _M_Vistek.Data.RuleService._op_GetAllDevicesWithRuleList.end(self, _r)

        def GetAllDevices(self, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetAllDevices.invoke(self, ((), _ctx))

        def begin_GetAllDevices(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Vistek.Data.RuleService._op_GetAllDevices.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_GetAllDevices(self, _r):
            return _M_Vistek.Data.RuleService._op_GetAllDevices.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Vistek.Data.RuleServicePrx.ice_checkedCast(proxy, '::Vistek::Data::RuleService', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Vistek.Data.RuleServicePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::Vistek::Data::RuleService'
        ice_staticId = staticmethod(ice_staticId)

    _M_Vistek.Data._t_RuleServicePrx = IcePy.defineProxy('::Vistek::Data::RuleService', RuleServicePrx)

    _M_Vistek.Data._t_RuleService = IcePy.defineClass('::Vistek::Data::RuleService', RuleService, -1, (), True, False, None, (), ())
    RuleService._ice_type = _M_Vistek.Data._t_RuleService

    RuleService._op_GetRuleList = IcePy.Operation('GetRuleList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Vistek.Data._t_AsRuleList, False, 0), ())
    RuleService._op_GetRuleListByServiceID = IcePy.Operation('GetRuleListByServiceID', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Vistek.Data._t_AsRuleList, False, 0), ())
    RuleService._op_GetRuleByIdList = IcePy.Operation('GetRuleByIdList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Vistek.Data._t_ruleIdList, False, 0),), (), ((), _M_Vistek.Data._t_ruleList, False, 0), ())
    RuleService._op_GetRuleByID = IcePy.Operation('GetRuleByID', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Vistek.Data._t_AsRuleEx, False, 0), ())
    RuleService._op_UpdateRule = IcePy.Operation('UpdateRule', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Vistek.Data._t_AsRule, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    RuleService._op_DeleteRule = IcePy.Operation('DeleteRule', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    RuleService._op_getServiceAndEventSource = IcePy.Operation('getServiceAndEventSource', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Vistek.Data._t_serviceAndEvent, False, 0), ())
    RuleService._op_GetAllDevicesWithRuleList = IcePy.Operation('GetAllDevicesWithRuleList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Vistek.Data._t_DmDeviceList, False, 0), ())
    RuleService._op_GetAllDevices = IcePy.Operation('GetAllDevices', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Vistek.Data._t_viewRoot, False, 0), ())

    _M_Vistek.Data.RuleService = RuleService
    del RuleService

    _M_Vistek.Data.RuleServicePrx = RuleServicePrx
    del RuleServicePrx

# End of module Vistek.Data

__name__ = 'Vistek'

# End of module Vistek
