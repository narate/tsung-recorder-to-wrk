import json
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) < 2:
    print('Usage: {} recorder.xml'.format(sys.argv[0]))
    exit(1)

tree = ET.parse(sys.argv[1])
requests = []
for req in tree.getroot().iter('request'):
    for http in req:
        if http.attrib.get('url') != '':
            path = http.attrib.get('url')
            m = http.attrib.get('method')
            contents = http.attrib.get('contents')
            content_type = http.attrib.get('content_type')
            data = {
                'path': path,
                'method': m
                }
            
            if not contents is None:
                data['body'] = contents

            headers = {}
            for h in http.iter('http_header'):
                headers[h.get('name')] =  h.get('value')

            if not content_type is None:
                headers['Content-Type'] = content_type
            
            data['headers'] = headers
            requests.append(data)
with open('wrk_data.json', 'w') as f:
    f.write(json.dumps(requests, indent=2, ensure_ascii=False))
    f.close()
print('saved to wrk_data.json')
