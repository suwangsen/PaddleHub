# coding:utf-8
# Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List

import paddlehub as hub
from paddlehub.commands import register, _commands


@register(name='hub.help', description='Show help for commands.')
class HelpCommand:
    def execute(self, argv: List) -> bool:
        msg = 'Usage:\n'
        msg += '    hub <command> <options>\n\n'
        msg += 'Commands:\n'
        for command, detail in _commands['hub'].items():
            if command.startswith('_'):
                continue

            if not '_description' in detail:
                continue
            msg += '    {:<15}        {}\n'.format(command, detail['_description'])

        print(msg)
        return True
