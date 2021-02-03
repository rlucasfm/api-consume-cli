#!/usr/bin/python3
import argparse
import requests
import json

parser  = argparse.ArgumentParser(prog='API Consumer', description='API Consumer CLI Application')

parser.add_argument('endpoint', metavar='endpoint', type=str, help='Endpoint of the API')
parser.add_argument('--bearer', action='store', type=str, help='Insert your bearer token for authentication')
parser.add_argument('data', action='store', type=str, help='Insert datakey for search')
parser.add_argument('--method', action='store', type=str, help='Set the method for the HTTP req')

args = parser.parse_args()

if(args.bearer == None):
	bearer = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYwMDU2MTdmY2FmYjE1NTk5MDMzZjlmZDNhMzI2MTc3NTEwOTJiZTcwZDU4NjI0NDVjZjI0ZDUyZjg5YTU2ZjE5NmQxMmRkNjFkZmM4YzU3In0.eyJhdWQiOiIyIiwianRpIjoiNjAwNTYxN2ZjYWZiMTU1OTkwMzNmOWZkM2EzMjYxNzc1MTA5MmJlNzBkNTg2MjQ0NWNmMjRkNTJmODlhNTZmMTk2ZDEyZGQ2MWRmYzhjNTciLCJpYXQiOjE2MTIzODI2NzMsIm5iZiI6MTYxMjM4MjY3MywiZXhwIjoxOTI3OTE1NDczLCJzdWIiOiI0MTM0Iiwic2NvcGVzIjpbXX0.mcUnyXYZCgpp46XrSaQb9BKNmrAEUeSq_-RsLtfHZFnZ-be0zwoKpMUUUY1vyazhAPcXYnwhK9idMAzT8IpkCadeFI7tVgLjJkLy6nIjicfGNmQgYZs-0PcQHq_1M8pzfWzz9atrD8Hz3HXiHMXCIM-Itewak7mAcRWgE-w94FJ7GcRSxZNWjKdXpLCDoLcPSlhpTEGBdQNGw7bJyMQ7_qEEc6txxvkgdC9yqmZAAY6VdL6FeGiqwT14DV8v_cZDziaSUqcfQLQJSnVFc0NGltphObBTDUg5J6PtDvHpSWQ6UWWY83LqMqFLXvOxPSlqmTemQ1_asDU6H5kmEUmv0VI8KlXOvBkSZqeXE-v9VFaibGEGdl_wi-dCpoFzhHnP8_vJD52OHIAnfl_PWT749k55LF65jsaqfM1YMhVHP_1VEiQuA0hFhkOCQt39jRv-HqDBG6ASl3sEwsO7BHwy03qFkv7EaYm3wmA5e5Mlw1fFhinGZbzfjkyAjxTgtFosJwMxUH17tcfuLp0kCmMAAFNydsbYGCm3ELRN4iSmTWw0pf9kB2NW1bJuPo_Jh8N3mvBB3fVuvUhCcAw3I70VFTxVLKFWrtZ6U5kw8hyCq0laQmpYjFJb-zeDqUkDT9E4rEdFvVihWM9uxFtdCVUB03wgt0ZzgOBkfSkGnVc44Jg'
else:
	bearer = args.bearer

if(args.method == None):
	method = 'POST'
else:
	method = args.method


headers = {'Authorization': 'Bearer '+format(bearer), 'Content-Type': 'application/json', 'Accept': 'application/json'}
raw_data = args.data

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

json_dict = response.json();

print('Registros encontrados: '+str(json_dict['report']['totalRetornado']))
print(json.dumps(response.json()['result'], indent=4))
