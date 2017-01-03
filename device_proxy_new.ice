#pragma once
#include "DBEntity.ice"

module Vistek
{
	module Device
	{
		enum RegisterType
		{
			rtNormal = 0,
			rtCheck = 1
		};

		["clr:property"]
		class DeviceStreamInfo
		{
			string deviceID;
			string uri;
			int channel = 0;
			int stream = 0;
		};
		sequence<DeviceStreamInfo> DeviceStreamInfoList;

		["clr:property"]
		class DeviceChannelInfo
		{
			string deviceID;
			string username;
			string password;
			DeviceStreamInfoList streamList;
			int channel = 0;
			bool thirdparty = false;
		};
		sequence<DeviceChannelInfo> DeviceChannelInfoList;

		interface DeviceCallback
		{
			void DeviceChangedNotify(Vistek::Data::DmDevice device, Vistek::Data::DataChangeTypes changetype);
			void DeviceVideoChannelChangedNotify(Vistek::Data::DmDeviceVideoChannel channel, Vistek::Data::DataChangeTypes changetype);
			void MessageReceived(Vistek::Data::ServiceMessage msg);
			Vistek::Data::ServiceMessage DuplexMessageReceived(Vistek::Data::ServiceMessage msg);
		};
		interface DeviceDispatchSession
		{
			string GetID();
			void KeepAlive();
			void Destroy();
			Vistek::Data::DmDeviceList GetDeviceList();
			int UpdateDeviceList(Vistek::Data::DmDeviceList list);
			int PushDeviceStatus(Vistek::Data::DeviceStatusInfo info);
			int PushDeviceStatusList(Vistek::Data::DeviceStatusInfoList list);
		};
		interface DeviceDispatchService
		{
			DeviceDispatchSession* Register(string id, RegisterType rt);
			DeviceDispatchSession* register2(string id, string manuc);
			int Unregister(string id);
			int PushDeviceStreamInfos(DeviceChannelInfoList infoMap);
			int PushDeviceStreamInfo(DeviceChannelInfo info);
		};
		interface DeviceDispatchServiceV1 extends DeviceDispatchService
		{
			void SubscribeCallback(Ice::Identity ident);
		};
	};
};

module Vistek
{

	module Media
	{
		enum ServiceType
		{
			stRtsp = 1,
			stRtmp = 2,
			stOther = 4
		};
		
		dictionary<string, int> ProtocolPortMap;	
		dictionary<string, string> UriMap;
		
		interface MediaCallback
		{
			void MediaChangeNotify(string did, int type);
		};
		interface MediaDispatchSession
		{
			string GetID();
			void KeepAlive();
			void Destroy();

			/////key -> deviceID + ":" + channelID + ":" + streamID(default:0) , value -> uri
			UriMap GetAllDeviceUri();
		};
		interface MediaDispatchService
		{
			MediaDispatchSession* Login(string id, int st, string host, ProtocolPortMap ports);
			int Logout(string id);
		};
		interface MediaDispatchServiceV1 extends MediaDispatchService
		{
			void SubscribeCallback(Ice::Identity ident);
		};

		interface MediaLocateService
		{
			string GetMediaServiceUriV0(string key, ServiceType st);
			string GetMediaServiceUriV1(string did, int cid, int sid, ServiceType st);
			UriMap GetAllMediaServiceUri();
		};
		interface MediaLocateServiceFactory
		{
		    MediaLocateService* Login(string username, string password);
		};
	};
};