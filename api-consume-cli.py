#!/usr/bin/python3
import argparse
import requests
import json
import ast

#### Configue the argparser ####
parser  = argparse.ArgumentParser(prog='API Consumer', 
				  epilog='This work is available on github: https://github.com/rlucasfm/api-consume-cli/. Feel free to colaborate!!', 
				  description='Simple and easy tool developed to consume your simple REST API')
### Creating the arguments, options ###
parser.add_argument('endpoint', metavar='Endpoint', type=str, help='Endpoint of the API')
parser.add_argument('--bearer', action='store', type=str, help='Insert your bearer token for authentication')
parser.add_argument('data', action='store', type=str, help='Insert datakey for search in the form \'["KEY1","KEY2",...]\' or write a JSON Object as \'{"key":"value"}\'')
parser.add_argument('--method', action='store', type=str, help='Set the method for the HTTP req, as \'GET\' or \'PUT\', POST method as default')
parser.add_argument('--key', action='store', type=str, help='You can use --k. If you expect to get one of the first level keys only, on the form \'KEY\'', nargs='*')
parser.add_argument('--subkey', action='store', type=str, help='You can use --s. If you want to access one of the second level keys, on the form \'KEY\'', nargs='*')
parser.add_argument('--getauth', action='store_true', help='Use this if you want to auth and get you bearer. On data, write a JSON with the needed keys.')
parser.add_argument('--raw', action='store_true', help='If you want to see the response as it comes.')
parser.add_argument('--auth', action='store', type=str, help='If somekind of authentication is needed to access the api')

args = parser.parse_args()

### Loads the config json file ###
with open('config.json') as json_file:
	configData = json.load(json_file)
	authMethod = configData['auth']
	if 'bearer' in configData:
		bearerToken = configData['bearer']

if(args.bearer != None):
	bearer = args.bearer
else:
	bearer = bearerToken

if(args.method == None):
	method = 'POST'
else:
	method = args.method

if(args.auth != None):
	authMethod = args.auth

if(authMethod == 'bearer'):
	headers = {'Authorization': 'Bearer '+format(bearer), 'Content-Type': 'application/json', 'Accept': 'application/json'}
else:
	headers = {'Content-type': 'application/json', 'Accept': '*/*'}

raw_data = args.data

if args.getauth:
	raw_data = ast.literal_eval(raw_data)
	response = requests.post(args.endpoint, data=raw_data)
else:
	response = requests.post(args.endpoint, data=raw_data, headers = headers)

print("""
░╔═══╦═══╦══╗╔═══╦═══╦═╗░╔╦═══╦╗░╔╦═╗╔═╦═══╦═══╗
░║╔═╗║╔═╗╠╣╠╝║╔═╗║╔═╗║║╚╗║║╔═╗║║░║║║╚╝║║╔══╣╔═╗║
░║║░║║╚═╝║║║░║║░╚╣║░║║╔╗╚╝║╚══╣║░║║╔╗╔╗║╚══╣╚═╝║
░║╚═╝║╔══╝║║░║║░╔╣║░║║║╚╗║╠══╗║║░║║║║║║║╔══╣╔╗╔╝
░║╔═╗║║░░╔╣╠╗║╚═╝║╚═╝║║░║║║╚═╝║╚═╝║║║║║║╚══╣║║╚╗
░╚╝░╚╩╝░░╚══╝╚═══╩═══╩╝░╚═╩═══╩═══╩╝╚╝╚╩═══╩╝╚═╝
░┌──┐░░┌─┬┐░┌┐░░░░░░┌┐░░░░░░░░░░░░░░░░░░░░░░░░░░
░│┌┐├┬┐│┼├┼─┤└┬─┐┌┬┬┘│░░░░░░░░░░░░░░░░░░░░░░░░░░
░│┌┐││││┐┤│─┤││┼└┤┌┤┼│░░░░░░░░░░░░░░░░░░░░░░░░░░
░└──┼┐│└┴┴┴─┴┴┴──┴┘└─┘░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░└─┘░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
print('\n')

try:
	json_dict = response.json();
except:
	json_dict = {}
	print('Something wrong... You probably need to specify your auth, use the "--auth" option')

if not args.getauth:
	if not args.raw:
		try:
			if 'report' in json_dict:
				print('Registros encontrados: '+str(json_dict['report']['totalRetornado']))

			if(args.subkey != None):
				subkeyExists = True
				subkeys = args.subkey
			else:
				subkeyExists = False

			if(args.key != None):
				keystoshow = args.key
				for regs in range(len(json_dict['result'])):
					for key in keystoshow:
						if(subkeyExists):
							for subkey in subkeys:
								try:
									print(json.dumps(json_dict['result'][regs][key][subkey], indent=4))
								except Exception as err:
									print('Dict subkey not found')
						else:
							try:
								print(json.dumps(json_dict['result'][regs][key], indent=4))
							except Exception as err:
								print('Dict keys not found')
			else:
				print(json.dumps(json_dict['result'], indent=4))
		except Exception as err:
			print('Something wrong... Use the "--raw" tag to see the entire response without any treatments')
	else:
		print(json.dumps(json_dict, indent=4))
else:
	if(args.key != None):
		if(args.subkey != None):
			print('Subkeys not applicable in auth requests')
		for regs in args.key:
			print(json.dumps(json_dict[regs], indent=4))
	else:
		print(json.dumps(json_dict, indent=4))
