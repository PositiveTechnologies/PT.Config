[
{
    "conftype": "domain.xml",
    "name": "@port",
    "xpath": ".//network-listener[@protocol=\"admin-listener\"]",
    "default": "4848",
    "recommended": "4847",
    "not_recommended": "4848"
},
{
    "conftype": "domain.xml",
    "name": "jvm-options",
    "xpath": ".//java-config",
    "default": "",
    "recommended": "-Djava.security.manager"
},
{
    "conftype": "domain.xml",
    "name": "@audit-enabled",
    "xpath": ".//security-service",
    "default": "false",
    "recommended": "true"
},
{
    "conftype": "domain.xml",
    "name": "@value",
    "xpath": ".//security-service/audit-module/property[@name=\"auditOn\"]",
    "default": "false",
    "not_recommended": "false",
    "recommended": "true"
},
{
    "conftype": "domain.xml",
    "name": "@xpowered-by",
    "xpath": ".//http-listener",
    "default": "false",
    "recommended": "false"
}
]