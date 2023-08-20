import configparser
config = configparser.ConfigParser()

config['google'] = {'name': 'id gsc_prf_in',
                    'institution': 'class gsc_prf_ila',
                    'keywords': 'class gsc_prf_inta"',
                    'papers': 'class gsc_a_at'}
''
with open('configuration.ini', 'w') as configfile:
  config.write(configfile)