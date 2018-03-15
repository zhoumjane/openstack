REGION_ID = 'SZ_HQYG01'
AK = 'bb1e603fb70b46d28eef143bd32c4f41'
SECRET = 'aadcbf12c8d842218daa4bec528b42e3'
JSON = 'json'
GET = 'GET'
IMID = '4af481cf-fd72-407f-86b8-e9147a8ca452'
PERIOD = '1'

def get_version():
    return '2016-04-28'

def get_action_name():
    #return 'DescribeInstances'
    #return 'AllocateEipAddress'
    return 'StopInstance'
    #return 'ReleaseEipAddress'

def get_accept_format():
    return 'json'

def get_sign_params():
    req_params = {}
    req_params['Version'] = get_version()
    req_params['Action'] = get_action_name()
    req_params['Format'] = get_accept_format()
    req_params['RegionId'] = REGION_ID
    req_params['Period'] = PERIOD
    req_params['InstanceId'] = '523c6add-51bb-4dbf-b629-1d882b11d09c'
    return req_params 

def get_url_sign():
    sign_params = get_sign_params()
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


def main():
    get_url_sign()
    
if __name__ == '__main__':
    import os
    import sys
    import requests

    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, parent_dir)

    from aliyunsdkcore.auth import rpc_signature_composer as rpc_signer
    main() 
