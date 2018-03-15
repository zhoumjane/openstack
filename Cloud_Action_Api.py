#!/usr/bin/python  
# -*- coding: UTF-8 -*-
import os
import sys
import requests
#from termcolor import *

# The Public Params
REGION_ID = 'SZ_HQYG01'
AK = 'bb1e603fb70b46d28eef143bd32c4f41'
SECRET = 'aadcbf12c8d842218daa4bec528b42e3'
isp_line = 'isp_bgp'
JSON = 'json'
GET = 'GET'
PERIOD = '1'
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from aliyunsdkcore.auth import rpc_signature_composer as rpc_signer

text = """

列出所有eip
python Cloud_Action_Api.py DescribeEipAddresses
示例：python Cloud_Action_Api.py DescribeEipAddresses | python -mjson.tool

# AllocateEipAddress 申请EIP地址
python Cloud_Action_Api.py AllocateEipAddress 带宽值
python Cloud_Action_Api.py AllocateEipAddress 1000

# 修改eip带宽
python Cloud_Action_Api.py ModifyEipAddressAttribute 带宽值 eip地址的id号
示例：python Cloud_Action_Api.py ModifyEipAddressAttribute 150 eipalloc-bd288ee0

# AssociateEipAddress 绑定EIP地址到云主机
python Cloud_Action_Api.py AssociateEipAddress eip地址的id号 云主机的id号
示例： python Cloud_Action_Api.py AssociateEipAddress eipalloc-bd12288ee0 8ff87e0f-7dcc-4895-a012f9-427e4807b745

# UnassociateEipAddress 将EIP地址从云主机上解绑
python Cloud_Action_Api.py UnassociateEipAddress eip地址的id号 云主机的id号
示例：python Cloud_Action_Api.py UnassociateEipAddress eipalloc-bd12288ee0 8ff87e0f-7dcc-4895-a0f912-427e4807b745

# ReleaseEipAddress 释放EIP地址
python Cloud_Action_Api.py ReleaseEipAddress eip地址的id号
示例：python Cloud_Action_Api.py ReleaseEipAddress eipalloc-bd12288ee0

# CreateInstance 创建云主机
python Cloud_Action_Api.py CreateInstance ImageId（镜像id） InstanceType（配置） InstanceName（云主机名称） Password（密码） VSwitchId（子网id）
示例：python Cloud_Action_Api.py CreateInstance 4af481cf-fd7122-407f-86b8-e9147a8ca452 ram_type_1_1G_50G test-zhoumingjian zmj9301282126ZHOU$ ac8e1141-01249f-4307-9f99-511b8b457780

#修改云主机密码
python Cloud_Action_Api.py ModifyInstanceAttribute 云主机id号  云主机密码
示例：python Cloud_Action_Api.py ModifyInstanceAttribute fef04d7c-fa71-4b1282-9f2c-501236cbda91 WS12jumabp

#删除云主机
python Cloud_Action_Api.py DeleteInstance 云主机id号
示例：python Cloud_Action_Api.py DeleteInstance 8ff87e0f-712dcc-4895-a0f9-427e4807b745

#停止云主机
python Cloud_Action_Api.py StopInstance 云主机id号
示例：python Cloud_Action_Api.py StopInstance fef04d7c-f12a71-4b82-9f2c-501236cbda91

#开启云主机
python  Cloud_Action_Api.py StartInstance 云主机id号
示例：python Cloud_Action_Api.py StartInstance fef04d7c-fa71-124b82-9f2c-501236cbda91

#重启云主机
python Cloud_Action_Api.py RebootInstance 云主机id号
示例：python Cloud_Action_Api.py RebootInstance 79dda5b6-2c1236-46d3-981d-ddc4eecc7cfd

#列出某一台云主机的详情
python Cloud_Action_Api.py DescribeInstances 云主机内网ip，类似如下格式  |  python -mjson.tool(转换为json格式) 
示例：python Cloud_Action_Api.py DescribeInstances '["10.61.100.34"]'  | python -mjson.tool 

#列出该项目部所有云主机
python Cloud_Action_Api.py DescribeInstances_All | python -mjson.tool(转换为json格式)
示例：python Cloud_Action_Api.py DescribeInstances_All | python -mjson.tool

"""



# AllocateEipAddress  申请EIP地址
class AllocateEipAddress:
                def __init__(self, Bandwidth):
                        self.Bandwidth = Bandwidth
                def get_sign_params(self):
                        req_params = {}
                        req_params['Version'] = '2016-04-28'
                        req_params['Action'] = 'AllocateEipAddress'
                        req_params['Format'] = JSON
                        req_params['RegionId'] = REGION_ID
                        req_params['Bandwidth'] = self.Bandwidth
                        req_params['isp_line'] = isp_line
                        return req_params 

                def get_url_sign(self):
                        sign_params = self.get_sign_params()
                        url = rpc_signer.get_signed_url(
                                sign_params,
                                AK,
                                SECRET,
                                JSON,
                                GET)
                        http_url = "http://10.60.32.3:9698" + url
                        r = requests.get(http_url)
                        print r.text
                        return http_url



# ModifyEipAddressAttribute  修改EIP地址带宽值
class ModifyEipAddressAttribute:
                def __init__(self, Bandwidth, AllocationId):
                        self.Bandwidth = Bandwidth
			self.AllocationId = AllocationId
                def get_sign_params(self):
                        req_params = {}
                        req_params['Version'] = '2016-04-28'
                        req_params['Action'] = 'ModifyEipAddressAttribute'
                        req_params['Format'] = JSON
                        req_params['RegionId'] = REGION_ID
                        req_params['Bandwidth'] = self.Bandwidth
			req_params['AllocationId'] = self.AllocationId
                        req_params['isp_line'] = isp_line
                        return req_params 

                def get_url_sign(self):
                        sign_params = self.get_sign_params()
                        url = rpc_signer.get_signed_url(
                                sign_params,
                                AK,
                                SECRET,
                                JSON,
                                GET)
                        http_url = "http://10.60.32.3:9698" + url
                        r = requests.get(http_url)
                        print r.text
                        return http_url



# AssociateEipAddress  绑定EIP地址到云主机
class AssociateEipAddress:
                                def __init__(self, AllocationId, InstanceId):
                                        self.AllocationId = AllocationId
                                        self.InstanceId = InstanceId

                                def get_sign_params(self):
                                        req_params = {}
                                        req_params['Version'] = '2016-04-28'
                                        req_params['Action'] = 'AssociateEipAddress'
                                        req_params['Format'] = JSON
                                        req_params['RegionId'] = REGION_ID
                                        req_params['AllocationId'] = self.AllocationId
                                        req_params['InstanceId'] = self.InstanceId
                                        req_params['isp_line'] = isp_line
                                        return req_params

                                def get_url_sign(self):
                                        sign_params = self.get_sign_params()
                                        url = rpc_signer.get_signed_url(
                                        sign_params,
                                        AK,
                                        SECRET,
                                        JSON,
                                        GET)
                                        http_url = "http://10.60.32.3:9698" + url
                                        r = requests.get(http_url)
                                        print r.text
                                        return http_url



# UnassociateEipAddress 将EIP地址从云主机上解绑
class UnassociateEipAddress:
                                def __init__(self, AllocationId, InstanceId):
                                        self.AllocationId = AllocationId
                                        self.InstanceId = InstanceId

                                def get_sign_params(self):
                                        req_params = {}
                                        req_params['Version'] = '2016-04-28'
                                        req_params['Action'] = 'UnassociateEipAddress'
                                        req_params['Format'] = JSON
                                        req_params['RegionId'] = REGION_ID
                                        req_params['AllocationId'] = self.AllocationId
                                        req_params['InstanceId'] = self.InstanceId
                                        req_params['isp_line'] = isp_line
                                        return req_params

                                def get_url_sign(self):
                                        sign_params = self.get_sign_params()
                                        url = rpc_signer.get_signed_url(
                                        sign_params,
                                        AK,
                                        SECRET,
                                        JSON,
                                        GET)
                                        http_url = "http://10.60.32.3:9698" + url
                                        r = requests.get(http_url)
                                        print r.text
                                        return http_url



# ReleaseEipAddress 释放EIP地址
class ReleaseEipAddress:
				def __init__(self, AllocationId):
					self.AllocationId = AllocationId
						
				def get_sign_params(self):
					req_params = {}
					req_params['Version'] = '2016-04-28'
					req_params['Action'] = 'ReleaseEipAddress'
					req_params['Format'] = JSON
					req_params['RegionId'] = REGION_ID
					req_params['AllocationId'] = self.AllocationId
					req_params['isp_line'] = isp_line
					return req_params 
					
				def get_url_sign(self):
					sign_params = self.get_sign_params()
					url = rpc_signer.get_signed_url(
					sign_params,
					AK,
					SECRET,
					JSON,
					GET)
					http_url = "http://10.60.32.3:9698" + url
					r = requests.get(http_url)
					print r.text
					return http_url




# DescribeEipAddresses 列出EIP地址
class DescribeEipAddresses:
				def __init__(self):
					pass
				
				
				def get_sign_params(self):
					req_params = {}
					req_params['Version'] = '2016-04-28'
					req_params['Action'] = 'DescribeEipAddresses'
					req_params['Format'] = JSON
					req_params['RegionId'] = REGION_ID
					req_params['isp_line'] = isp_line
					return req_params
				def get_url_sign(self):
					sign_params = self.get_sign_params()
					url = rpc_signer.get_signed_url(
					sign_params,
					AK,
					SECRET,
					JSON,
					GET)
					http_url = "http://10.60.32.3:9698" + url
					r = requests.get(http_url)
					print  r.text 
					return http_url




# CreateInstance 创建云主机
class CreateInstance:
				def __init__(self, ImageId, InstanceType, InstanceName, Password, VSwitchId):
					self.ImageId = ImageId
					self.InstanceType = InstanceType
					self.InstanceName = InstanceName
					self.Password = Password
					self.VSwitchId = VSwitchId
					
				def get_sign_params(self):
					req_params = {}
					req_params['Version'] = '2016-04-28'
					req_params['Action'] = 'CreateInstance'
					req_params['Format'] = JSON
					req_params['RegionId'] = REGION_ID
					req_params['ImageId'] = self.ImageId
					req_params['InstanceType'] = self.InstanceType
					req_params['InstanceName'] = self.InstanceName
					req_params['Password'] = self.Password
					req_params['VSwitchId'] = self.VSwitchId
					req_params['Period'] = PERIOD
					return req_params
						
				def get_url_sign(self):
					sign_params = self.get_sign_params()
					url = rpc_signer.get_signed_url(
					sign_params,
					AK,
					SECRET,
					JSON,
					GET)
					http_url = "http://10.60.32.3:8788" + url
					r = requests.get(http_url)
					print r.text
					return http_url
				



# ModifyInstanceAttribute 修改云主机密码
class ModifyInstanceAttribute:
				def __init__(self, InstanceId, Password):
						self.InstanceId = InstanceId
						self.Password = Password
						
				def get_sign_params(self):
						req_params = {}
						req_params['Version'] = '2016-04-28'
						req_params['RegionId'] = REGION_ID
						req_params['InstanceId'] = self.InstanceId
						req_params['Action'] = 'ModifyInstanceAttribute'
						req_params['Format'] = JSON
					#	req_params['InstanceName'] = 'test_1'
						req_params['Password'] = self.Password
						return req_params 
						
				def get_url_sign(self):
						sign_params = self.get_sign_params()
						url = rpc_signer.get_signed_url(
						sign_params,
						AK,
						SECRET,
						JSON,
						GET)
						http_url = "http://10.60.32.3:8788" + url
						r = requests.get(http_url)
						print r.text
						return http_url
						


# DeleteInstance 删除云主机
class DeleteInstance:
				def __init__(self, InstanceId):
						self.InstanceId = InstanceId
				
				def get_sign_params(self):
						req_params = {}
						req_params['Version'] = '2016-04-28'
						req_params['Action'] = 'DeleteInstance'
						req_params['Format'] = JSON
						req_params['RegionId'] = REGION_ID
						req_params['InstanceId'] = self.InstanceId
						return req_params 
						
				def get_url_sign(self):
						sign_params = self.get_sign_params()
						url = rpc_signer.get_signed_url(
						sign_params,
						AK,
						SECRET,
						JSON,
						GET)
						http_url = "http://10.60.32.3:8788" + url
						r = requests.get(http_url)
						print r.text
						return http_url


# StopInstance 云主机关机
class StopInstance:
				def __init__(self, InstanceId):
						self.InstanceId = InstanceId
				
				def get_sign_params(self):
						req_params = {}
						req_params['Version'] = '2016-04-28'
						req_params['Action'] = 'StopInstance'
						req_params['Format'] = JSON
						req_params['RegionId'] = REGION_ID
						req_params['InstanceId'] = self.InstanceId
						return req_params 
						
				def get_url_sign(self):
						sign_params = self.get_sign_params()
						url = rpc_signer.get_signed_url(
						sign_params,
						AK,
						SECRET,
						JSON,
						GET)
						http_url = "http://10.60.32.3:8788" + url
						r = requests.get(http_url)
						print r.text
						return http_url



# StartInstance 云主机开机
class StartInstance:
				def __init__(self, InstanceId):
						self.InstanceId = InstanceId
				
				def get_sign_params(self):
						req_params = {}
						req_params['Version'] = '2016-04-28'
						req_params['Action'] = 'StartInstance'
						req_params['Format'] = JSON
						req_params['RegionId'] = REGION_ID
						req_params['InstanceId'] = self.InstanceId
						return req_params 
						
				def get_url_sign(self):
						sign_params = self.get_sign_params()
						url = rpc_signer.get_signed_url(
						sign_params,
						AK,
						SECRET,
						JSON,
						GET)
						http_url = "http://10.60.32.3:8788" + url
						r = requests.get(http_url)
						print r.text
						return http_url


# RebootInstance 重启云主机
class RebootInstance:
				def __init__(self, InstanceId):
						self.InstanceId = InstanceId
				
				def get_sign_params(self):
						req_params = {}
						req_params['Version'] = '2016-04-28'
						req_params['Action'] = 'RebootInstance'
						req_params['Format'] = JSON
						req_params['RegionId'] = REGION_ID
						req_params['InstanceId'] = self.InstanceId
						return req_params 
						
				def get_url_sign(self):
						sign_params = self.get_sign_params()
						url = rpc_signer.get_signed_url(
						sign_params,
						AK,
						SECRET,
						JSON,
						GET)
						http_url = "http://10.60.32.3:8788" + url
						r = requests.get(http_url)
						print r.text
						return http_url



# DescribeInstances 根据内网ip列出云主机详细信息
class DescribeInstances:
				def __init__(self, PrivateIpAddresses):
						self.PrivateIpAddresses = PrivateIpAddresses
				
				def get_sign_params(self):
						req_params = {}
						req_params['Version'] = '2016-04-28'
						req_params['RegionId'] = REGION_ID
						req_params['Action'] = 'DescribeInstances'
						req_params['Format'] = JSON
						req_params['PrivateIpAddresses'] = self.PrivateIpAddresses
						#req_params['InstanceIds'] = '["2f02792d-befb-4bca-87c6-7589224883c8","fef04d7c-fa71-4b82-9f2c-501236cbda91"]'
						return req_params 
					
				def get_url_sign(self):
						sign_params = self.get_sign_params()
						url = rpc_signer.get_signed_url(
						sign_params,
						AK,
						SECRET,
						JSON,
						GET)
						http_url = "http://10.60.32.3:8788" + url
						r = requests.get(http_url)
						print r.text
						return http_url

class DescribeInstances_All:
        def get_sign_params(self):
                         req_params = {}
                         req_params['Version'] = '2016-04-28'
                         req_params['RegionId'] = REGION_ID
                         req_params['Action'] = 'DescribeInstances'
                         req_params['Format'] = JSON
                         #req_params['PrivateIpAddresses'] = self.PrivateIpAddresses
                         #req_params['InstanceIds'] = '["2f02792d-befb-4bca-87c6-7589224883c8","fef04d7c-fa71-4b82-9f2c-501236cbda91"]'
                         return req_params

        def get_url_sign(self):
                         sign_params = self.get_sign_params()
                         url = rpc_signer.get_signed_url(
                         sign_params,
                         AK,
                         SECRET,
                         JSON,
                         GET)
                         http_url = "http://10.60.32.3:8788" + url
                         r = requests.get(http_url)
                         print r.text
                         return http_url

if len(sys.argv) < 2:
	print "\033[1;35m第一个参数请输入如下一个：\nAllocateEipAddress\nModifyEipAddressAttribute\nAssociateEipAddress\nUnassociateEipAddress\nReleaseEipAddress\nDescribeEipAddresses\nCreateInstance\nModifyInstanceAttribute\nDeleteInstance\nStopInstance\nStartInstance\nRebootInstance\nDescribeInstances\nDescribeInstances_All"

elif 'AllocateEipAddress' == sys.argv[1]: 
	AllocateEipAddress(sys.argv[2]).get_url_sign()

elif 'ModifyEipAddressAttribute' == sys.argv[1]:
	ModifyEipAddressAttribute(sys.argv[2], sys.argv[3]).get_url_sign()

elif 'AssociateEipAddress' == sys.argv[1]:
	AssociateEipAddress(sys.argv[2], sys.argv[3]).get_url_sign()

elif 'UnassociateEipAddress' == sys.argv[1]:
	UnassociateEipAddress(sys.argv[2], sys.argv[3]).get_url_sign()

elif 'ReleaseEipAddress' == sys.argv[1]:
	ReleaseEipAddress(sys.argv[2]).get_url_sign()

elif 'DescribeEipAddresses' == sys.argv[1]:
	DescribeEipAddresses().get_url_sign()

elif 'CreateInstance' == sys.argv[1]:
	CreateInstance(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]).get_url_sign()

elif 'ModifyInstanceAttribute' == sys.argv[1]:
	ModifyInstanceAttribute(sys.argv[2], sys.argv[3]).get_url_sign()

elif 'DeleteInstance' == sys.argv[1]:
	DeleteInstance(sys.argv[2]).get_url_sign()

elif 'StopInstance' == sys.argv[1]:
	StopInstance(sys.argv[2]).get_url_sign()	

elif 'StartInstance' == sys.argv[1]:
	StartInstance(sys.argv[2]).get_url_sign()

elif 'RebootInstance' == sys.argv[1]:
	RebootInstance(sys.argv[2]).get_url_sign()

elif 'DescribeInstances' == sys.argv[1]:
	DescribeInstances(sys.argv[2]).get_url_sign()

elif 'DescribeInstances_All' == sys.argv[1]:
	DescribeInstances_All().get_url_sign()

#elif  sys.argv[1] in ("*"):
#	print "第一个参数请输入如下一个：\n AllocateEipAddress\nModifyEipAddressAttribute\nAssociateEipAddress\nUnassociateEipAddress\nReleaseEipAddress\nDescribeEipAddresses\nCreateInstance\nModifyInstanceAttribute\nDeleteInstance\nStopInstance\nStartInstance\nRebootInstance\n"
	
else :
	print "具体操作如下：\033[0m" + "\033[1;35m %s \033[0m"  % text
