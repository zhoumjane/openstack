REGION_ID = 'SZ_HQYG01'
AK = 'bb1e603fb70b46d28eef143bd32c4f41'
SECRET = 'aadcbf12c8d842218daa4bec528b42e3'
JSON = 'json'
GET = 'GET'
SUBNETID = 'ac8e1141-049f-4307-9f99-511b8b457780'
BW = '1'
IMID = '4af481cf-fd72-407f-86b8-e9147a8ca452'
INSTYPE = 'ram_type_1_1G_50G'
PERIOD = '1'
import sys, os, requests

def get_version():
    return '2016-04-28'

def get_action_name():
    return 'DescribeInstances'
    #return 'AllocateEipAddress'
    #return 'CreateInstance'
    #return 'ReleaseEipAddress'

def get_accept_format():
    return 'json'

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from aliyunsdkcore.auth import rpc_signature_composer as rpc_signer

class DescribeInstances:
#	def __init__(self):
#			 self.DescribeInstances = get_action_name()
	def get_sign_params(self):
        	         req_params = {}
                         req_params['Version'] = get_version()
         	         req_params['RegionId'] = REGION_ID
                	 req_params['Action'] = get_action_name()
           	    	 req_params['Format'] = get_accept_format()
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

DescribeInstances().get_url_sign()
