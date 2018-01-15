[{
    "conftype": "server.xml_tomcat",
    "name": "@xpoweredBy",
    "xpath": ".//Service/Connector",
    "default": "false",
    "recommended": "false"
},
{
    "conftype": "server.xml_tomcat",
    "name": "@allowTrace",
    "xpath": ".//Service/Connector",
    "default": "false",
    "recommended": "false"
},
{
    "conftype": "server.xml_tomcat",
    "name": "@shutdown",
    "xpath": "./",
    "default": "SHUTDOWN",
    "recommended": "NONDETERMINISTICVALUE",
    "not_recommended": "SHUTDOWN"
},
{
    "conftype": "server.xml_tomcat",
    "name": "@clientAuth",
    "xpath": ".//Service/Connector",
    "default": "false",
    "recommended": "true"
},
{
    "conftype": "server.xml_tomcat",
    "name": "@secure",
    "xpath": ".//Service/Connector",
    "default": "false",
    "recommended": "true"
},
{
    "conftype": "server.xml_tomcat",
    "name": "@autoDeploy",
    "xpath": ".//Service/Engine/Host",
    "default": "true",
    "recommended": "false"
},
{
    "conftype": "server.xml_tomcat",
    "name": "@deployOnStartup",
    "xpath": ".//Service/Engine/Host",
    "default": "true",
    "recommended": "false"
},
{
    "conftype": "server.xml_tomcat",
    "name": "@connectionTimeout",
    "xpath": ".//Service/Connector",
    "default": "60000",
    "recommended": "60000",
    "comparison_type": "<="
                                        
},
{
    "conftype": "server.xml_tomcat",
    "name": "@connectionTimeout",
    "xpath": ".//Service/Connector",
    "default": "60000",
    "recommended": "60000",
    "not_recommended": "-1"
},
{
    "conftype": "server.xml_tomcat",
    "name": "@maxHttpHeaderSize",
    "xpath": ".//Service/Connector",
    "default": "8192",
    "recommended": "8192",
    "comparison_type": "<="
}
]