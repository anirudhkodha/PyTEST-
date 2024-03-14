import yaml
import os.path

settings_dir = os.path.join(os.path.dirname(__file__), '..', 'Settings')
test_credentials_file = os.path.join(settings_dir, 'credentials.yml')

browserstack_config_dir = os.path.join(os.path.dirname(__file__), '../..', 'emembership_sel')
browserstack_data_file = os.path.join(browserstack_config_dir, 'browserstack.yml')

with open(test_credentials_file) as login_data:
	script_creds = yaml.safe_load(login_data)
print(script_creds)

with open(browserstack_data_file) as bs_options:
	bs_config = yaml.safe_load(bs_options)
print(bs_config)
