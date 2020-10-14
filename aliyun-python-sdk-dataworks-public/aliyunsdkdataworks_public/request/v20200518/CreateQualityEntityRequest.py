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

from aliyunsdkcore.request import RpcRequest
from aliyunsdkdataworks_public.endpoint import endpoint_data

class CreateQualityEntityRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'CreateQualityEntity')
		self.set_protocol_type('https')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ProjectName(self):
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_body_params('ProjectName', ProjectName)

	def get_EntityLevel(self):
		return self.get_body_params().get('EntityLevel')

	def set_EntityLevel(self,EntityLevel):
		self.add_body_params('EntityLevel', EntityLevel)

	def get_MatchExpression(self):
		return self.get_body_params().get('MatchExpression')

	def set_MatchExpression(self,MatchExpression):
		self.add_body_params('MatchExpression', MatchExpression)

	def get_EnvType(self):
		return self.get_body_params().get('EnvType')

	def set_EnvType(self,EnvType):
		self.add_body_params('EnvType', EnvType)

	def get_TableName(self):
		return self.get_body_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_body_params('TableName', TableName)