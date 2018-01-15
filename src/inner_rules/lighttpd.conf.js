[{
    "conftype": "lighttpd.conf",
    "name": "server.dir-listing",
    "default": "enable",
    "recommended": "disable"
},
{
    "conftype": "lighttpd.conf",
    "name": "status.status-url",
    "default": "",
    "recommended": ""
},
{
    "conftype": "lighttpd.conf",
    "name": "status.config-url",
    "default": "",
    "recommended": ""
},
{
    "conftype": "lighttpd.conf",
    "name": "setenv.add-response-header",
    "default": [],
    "recommended": "(\"Strict-Transport-Security\" => \"max-age=%d; includeSubDomains\",\"X-XSS-Protection\" => \"1; mode=block\",\"X-Frame-Options\" => \"DENY\",\"Access-Control-Allow-Origin\" => \"http://%s\",\"X-Content-Type-Options\" => \"nosniff\",\"X-Download-Options\" => \"noopen\",\"Content-Security-Policy\" => \"default-src 'self'\")",
    "comparison_type": "regexp",
    "regexp": {"Strict-Transport-Security": "max-age=[\\d]+; includeSubDomains",
               "X-XSS-Protection": "1; mode=block",
               "X-Frame-Options": "DENY",
               "Access-Control-Allow-Origin": "http://[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9](?:\\.[a-zA-Z]{2,})*$",
               "X-Content-Type-Options": "nosniff",
               "X-Download-Options": "noopen",
               "Content-Security-Policy": "default-src 'self'"
        },
    "comparison_method": "all"
},
{
    "conftype": "lighttpd.conf",
    "name": "cgi.assign",
    "xpath": "root",
    "default": [],
    "recommended": "$HTTP[\"url\"] =~ \"^/cgi-bin/\" {cgi.assign = (\".pl\"  => \"/usr/bin/perl\", \".py\"  => \"/usr/bin/python\")}",
    "not_recommended": [".pl", ".py"],
    "comparison_type": "in"
},
[
    {
        "conftype": "lighttpd.conf",
        "name": "webdav.activate",
        "default": "disable",
        "recommended": "disable",
        "not_recommended": "enable"
    },
    {
        "conftype": "lighttpd.conf",
        "name": "auth.backend",
        "default": "",
        "recommended": "htpasswd",
        "not_recommended": ""
    },
    {
        "conftype": "lighttpd.conf",
        "name": "auth.backend.htpasswd.userfile",
        "default": "",
        "recommended": "some/path",
        "not_recommended": ""
    },
    {
        "conftype": "lighttpd.conf",
        "name": "auth.require",
        "default": "",
        "recommended": "(\"\" => (\"method\" => \"basic\", \"realm\" => \"webdav\", \"require\"=> \"valid-user\"))",
        "not_recommended": ""
    },
    {
        "conftype": "lighttpd.conf",
        "name": "webdav.is-readonly",
        "default": "disable",
        "recommended": "enable"
    }
]
]