
import json
from os import name

# Opening JSON file
with open('script/data.json', 'r') as openfile:

    # Reading from json file
    json_object = json.load(openfile)

f2 = open("./lib/canbus/canbus.h", "w+")
f2.write('#ifndef CANBUS_H\n#define CANBUS_H\n#include <stdint.h>\n#include <stdbool.h>')
for x in range(len(json_object['messages'][0]['signals'])):
    f2.write('\n\nbool canbus_set_')
    f2.write(json_object['messages'][0]['signals'][x]['name'])
    f2.write('(')
    f2.write(json_object['messages'][0]['signals'][x]['type'])
    f2.write(' value)')
    f2.write('\n')
    f2.write(json_object['messages'][0]['signals'][x]['type'])
    f2.write(' canbus_get_')
    f2.write(json_object['messages'][0]['signals'][x]['name'] + '(void)')

for x in range(len(json_object['messages'][1]['signals'])):
    f2.write('\n\nbool canbus_set_')
    f2.write(json_object['messages'][1]['signals'][x]['name'])
    f2.write('(')
    f2.write(json_object['messages'][1]['signals'][x]['type'])
    f2.write(' value)')
    f2.write('\n')
    f2.write(json_object['messages'][1]['signals'][x]['type'])
    f2.write(' canbus_get_')
    f2.write(json_object['messages'][1]['signals'][x]['name'] + '(void)')
