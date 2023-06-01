#!/usr/bin/env python
import json

with open('keys.json') as json_file:
    data = json.load(json_file)

with open('bink.h', 'w') as out:
    out.write('''
 /******************************************************************
 * This file was automatically generated by convert_keys_to_cpp.py *
 *                         DO NOT EDIT                             *
 ******************************************************************/
 
#ifndef WINDOWSXPKG_BINK_H
#define WINDOWSXPKG_BINK_H

#include "shared.h"

std::unordered_map<std::string, std::unordered_map<int, std::string>> Products;
std::unordered_map<std::string, ECDLP_Params> BINKData;

void initBink() {
''')

    for product in data['Products']:
        d = data['Products'][product]
        k = 0
        for v in d:
            out.write('    Products["' + product + '"][' + str(k) + '] = "' + v + '";' + "\n")
            k += 1

    out.write("\n")

    for bink in data['BINK']:
        d = data['BINK'][bink]
        out.write('    BINKData["' + bink + '"] = {' +
                  '{"' + d['p'] + '", "' + d['a'] + '", "' + d['b'] + '"}, ' +
                  '{"' + d['pub']['x'] + '", "' + d['pub']['y'] + '"}, ' +
                  '{"' + d['g']['x'] + '", "' + d['g']['y'] + '"}, ' +
                  '"' + d['n'] + '", "' + d['priv'] + '"};' + "\n")

    out.write("""
}

#endif //WINDOWSXPKG_BINK_H
""")
