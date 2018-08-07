#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from remote_pdb import RemotePdb
import pyspark.daemon as original_daemon

if __name__ == '__main__':
    # Note it's super important we don't output anything to STDERR/STDOUT since
    # The Scala Spark expects certain bytes to happen to tell it how to connect to us
    debug_port = 7778
    fail = False
    try:
        RemotePdb('0.0.0.0', debug_port).set_trace()
    except:
        fail = True
    while fail and debug_port < 7799:
        try:
            RemotePdb('0.0.0.0', debug_port).set_trace()
            fail = False
        except:
            fail = True
    original_daemon.manager()
    
