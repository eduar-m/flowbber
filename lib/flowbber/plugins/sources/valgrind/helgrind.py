# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 KuraLabs S.R.L
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""

Valgrind Helgrind
=================

This source parses and collects information from the XML generated by
`Valgrind's Helgrind`_ tool.

.. _`Valgrind's helgrind`: http://valgrind.org/docs/manual/hg-manual.html

Such XML file can be generated with:

.. code-block:: sh

    $ valgrind \\
        --tool=helgrind \\
        --gen-suppressions=all \\
        --read-var-info=yes \\
        --error-exitcode=1 \\
        --xml=yes \\
        --xml-file=helgrind.xml \\
        ./executable

**Data collected:**

.. code-block:: json

    {
        "protocolversion":"4"
        "protocoltool":"helgrind"
        "preamble":{
            "line":[
                "Helgrind, a thread error detector",
                "Copyright (C) 2007-2015, and GNU GPL'd, by OpenWorks LLP et al.",
                "Using Valgrind-3.11.0 and LibVEX; rerun with -h for copyright info",
                "Command: ./binary"
            ]
        },
        "pid":"11023"
        "ppid":"2162",
        "tool": "helgrind"
        "args":{
            "vargv":{
                "exe":"/usr/bin/valgrind.bin",
                "arg":[
                    "--tool=helgrind",
                    "--gen-suppressions=all",
                    "--read-var-info=yes",
                    "--error-exitcode=1",
                    "--xml=yes",
                    "--xml-file=helgrind.xml",
                ]
            },
            "argv":{
                "exe":"./binary",
                "arg":[]
            }
        }
        "status":[
            {
                "state":"RUNNING",
                "time":"00:00:00:01.593"
            },
            {
                "state":"FINISHED",
                "time":"00:00:00:58.060"
            }
        ],
        "error":[
            {
                "unique":"0x968"
                "tid":"4",
                "kind":"Race",
                "xwhat":[
                        {
                            "text":"Possible data race during write of size 1 at 0x12CD1C28 by thread #4",
                            "hthreadid":"4"
                        }
                ],
                "stack":[
                    {
                        "frame":[
                            {
                                "ip":"0xED467F",
                                "obj":"/home/library/binary",
                                "fn":"check_thread",
                                "dir":"/home/library",
                                "file":"hello.cpp"
                                "line":"76",
                            },
                            {
                                "ip":"0xED4DF2",
                                "obj":"/home/library/binary",
                                "fn":"main",
                                "dir":"/home/library",
                                "file":"hello.cpp"
                                "line":"130",
                            },
                        ],
                        "frame":[
                            {
                                "ip":"0xED467F",
                                "obj":"/home/library/binary",
                                "fn":"thread_exists",
                                "dir":"/home/library",
                                "file":"hello.cpp"
                                "line":"234",
                            },
                            {
                                "ip":"0xED9402",
                                "obj":"/home/library/binary",
                                "fn":"main",
                                "dir":"/home/library",
                                "file":"hello.cpp"
                                "line":"130",
                            },
                        ],
                    },
                ],
                "auxwhat":"Location 0x12cd1c28 is 0 bytes inside thread_data[1].valid,"
            }
        ],
    }


**Dependencies:**

.. code-block:: sh

    pip3 install flowbber[valgrind_helgrind]

**Usage:**

.. code-block:: toml

    [[sources]]
    type = "valgrind_helgrind"
    id = "..."

        [sources.config]
        xmlpath = "helgrind.xml"

.. code-block:: json

    {
        "sources": [
            {
                "type": "valgrind_helgrind",
                "id": "...",
                "config": {
                    "xmlpath": "helgrind.xml"
                }
            }
        ]
    }

xmlpath
-------

Path to Valgrind's Helgrind XML output.

- **Default**: ``N/A``
- **Optional**: ``False``
- **Schema**:

  .. code-block:: python3

     {
         'type': 'string',
         'empty': False,
     }

- **Secret**: ``False``

"""  # noqa

from . import ValgrindBaseSource


class ValgrindHelgrindSource(ValgrindBaseSource):
    pass


__all__ = ['ValgrindHelgrindSource']
