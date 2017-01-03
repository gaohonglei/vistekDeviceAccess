#pragma once
#include <Ice/Identity.ice>
#include <Ice/Instrumentation.ice>
#include "DBEntity.ice"
#include "ServiceCommon.ice"
module Vistek
{
	module Data
	{
		exception DataError
		{
			int errorCode;
			string errorMessage;
		};
		
		enum SubscribeTypes 
		{ 
			STNone = 0, 
			STDevice = 1, 
			STStorage = 2, 
			STService = 4
		};
		interface DataProviderRelayMessage
		{
			void MessageReceived(ServiceMessage msg);
			ServiceMessage DuplexMessageReceived(ServiceMessage msg);
		};
		interface DataProviderDmDeviceNotify
		{
			void DmDeviceChangedNotify(DmDevice device, DataChangeTypes changetype);
		};
		interface DataProviderDmStorageNotify
		{
			void DmStorageChangedNotify(DmStorage storage, DataChangeTypes changetype);
		};
		interface DataProviderDmServiceNotify
		{
			void DmServiceChangedNotify(DmService service, DataChangeTypes changetype);
		};
		interface DataProviderAsRuleNotify
		{
			void AsRuleChangedNotify(AsRule rule, DataChangeTypes changetype);
		};
		
		interface DataProviderDeviceStatusNotify
		{
			void DeviceStatusNotify(DeviceStatusInfo status);
		};
		
		interface DataProviderCallback extends Vistek::Core::BaseCallback
		{
			void DmDeviceChangedNotify(DmDevice device, DataChangeTypes changetype);
			void DmDeviceVideoChannelChangedNotify(DmDeviceVideoChannel channel, DataChangeTypes changetype);
			void DmStorageChangedNotify(DmStorage storage, DataChangeTypes changetype);
			void DmServiceChangedNotify(DmService service, DataChangeTypes changetype);
			void DmGroupChangedNotify(DmGroup group, DataChangeTypes changetype);
			void DmGroupChangedListNotify(DmGroupList groupList, DataChangeTypes changetype);
			void AsRuleChangedNotify(AsRule rule, DataChangeTypes changetype);
			void DeviceStatusNotify(DeviceStatusInfo status);
			void DeviceStatusListNotify(DeviceStatusInfoList status);
			void MessageReceived(ServiceMessage msg);
			ServiceMessage DuplexMessageReceived(ServiceMessage msg);
		};
		
		interface DataProviderServer extends Vistek::Core::BaseService
		{
			DmPlatformList GetAllPlatforms();
			DmDeviceList GetAllDevices();
			DmStorageList GetAllStorages();
			DmStorageList GetStoragesByServiceID(string sid);
			DmServiceList GetAllServices();
			DmServiceList GetServicesByServerID(string sid);
			DeviceStatusInfoList GetAllDeviceStatus();
			
			DmGroupList GetAllGroups();
			DmGroupList GetLeafGroups();
			DmDevice2GroupList GetAllDeviceGroupMapping();

			DmDeviceList GetAllDevicesWithRuleList();
			AsRuleList GetRuleList();
			AsRuleList GetRuleListByServiceID(string serviceID);
			AsRule GetRuleByID(string rid);

			AsEventSourceList GetAllEventSource();
			long KeepAlive(long ticks);
			int UpdateRule(AsRule rule);
			int DeleteRule(AsRule rule);
			
			int UpdateRoleService(DmService svc);
			int DeleteRoleService(DmService svc);
			
			bool UpdateDevice(DmDevice dev);
			bool UpdateDeviceList(DmDeviceList devList);
			

			void PushEvent(AsEvent evt, DataChangeTypes dct);
			void PushRGB24Image(AsEvent evt, int w, int h, Binary imageData);
			void PushPngImage(string rid, string eid, Binary imageData);
			
			void UploadTrafficCheckPointResult(Vistek::Data::TrafficCheckPointResult result) throws DataError;
			void UploadTrafficCheckPointResultOneway(Vistek::Data::TrafficCheckPointResult result);
			void ReportDeviceStatus(DeviceStatusInfo statusInfo);
			void ReportDeviceStatusList(DeviceStatusInfoList statusList);
		};
		interface DataProviderServerV0 extends DataProviderServer
		{
			void SubscribeChangesDmDevice(Ice::Identity ident);
			void SubscribeChangesDmStorage(Ice::Identity ident);
			void SubscribeChangesDmServices(Ice::Identity ident);
			void SubscribeChangesAsRules(Ice::Identity ident);
			//void SubscribeDeviceStatus(Ice::Identity ident);
			void SubscribeMessage(Ice::Identity ident);
		};

		interface DataProviderServerV1 extends DataProviderServer
		{
			void SubscribeCallbacks(Ice::Identity ident, Ice::StringSeq subList);
		};
	};
};