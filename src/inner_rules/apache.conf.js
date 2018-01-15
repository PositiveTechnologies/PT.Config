[{
    "conftype": "apache.conf",
    "name": "ServerTokens",
    "xpath": "ServerConfig",
    "default": "Full",
    "recommended": ["Prod", "Product Only"]
},
{
    "conftype": "apache.conf",
    "name": "TraceEnable",
    "xpath": ["ServerConfig","VirtualHost"],
    "default": "on",
    "recommended": "off"
},
{
    "conftype": "apache.conf",
    "name": "ServerSignature",
    "default": "off",
    "recommended": "off"
},
{
    "conftype": "apache.conf",
    "name": "LoadModule",
    "xpath": ["ServerConfig","VirtualHost"],
    "default": "",
    "recommended": "do not use",
    "not_recommended": ["autoindex_module","include_module","info_module","cgi_module", "negotiation_module"],
    "comparison_type": "in"
},
{
    "conftype": "apache.conf",
    "name": "LoadModule",
    "xpath": ["ServerConfig","VirtualHost"],
    "default": "",
    "recommended": "security2_module",
    "comparison_type": "in"
},
{
    "conftype": "apache.conf",
    "name": "Options",
    "default":  "FollowSymlinks",
    "recommended": "-Indexes -ExecCGI -Includes -Multiviews",
    "not_recommended": "([^-]*)(Indexes|ExecCGI|Includes|Multiviews|All)",
    "comparison_type": "regexp",
    "regexp": "([^-]*)(Indexes|ExecCGI|Includes|Multiviews|All)"
},
{
    "conftype": "apache.conf",
    "name": "AddType",
    "default": "",
    "recommended": "SetHandler application/x-httpd-php",
    "not_recommended": "application/x-httpd-php",
    "comparison_type": "in"
},
{
    "conftype": "apache.conf",
    "name": "AddType",
    "default": "",
    "recommended": "do not use",
    "not_recommended": "application/x-httpd-suphp",
    "comparison_type": "in"
},
{
    "conftype": "apache.conf",
    "name": "AddHandler",
    "default": "",
    "recommended": "SetHandler application/x-httpd-php",
    "not_recommended": "application/x-httpd-php",
    "comparison_type": "in"
},
{
    "conftype": "apache.conf",
    "name": "php_value",
    "default": "",
    "recommended": "do not use",
    "not_recommended": ["auto_prepend_file", "auto_append_file"],
    "comparison_type": "in"
}
]