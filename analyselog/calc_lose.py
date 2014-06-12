import re
data=[]
#for line in open("/home/frank/Downloads/2pl.ms.log/2pl.HITSZ_CS_13.marv.0.1.log"):

for line in open("/home/frank/dev/project/Texas/project_acpc_server/seed560980368ms.1.log"):
    re_obj=re.search(r'(-?\d+)\|(-?\d+):(\w+)\|(\w+)',line)
    if not re_obj:
        continue
    result=re_obj.groups()
    value=int(dict(zip(result[2:],result[:2]))['song'])
    if value<0:
        data.append(value)
print('ljp' ,(sum(data)))
