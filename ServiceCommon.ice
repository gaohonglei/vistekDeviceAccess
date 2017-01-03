
// **********************************************************************
//
// Copyright (c) 2003-2013 Vistek. All rights reserved.
// Wirten by FJW on 2013/07/22
// *******
#pragma once

#include <Ice/Identity.ice>
#include "DBEntity.ice"
module Vistek
{
	module Core
	{		
		exception GenericError
		{
			int errorCode;
			string errorMessage;
		};
		exception ServiceException extends GenericError {};
		interface BaseCallback 
		{
			void CheckConnection(long ticks); 
		};
		interface BaseService
		{
			//string Login(string username, string password) throws ServiceException;
			//string AuthenticateByCenter(string globalToken) throws ServiceException;

			idempotent Vistek::Data::DmService GetServiceInfo(string token);
			string GetStatusInfo(string token) throws ServiceException;

			int SendServiceMessage(Vistek::Data::ServiceMessage msg);
			void PostServiceMessage(Vistek::Data::ServiceMessage msg);
			Vistek::Data::ServiceMessage SendServiceMessageDuplex(Vistek::Data::ServiceMessage msg);
		};

	};
};