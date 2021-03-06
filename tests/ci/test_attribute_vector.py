# Copyright 2018 www.privaz.io Valletech AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import pyone

class AttributeVectorTests(unittest.TestCase):
    def test_dict_to_attr(self):
        atts = {
            'NAME': 'abc',
            'MEMORY': '1024',
            'ATT1': 'value1'
            }
        self.assertIn(pyone.util.dict2one(atts),[ '''NAME = "abc"\nATT1 = "value1"\nMEMORY = "1024"\n''','''NAME = "abc"\nMEMORY = "1024"\nATT1 = "value1"\n'''])
