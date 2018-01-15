[{
    "conftype": "nginx.conf",
    "name": "autoindex",
    "xpath": ["http", "server", "location"],
    "default": "off",
    "recommended": "off"
},
{
    "conftype": "nginx.conf",
    "name": "ssi",
    "xpath": ["http", "server", "location"],
    "default": "off",
    "recommended": "off"
},
{
    "conftype": "nginx.conf",
    "name": "server_tokens",
    "xpath": ["http", "server", "location"],
    "default": "on",
    "recommended": "off"
},
{
    "conftype": "nginx.conf",
    "name": "ssl_prefer_server_ciphers",
    "xpath": ["http", "server"],
    "default": "off",
    "recommended": "on"
},
{
    "conftype": "nginx.conf",
    "name": "ssl_stapling",
    "xpath": ["http", "server"],
    "default": "off",
    "recommended": "on"
},
{
    "conftype": "nginx.conf",
    "name": "ssl",
    "xpath": ["http", "server"],
    "default": "off",
    "recommended": "on"
},
{
    "conftype": "nginx.conf",
    "name": "ssl_certificate",
    "xpath": ["http", "server"],
    "default": "",
    "recommended": "path/to/cert",
    "not_recommended": ""
},
{
    "conftype": "nginx.conf",
    "name": "ssl_certificate_key",
    "xpath": ["http", "server"],
    "default": "",
    "recommended": "path/to/key",
    "not_recommended": ""
},
[
    {
        "conftype": "nginx.conf",
        "name": "ssl",
        "xpath": ["http", "server"],
        "default": "off",
        "recommended": "off"
    },
    {
        "conftype": "nginx.conf",
        "name": "ssl_ciphers",
        "xpath": ["http", "server"],
        "default": "ALL: !aNULL:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP",
        "recommended": "EDH",
        "comparison_type": "in"
    },
    {
        "conftype": "nginx.conf",
        "name": "ssl_dhparam",
        "xpath": ["http", "server"],
        "default": "",
        "recommended": "Path/to/dhparam",
        "not_recommended": ""
    }
],
{
    "conftype": "nginx.conf",
    "name": "ssl_session_timeout",
    "xpath": ["http", "server"],
    "default": "5m",
    "recommended": "5m",
    "regexp": "(([5-9])|(1[0-5]))m",
    "comparison_type": "regexp"
},
{
    "conftype": "nginx.conf",
    "name": "ssl_session_cache",
    "xpath": ["http", "server"],
    "default": "none",
    "recommended": "shared:SSL:2m",
    "comparison_type": "regexp",
    "regexp": "shared:SSL:(([2-9])|10)m"
},
{
    "conftype": "nginx.conf",
    "name": "ssl_protocols",
    "xpath": ["http", "server"],
    "default": "TLSv1 TLSv1.1 TLSv1.2",
    "recommended": "TLSv1 TLSv1.1 TLSv1.2",
    "not_recommended": ["SSLv2", "SSLv3"],
    "comparison_type": "in"
},
{
    "conftype": "nginx.conf",
    "name": "ssl_ciphers",
    "xpath": ["http", "server"],
    "default": "ALL: !aNULL:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP",
    "recommended": "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH",
    "not_recommended": ["MEDIUM", "LOW", "aNULL", "eNULL", "EXPORT", "DES", "MD5","PSK", "RC4"],
    "comparison_type": "in"
}
]