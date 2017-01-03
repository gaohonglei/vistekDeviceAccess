#pragma once
#include <Ice/Identity.ice>
#include <Ice/Instrumentation.ice>
#include "DBEntity.ice"
module Vistek
{
	module Data
	{
		sequence<string> tagList;
		class BootstrapViewNode;
		sequence<BootstrapViewNode> nodesList;
		
		class BootstrapViewNode
		{
			string text;
			string href;
			tagList tags;
			nodesList nodes;
		};
		class BootstrapViewRoot
		{
			string text;
			tagList tags;
			nodesList nodes;
		};
		sequence<BootstrapViewRoot> viewRoot;
		dictionary<string,string> dic;
		sequence<dic> eventSourceList;
		sequence<dic> serviceList;
		dictionary<string,serviceList> serviceAndEvent;
		class AsRuleEx
		{
			AsRule baseRule;
			string deivceName;
			string deviceIP;
			string EventSourceName;
			string serviceName;
			string serviceIP;
			eventSourceList SourceList;
			serviceList ServList;
		};
		sequence<AsRuleEx> ruleList;
		sequence<string> ruleIdList;
		class ruleEdit
		{
			string Name;
			int EventLevel;
			bool IsAvtive;
			string ServiceID;
			int StreamIndex;
			string AnalysisService;
		};
		interface RuleService
		{
			AsRuleList GetRuleList();
			AsRuleList GetRuleListByServiceID(string serviceID);
			ruleList GetRuleByIdList(ruleIdList list);
			AsRuleEx GetRuleByID(string ID);
			int UpdateRule(AsRule rule);
			int DeleteRule(string ruleID);
			serviceAndEvent getServiceAndEventSource();
			DmDeviceList GetAllDevicesWithRuleList();
			viewRoot GetAllDevices();
		};
	};
};