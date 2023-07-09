import os

from fabric import Connection

base_dir = 'C:\\Users\\L-yangsen\\Desktop\\domain_data'
base_nod_sld_dir = base_dir + '\\nod\\sld'
base_spike_sld_dir = base_dir + '\\spike\\sld'
base_nod_black_dir = base_dir + '\\blacksite\\sld'
remote_nod_sld = '/home/l-yangsen/nod/sld'
remote_spike_sld = '/home/l-yangsen/spike/sld'
remote_nod_black = '/home/l-yangsen/blacksite/sld'

sp_nod_sld = '/home/scam/qax/nod/sld'
sp_spike_sld = '/home/scam/qax/spike/sld'
sp_nod_black = '/home/scam/qax/blacksite/sld'

qianxin_user = 'l-yangsen'
qianxin_host = 'fe03v.yjy.shyc3.qianxin-inc.cn'
qianxin_password = 'Ys2015@qianxin666'

c = Connection(host=f'{qianxin_user}@{qianxin_host}',
    connect_kwargs=dict(
    password=qianxin_password
))

nas = Connection(host='scam@124.220.19.68',connect_kwargs=dict(password='Scam2021@!'))

c.run('/home/l-yangsen/miniconda3/bin/python /home/l-yangsen/update_spike_sld.py')
#c.run('/home/l-yangsen/miniconda3/bin/python /home/l-yangsen/update_nod_sld.py')
#c.run('/home/l-yangsen/miniconda3/bin/python /home/l-yangsen/update_nod_black.py')

c.get('/home/l-yangsen/spike_sld_sync.log', 'C:\\Users\\L-yangsen\\Desktop\\spike_sld_sync.log')
#c.get('/home/l-yangsen/nod_sld_sync.log', 'C:\\Users\\L-yangsen\\Desktop\\nod_sld_sync.log')
#c.get('/home/l-yangsen/blacksite_sld_sync.log', 'C:\\Users\\L-yangsen\\Desktop\\blacksite_sld_sync.log')

with open('C:\\Users\\L-yangsen\\Desktop\\spike_sld_sync.log', 'r') as f:
    lines = f.readlines()
    for line in lines:
        date = line.strip()
        zip_path = base_spike_sld_dir + f'/{date}.zip'
        if os.path.exists(zip_path):
            continue
        else:
            remote_zip = remote_spike_sld + f'/{date}.zip'
            print('update ' + remote_zip)
            c.get(remote_zip, zip_path)
            nas_zip = sp_spike_sld + f'/{date}.zip'
            nas.put(zip_path, nas_zip)

# with open('C:\\Users\\L-yangsen\\Desktop\\nod_sld_sync.log', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         date = line.strip()
#         zip_path = base_nod_sld_dir + f'/{date}.zip'
#         if os.path.exists(zip_path):
#             continue
#         else:
#             remote_zip = remote_nod_sld + f'/{date}.zip'
#             c.get(remote_zip, zip_path)
#             print('update' + remote_zip)
#             nas_zip = sp_nod_sld + f'/{date}.zip'
#             nas.put(zip_path, nas_zip)

# with open('C:\\Users\\L-yangsen\\Desktop\\blacksite_sld_sync.log', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         date = line.strip()
#         zip_path = base_nod_black_dir + f'/{date}.zip'
#         if os.path.exists(zip_path):
#             continue
#         else:
#             remote_zip = remote_nod_black + f'/{date}.zip'
#             print(remote_zip)
#             try:
#                 c.get(remote_zip, zip_path)
#                 print('update' + remote_zip)
#                 nas_zip = sp_nod_black + f'/{date}.zip'
#                 nas.put(zip_path, nas_zip)
#             except:
#                 continue