# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
from aliyunsdkairec.endpoint import endpoint_data

class ModifyFilteringAlgorithmMetaRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Airec', '2020-11-26', 'ModifyFilteringAlgorithmMeta','airec')
		self.set_uri_pattern('/v2/openapi/instances/[instanceId]/filtering-algorithms/[algorithmId]/meta')
		self.set_method('PUT')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_instanceId(self):
		return self.get_path_params().get('instanceId')

	def set_instanceId(self,instanceId):
		self.add_path_param('instanceId',instanceId)

	def get_algorithmId(self):
		return self.get_path_params().get('algorithmId')

	def set_algorithmId(self,algorithmId):
		self.add_path_param('algorithmId',algorithmId)