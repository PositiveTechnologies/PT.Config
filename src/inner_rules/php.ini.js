[{
    "conftype": "php.ini",
    "name": "allow_url_fopen",
    "default": "1",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "allow_url_include",
    "default": "0",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "cgi.fix_pathinfo",
    "default": "1",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "display_errors",
    "default": "1",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "display_startup_errors",
    "default": "0",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "enable_dl",
    "default": "1",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "expose_php",
    "default": "1",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "magic_quotes_gpc",
    "default": "1",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "magic_quotes_runtime",
    "default": "0",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "magic_quotes_sybase",
    "default": "0",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "register_globals",
    "default": "0",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "safe_mode",
    "default": "0",
    "recommended": "1"
},
{
    "conftype": "php.ini",
    "name": "log_errors",
    "default": "0",
    "recommended": "1"
},
{
    "conftype": "php.ini",
    "name": "request_order",
    "default": "GP",
    "recommended": "GP"
},
{
    "conftype": "php.ini",
    "name": "assert.active",
    "default": "1",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "auto_append_file",
    "default": "",
    "recommended": ""
},
{
    "conftype": "php.ini",
    "name": "auto_prepend_file",
    "default": "",
    "recommended": ""
},
{
    "conftype": "php.ini",
    "name": "max_execution_time",
    "default": "30",
    "recommended": "30",
    "comparison_type": "<="
},
{
    "conftype": "php.ini",
    "name": "max_input_time",
    "default": "-1",
    "recommended": "30",
    "not_recommended": "-1"
},
{
    "conftype": "php.ini",
    "name": "max_input_time",
    "default": "-1",
    "recommended": "30",
    "comparison_type": "<="
},
{
    "conftype": "php.ini",
    "name": "max_input_nesting_level",
    "default": "64",
    "recommended": "64",
    "comparison_type": "<="
},
{
    "conftype": "php.ini",
    "name": "memory_limit",
    "default": "128M",
    "recommended": "128M",
    "comparison_type": "<="
},
{
    "conftype": "php.ini",
    "name": "post_max_size",
    "default": "8M",
    "recommended": "8M",
    "comparison_type": "<="
},
{
    "conftype": "php.ini",
    "name": "upload_max_filesize",
    "default": "2M",
    "recommended": "2M",
    "comparison_type": "<="
},
{
    "conftype": "php.ini",
    "name": "open_basedir",
    "default": "",
    "recommended": "some/path",
    "not_recommended": ""
},
{
    "conftype": "php.ini",
    "name": "session.cookie_httponly",
    "default": "0",
    "recommended": "1"
},
{
    "conftype": "php.ini",
    "name": "session.save_path",
    "default": "",
    "recommended": "some/path",
    "not_recommended": ["", "\"/tmp\""]
},
{
    "conftype": "php.ini",
    "name": "session.use_strict_mode",
    "default": "0",
    "recommended": "1"
},
{
    "conftype": "php.ini",
    "name": "session.use_cookies",
    "default": "1",
    "recommended": "1"
},
{
    "conftype": "php.ini",
    "name": "session.use_only_cookies",
    "default": "1",
    "recommended": "1"
},
{
    "conftype": "php.ini",
    "name": "session.cookie_secure",
    "default": "0",
    "recommended": "1"
},
{
    "conftype": "php.ini",
    "name": "session.cookie_lifetime",
    "default": "0",
    "recommended": "0"
},
{
    "conftype": "php.ini",
    "name": "disable_functions",
    "default": "",
    "recommended": ["popen","exec","system","passthru","proc_open","shell_exec","apache_setenv","putenv","dl","expect_popen","pcntl_exec"],
    "comparison_type": "in",
    "comparison_method": "all"
}
]