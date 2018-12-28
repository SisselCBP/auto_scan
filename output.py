result = {
    '10.3.8.211': {
        'state': 'up', #up, down
        'services': {
            80: {
                'name': 'http',
                'state': 'open', # open, closed, filtered, unfiltered, open|filtered, closed|filtered
            },
            22: {
                'name': 'ssh',
                'state': 'open',
            },
        },
        'system': 'windows', # windows, linux, unknown
        'is_router': False,
    },
    '192.168.12.1': {
        'state': 'up', #up, down
        'services': {
            80: {
                'name': 'http', # http, https, ssh, ftp, telnet, samba, balabala
                'state': 'open', # open, closed, filtered, unfiltered, open|filtered, closed|filtered
            },
            22: {
                'name': 'ssh',
                'state': 'open',
            }
        },
        'system': 'linux', # windows, linux, unknown
        'is_router': False,
    }
}

result_hosts = ['10.3.8.211', '10.3.8.216', '10.3.8.217']

result_local_info = {
    ''
}

