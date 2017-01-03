#pragma once
#include <Ice/BuiltinSequences.ice>
#include <Ice/Identity.ice>
[["cpp:include:list"]]
module Vistek
{
	module Data
	{
		enum SVIOFormat
		{
			BIN = 0,
			XML = 1,
			JSON = 2,
			TEXT = 3
		};
		enum DeviceCategoryFlags
		{
			DeviceCategoryNone				= 0,		//Nothing
			DeviceCategoryIsSysDevice		= 0x01,		//是否是系统设备
			DeviceCategoryRemoteConfig		= 0x02,		//远程配置
			DeviceCategoryHasRealtimeStream	= 0x04,		//是否有流(仅音视频流)
			DeviceCategoryHasPlaybackStream	= 0x08,		//是否自带存储
			DeviceCategoryCanStorage		= 0x10,		//是否可以存储其他通道流
			DeviceCategoryHasAlarmIN		= 0x20,		//是否具有报警输入
			DeviceCategoryHasAlarmOUT		= 0x40,		//是否具有报警输出
			DeviceCategoryHasBayonet		= 0x80		//是否具有卡口输入
		};
		enum DataChangeTypes { NoneChanged, DataAdded, DataModified, DataRemoved };
		enum StorageModes { ByPrioirity, BySize };
		enum DeviceStatus
		{ 
			dstsOK = 0, 
			dstsOFFLINE = 1, 
			dstsERROR = 2
		};


		class DomainSite
		{
			string ID;
			string SiteCode;
			string SiteName;
			string ParentID;
		};
		class DmDevice;
		
		["clr:property"]
		class DmStorage
		{
			string ID;
			string ServiceID;
			string DeviceID;
			int Channel;
			int Stream;
			StorageModes StorageMode;
			long StorageParam;
			string Schedule;
			DmDevice Device;
		};
		
		sequence<DmStorage> DmStorageList;
		class DmDeviceCategory
		{
			string CategoryID;
			string CategoryCode;
			string CategoryName;
			int BasicFlag;
		};
		
		class DmGroup
		{
			string GroupID;
			string GroupName;
			string GroupParentID;
			long GroupIndex;
			long GroupParentIndex;
			string ExtensionID;
			string ParentExtensionID;
		};
		sequence<DmGroup> DmGroupList;
		class DmDevice2Group
		{
			string DeviceID;
			int DeviceChannelIndex;
			string GroupID;
			long GroupIndex;
		};
		sequence<DmDevice2Group> DmDevice2GroupList;

		["clr:property"]
		class DmDeviceVideoChannel
		{
			string DeviceID;
			int ChannelIndex;
			string SystemID;
			string Name;
			bool IsPTZEnabled;
			long DeviceIndex;
			long GroupIndex;
			string ExtensionID;
			double Latitude;
			double Longitude;
		};

		sequence<DmDeviceVideoChannel> DmDeviceVideoChannelList;

		class AsRule;

		sequence<AsRule> AsRuleList;
		
		["clr:property"]
		class DmPlatformManufacture
		{
			string Code;
			string Name;
			string DefaultUsername;
			string DefaultPassword;
			string Extension;
		};
		["clr:property"]
		class DmPlatformRedirection
		{
			string PlatformID;
			string Protocol;
			string Category;
			string CategoryName;
			string IP;
			int Port;
			string Username;
			string Password;
		};
		sequence<DmPlatformRedirection> DmPlatformRedirectionList;
		["clr:property"]
		class DmPlatform
		{
			string ID;
			string Code;
			string Name;
			string Version;
			string ManufactureCode;
			string IP;
			int IPVer;
			int Port;
			string Username;
			string Password;
			int Status;
			string SiteID;
			string Extension;
			string ChangedDtTm;
			string ProtocolHeader;
			DmPlatformManufacture Manufacture;
			optional(1) DmPlatformRedirectionList RedirectionList;
		};
		
		sequence<DmPlatform> DmPlatformList;
		
		["clr:property"]
		class DmDevice
		{
			string DeviceID;
			string DeviceName;
			string Manufacture;
			string Extension;
			string ParentID;
			string SiteID;
			string Code;
			string IP;
			int Port;
			string Username;
			string Password;
			int ProtocolFlag;
			string PlatformID;
			string ChangedDateTime;
			string ExtensionID;
			string SystemID;
			double Latitude;
			double Longitude;
			int Status;
			DmDeviceCategory DeviceCategory;
			DmStorageList StorageList;
			DmDeviceVideoChannelList ChannelList;
			AsRuleList RuleList;
			DmPlatform Platform;
			optional(1) string reserved = "";
		};

		sequence<DmDevice> DmDeviceList;
		
		["clr:property"]
		class DmServiceType
		{
			string ServiceTypeCode;
			string ServiceTypeName;
			string ConfigSchema;
		};
		
		["clr:property"]
		class DmService
		{
			string ServiceID;
			string ServerID;
			string ServiceTypeCode;
			string ServiceName;
			string ServiceIP;
			int ServicePort;
			string SiteID;
			string Config;
			string ChangedDateTime;
			long TimeStampTicks;
			DmDevice ServerInfo;
			DmServiceType ServiceType;
			DomainSite Site;

		};
		sequence<DmService> DmServiceList;
		enum DeviceChannelType { ctVIDEO = 0, ctALARM = 1, ctBAYONET = 2 };
        
		class AsEventSource;

		["clr:property"]
		class AsEventType
		{
			string ID;
			string Key;
			string Name;
			string Desc;
			string EventSourceType;
			AsEventSource EventSource;
		};
		sequence<AsEventType> AsEventTypeList;
		sequence<byte> Binary;
		
		["clr:property"]
		class AsEventSource
		{
			string ID;
			string Name;
			string Desc;
			string AssemblyName;
			string InputTypeName;
			int InputFormat;
			string OutputTypeName;
			int OutputFormat;
			DeviceChannelType AnalysisChannelType;
			int ComputingOverhead;
			AsEventTypeList EventTypeList;
		};
		sequence<AsEventSource> AsEventSourceList;
		
		["clr:property"]
		class AsRule
		{
			string ID;
			string Name;
			string DeviceID;
			int ChannelIndex;
			int StreamIndex;
			string ServiceID;
			int EventLevel;
			string EventSourceID;
			Binary ConfigData;
			string DrawingData;
			string Schedule;
			bool IsActive;
			string ChangedDateTime;
			DmService AnalysisService;
			AsEventSource EventSource;
		};
		class TrafficCheckPointResult
		{
			int ChannelIndex;
            long DateTime;
            int DetectType;
            string DeviceID;
            int Direction;
            int DriveChan;
            string ID;
            int IllegalType;
            bool IsAdjusted;
            string License;
            int LicenseBelieve;
            string LicenseCharBelieve;
            int LicenseLen;
            int PlateColor;
            int PlateType;
            int VehicleColor;
            int VehicleColorDepth;
            int VehicleSpeed;
            int VehicleType;
			float LicenseX;
			float LicenseY;
			float LicenseW;
			float LicenseH;
            Binary LicenseImageData;
            Binary OverallViewData;
		};
		
		["clr:property"]
		class AsEvent
		{
			string eventID;
			string ruleID;
			string startDT;
			string endDT;
			string eventTypeID;
			string siteID;
			string deviceID;
			int channelIndex;
			DeviceChannelType channelType;
			int eventLevel;
			string extention;
		};

		
		class ServiceMessage
		{
			string header;
			string body;
		};

		
		["clr:property"]
		struct DeviceStatusInfo
		{
			string DeviceID;
			long DeviceIndex;
			int ChannelIndex;
			int Status;
			int ErrorCode;
		};
		sequence<DeviceStatusInfo> DeviceStatusInfoList;

	};

};