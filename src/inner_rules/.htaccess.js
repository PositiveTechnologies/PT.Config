[{
    "conftype": ".htaccess",
    "name": "ServerSignature",
    "default": "off",
    "recommended": "off"
},
{
    "conftype": ".htaccess",
    "name": "Options",
    "default":  "FollowSymlinks",
    "recommended": "-Indexes -ExecCGI -Includes -Multiviews",
    "not_recommended": "([^-]*)(Indexes|ExecCGI|Includes|Multiviews|All)",
    "comparison_type": "regexp",
    "regexp": "([^-]*)(Indexes|ExecCGI|Includes|Multiviews|All)"
},
{
    "conftype": ".htaccess",
    "name": "AddType",
    "default": "",
    "recommended": "SetHandler application/x-httpd-php",
    "not_recommended": "application/x-httpd-php",
    "comparison_type": "in"
},
{
    "conftype": ".htaccess",
    "name": "AddType",
    "default": "",
    "recommended": "do not use",
    "not_recommended": "application/x-httpd-suphp",
    "comparison_type": "in"
},
{
    "conftype": ".htaccess",
    "name": "AddHandler",
    "default": "",
    "recommended": "SetHandler application/x-httpd-php",
    "not_recommended": "application/x-httpd-php",
    "comparison_type": "in"
},
{
    "conftype": ".htaccess",
    "name": "php_value",
    "default": "",
    "recommended": "do not use",
    "not_recommended": ["auto_prepend_file", "auto_append_file"],
    "comparison_type": "in"
}
]