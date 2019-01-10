zabbix_study
===========

目录说明

```
WEBUI  zabbix-2.2.5/frontends/php/
字体   zabbix-2.2.5/fonts/            关系到中文支持
                    fonts/DejaVuSans.ttf 不支持中文
zabbix/etc/zabbix_server.conf
                    AlertScriptsPath  示警媒介脚本存放路径
```

查看CentOS系统字体
```
#fc-list
....
/usr/share/fonts/wqy-microhei/wqy-microhei.ttc: WenQuanYi Micro Hei Mono,文泉驛等寬微米黑:style=Regular
...
```

zabbix自定义agentd脚本部署
```
	1、zabbix_agentd服务配置文件zabbix_agentd.conf指定脚本配置文件所在位置:
		Include=/etc/zabbix/zabbix_agentd.d/*.conf

	2、编写、测试业务脚本
		/etc/zabbix/zabbix_agentd.d/zbx_redis_template/zbx_redis_stats.py -a foobared -p 6379 192.168.1.89 used_cpu_user none

	3、zabbix_agentd脚本配置文件指定key与shell映射关系：
		#redis.discovery
		UserParameter=redis.discovery,/etc/zabbix/zabbix_agentd.d/zbx_redis_template/zbx_redis_stats.py -p 6379 -a foobared localhost list_key_space_db
		#redis[{HOSTNAME}, gcc_version, none]
		UserParameter=redis[*],/etc/zabbix/zabbix_agentd.d/zbx_redis_template/zbx_redis_stats.py -p 6379 -a foobared $1 $2 $3
		说明：
			UserParameter=<key>,<shell command>  描述key与shell对应关系
			[,] 使用逗号分隔key，可在<shell command>中使用$n获取
			{HOSTNAME}宏变量  指代WEB配置“主机”时填写的”主机名称”，完整宏介绍：https://www.zabbix.com/documentation/3.0/manual/appendix/macros/supported_by_location#footnotes

	4、测试脚本在zabbix_agentd执行效果：
		zabbix_agentd -t "redis[192.168.1.89, used_cpu_user, none]" -c /etc/zabbix/zabbix_agentd.conf

	5、编写.xml模版定义文件(模版必须导入以便使用)（略）

	6、WEB配置中对key进行应用，对模版进行链接。
  ```
  
zabbix自定义server报警脚本部署
```
	动作
		标题
		内容
		zabbix users\groups
		报警媒介
	zabbix user
		收件人（企业微信号、企业微信组)
		报警媒介
	zabbix group
		zabbix user

	1、报警媒介脚本位置zabbix_server.conf：
		AlertScriptsPath=/usr/lib/zabbix/alertscripts

	2、给与执行权限
```

