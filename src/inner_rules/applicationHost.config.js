[{
    "conftype": "applicationHost.config",
    "name": "@userName",
    "xpath": ".//system.webServer/security/authentication/anonymousAuthentication",
    "default": "IUSR",
    "recommended": ""
},
[
    {
        "conftype": "applicationHost.config",
        "name": "@accessPolicy",
        "xpath": ".//system.webServer/handlers",
        "default": "Read",
        "recommended": "Read",
        "not_recommended": ["Script", "Execute"],
        "comparison_type": "in"
    },
    {
        "conftype": "applicationHost.config",
        "name": "@accessPolicy",
        "xpath": ".//system.webServer/handlers",
        "default": "Read",
        "recommended": "Read",
        "not_recommended": "Write",
        "comparison_type": "in"
    }
],
{
    "conftype": "applicationHost.config",
    "name": "@notListedIsapisAllowed",
    "xpath": ".//system.webServer/security/isapiCgiRestriction",
    "default": "false",
    "recommended": "false"
}
]