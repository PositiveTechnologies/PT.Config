[{
    "conftype": "web.xml",
    "name": "http-method",
    "xpath": ".//security-constraint/web-resource-collection",
    "default": "",
    "recommended": "do not use",
    "not_recommended": ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH", "TRACE", "CONNECT"]
},
{
    "conftype": "web.xml",
    "name": "transport-guarantee",
    "xpath": ".//security-constraint/user-data-constraint",
    "default": "",
    "recommended": "CONFIDENTIAL"
},
{
    "conftype": "web.xml",
    "name": "session-timeout",
    "xpath": ".//session-config",
    "default": "30",
    "recommended": "15",
    "comparison_type": "<="
},
{
    "conftype": "web.xml",
    "name": "tracking-mode",
    "xpath": ".//session-config",
    "default": "",
    "recommended": "COOKIE"
},
{
    "conftype": "web.xml",
    "name": "http-only",
    "xpath": ".//session-config/cookie-config",
    "default": "false",
    "recommended": "true"
},
{
    "conftype": "web.xml",
    "name": "secure",
    "xpath": ".//session-config/cookie-config",
    "default": "false",
    "recommended": "true"
},
[
        {
            "conftype": "web.xml",
            "name": "param-name",
            "xpath": ".//servlet/init-param",
            "default": "",
            "recommended": "",
            "not_recommended": "debug"
        },
        {
            "conftype": "web.xml",
            "name": "param-value",
            "xpath": ".//servlet/init-param",
            "default": "false",
            "recommended": "false"
        }
],
[
        {
            "conftype": "web.xml",
            "name": "param-name",
            "xpath": ".//context-param",
            "default": "",
            "recommended": "",
            "not_recommended": "disable-xsrf-protection"
        },
        {
            "conftype": "web.xml",
            "name": "param-value",
            "xpath": ".//context-param",
            "default": "false",
            "recommended": "false"
        }
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "400"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "401"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "403"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "404"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "405"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "408"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "411"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "413"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "414"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "500"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "502"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "503"
}
],
[
{
    "conftype": "web.xml",
    "name": "location",
    "xpath": "error-page",
    "default": "",
    "recommended": "path_to_page",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "errcode",
    "not_recommended": ""
},
{
    "conftype": "web.xml",
    "name": "error-code",
    "xpath": "error-page",
    "default": "",
    "recommended": "504"
}
]
]