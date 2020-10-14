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

class ListBaselineStatusesRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'ListBaselineStatuses')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SearchText(self):
		return self.get_body_params().get('SearchText')

	def set_SearchText(self,SearchText):
		self.add_body_params('SearchText', SearchText)

	def get_Owner(self):
		return self.get_body_params().get('Owner')

	def set_Owner(self,Owner):
		self.add_body_params('Owner', Owner)

	def get_Priority(self):
		return self.get_body_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_body_params('Priority', Priority)

	def get_PageNumber(self):
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_body_params('PageNumber', PageNumber)

	def get_TopicId(self):
		return self.get_body_params().get('TopicId')

	def set_TopicId(self,TopicId):
		self.add_body_params('TopicId', TopicId)

	def get_Bizdate(self):
		return self.get_body_params().get('Bizdate')

	def set_Bizdate(self,Bizdate):
		self.add_body_params('Bizdate', Bizdate)

	def get_FinishStatus(self):
		return self.get_body_params().get('FinishStatus')

	def set_FinishStatus(self,FinishStatus):
		self.add_body_params('FinishStatus', FinishStatus)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_BaselineTypes(self):
		return self.get_body_params().get('BaselineTypes')

	def set_BaselineTypes(self,BaselineTypes):
		self.add_body_params('BaselineTypes', BaselineTypes)

	def get_Status(self):
		return self.get_body_params().get('Status')

	def set_Status(self,Status):
		self.add_body_params('Status', Status)