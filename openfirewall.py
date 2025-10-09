# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.

import keyboard
import json
import os
import pypinyin
from alibabacloud_ecs20140526.client import Client as EcsClient
from alibabacloud_credentials.client import Client as CredClient
from alibabacloud_credentials.models import Config as CreConfig
from alibabacloud_sts20150401.models import AssumeRoleRequest
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_openapi.models import Config
from alibabacloud_sts20150401.client import Client as Sts20150401Client
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util.models import RuntimeOptions

class ruleConfig:
    def __init__(self, file):
        self.name = "dyq"
        self.ip = "127.0.0.1"
        self.port_range = "-1/-1"
        self.policy = "accept"
        self.priority = "1"
        self.ip_protocol = "ALL"
        if file is not None:
            self.name = file['name']
            self.ip = file['ip']
            self.source_group_id = file['source_group_id']
            self.access_key_id = file['access_key_id']
            self.access_key_secret = file['access_key_secret']
            self.role_arn = file['role_arn']
            if self.ip == "127.0.0.1" or self.ip == "xx.xx.xx.xx":
                print("请先修改ip.json文件中的ip地址")
                print("按任意键退出...")
                keyboard.read_key()  # 等待任意按键
                os._exit(0)
            else:
                print(f"配置文件加载成功,当前配置:姓名:{self.name},ip:{self.ip}")
        else:
            FileNotFoundError("配置文件不存在")
            print("按任意键退出...")
            keyboard.read_key()  # 等待任意按键
            os._exit(0)


class firewall:
    def __init__(self):
        pass

    @staticmethod
    def create_client(rule) -> EcsClient:
        print('正在获取STS Token')
        config = Config(
            access_key_id=rule.access_key_id,
            access_key_secret=rule.access_key_secret
        )
        config.endpoint = "sts.aliyuncs.com"
        stsClient = Sts20150401Client(config)
        assume_role_request = AssumeRoleRequest(
            # 会话有效时间
            duration_seconds=3600,
            # 要扮演的RAM角色ARN，防火墙专用ram
            role_arn=rule.role_arn,
            # 角色会话名称
            role_session_name=f'session-{pypinyin.slug(rule.name)}'
        )
        runtime = RuntimeOptions()
        print('正在初始化ECS Client')
        try:
            resp = stsClient.assume_role_with_options(assume_role_request, runtime)
            assumeRoleResponseBodyCredentials = resp.body.credentials

            # 使用STS Token初始化Credentials Client。
            credentialsConfig = CreConfig(
                # 凭证类型。
                type='sts',
                # 设置为AccessKey ID值。
                access_key_id=assumeRoleResponseBodyCredentials.access_key_id,
                # 设置为AccessKey Secret值。
                access_key_secret=assumeRoleResponseBodyCredentials.access_key_secret,
                # 设置为STS Token值。
                security_token=assumeRoleResponseBodyCredentials.security_token
            )
            credentialClient = CredClient(credentialsConfig)
            ecsConfig = Config(credential=credentialClient)
            # 配置云产品服务接入地址（endpoint）。
            ecsConfig.endpoint = 'ecs.cn-guangzhou.aliyuncs.com'
            # 初始化ECS Client。
            ecsClient = EcsClient(ecsConfig)
        except Exception as error:
            # 错误 message
            print(error.message)

        return ecsClient

    @staticmethod
    def addrule(
        rule
    ) -> None:
        client = firewall.create_client(rule)
        print('正在添加ECS防火墙规则')
        permissions_0 = ecs_20140526_models.AuthorizeSecurityGroupRequestPermissions(
            policy=rule.policy,
            priority=rule.priority,
            ip_protocol=rule.ip_protocol,
            ipv_6source_cidr_ip='',
            source_cidr_ip=rule.ip,
            source_group_id=rule.source_group_id,
            port_range=rule.port_range,
            dest_cidr_ip='',
            ipv_6dest_cidr_ip='',
            source_port_range='',
            source_group_owner_account='',
            nic_type='internet',
            description=f'{rule.name}自动创建'
        )
        authorize_security_group_request = ecs_20140526_models.AuthorizeSecurityGroupRequest(
            region_id='cn-guangzhou',
            security_group_id=rule.source_group_id,
            permissions=[
                permissions_0
            ],
            client_token=''
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            client.authorize_security_group_with_options(authorize_security_group_request, runtime)
            print(f"成功开放ip:{rule.ip}")
            print("按任意键退出...")
            keyboard.read_key()  # 等待任意按键
            os._exit(0)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    with open('./ip.json','r',encoding='utf8')as fp:
        json_data = json.load(fp)

    config = ruleConfig(json_data)

    firewall.addrule(config)

