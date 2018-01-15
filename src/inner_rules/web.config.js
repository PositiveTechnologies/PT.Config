[
{
    "conftype": "web.config",
    "name": "@debug",
    "xpath": ".//system.web/compilation",
    "default": "false",
    "recommended": "false"
},
{
    "conftype": "web.config",
    "name": "@enableHeaderChecking",
    "xpath": ".//system.web/httpRuntime",
    "default": "true",
    "recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@enableVersionHeader",
    "xpath": ".//system.web/httpRuntime",
    "default": "true",
    "recommended": "false"
},
{
    "conftype": "web.config",
    "name": "@mode",
    "xpath": ".//system.web/customErrors",
    "default": "RemoteOnly",
    "recommended": "RemoteOnly"
},
{
    "conftype": "web.config",
    "name": "@enableViewStateMac",
    "xpath": ".//system.web/pages",
    "default": "true",
    "recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@enableEventValidation",
    "xpath": ".//system.web/pages",
    "default": "true",
    "recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@viewStateEncryptionMode",
    "xpath": ".//system.web/pages",
    "default": "Auto",
    "recommended": "Always"
},
{
    "conftype": "web.config",
    "name": "@validateRequest",
    "xpath": ".//system.web/pages",
    "default": "true",
    "recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@httpOnlyCookies",
    "xpath": ".//system.web/httpCookies",
    "default": "false",
    "recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@requireSSL",
    "xpath": ".//system.web/httpCookies",
    "default": "false",
    "recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@useUnsafeHeaderParsing",
    "xpath": ".//system.net/settings/httpWebRequest",
    "default": "false",
    "recommended": "false"
},
{
    "conftype": "web.config",
    "name": "@value",
    "xpath": ".//add",
    "default": "",
    "recommended": "deleteAfterServicing=true;",
    "not_recommended": ["storage=file", "deleteAfterServicing=false"],
    "comparison_type": "in",
    "comparison_method": "all"
},
[
{
    "conftype": "web.config",
    "name": "@name",
    "xpath": ".//system.web/membership/providers/add",
    "default": "",
    "recommended": "",
    "not_recommended": "Sql",
    "comparison_type": "in"
},
{
    "conftype": "web.config",
    "name": "@passwordFormat",
    "xpath": ".//system.web/membership/providers/add",
    "default": "Hashed",
    "recommended": "Hashed",
    "not_recommended": "Clear"
}
],
{
    "conftype": "web.config",
    "name": "@passwordFormat",
    "xpath": ".//system.web/membership/providers/add[@name=\"MembershipADProvider\"]",
    "default": "Hashed",
    "recommended": "Hashed",
    "not_recommended": "Clear"
},
{
    "conftype": "web.config",
    "name": "@enabled",
    "xpath": ".//system.web/trace/",
    "default": "false",
    "recommended": "false"
},
{
    "conftype": "web.config",
    "name": "@maxRequestLength",
    "xpath": ".//system.web/httpRuntime",
    "default": "4096",
    "recommended": "4096",
    "comparison_type": "<="
},
{
    "conftype": "web.config",
    "name": "@protection",
    "xpath": ".//system.web/authentication[@mode=\"Forms\"]/forms",
    "default": "All",
    "recommended": "All"
},
{
    "conftype": "web.config",
    "name": "@timeout",
    "xpath": ".//system.web/authentication[@mode=\"Forms\"]/forms[@requireSSL=\"true\"]",
    "default": "30",
    "recommended": "30",
    "comparison_type": "<="
},
[
{
    "conftype": "web.config",
    "name": "@requireSSL[@authentication]",
    "xpath": ".//system.web/authentication[@mode=\"Forms\"]/forms",
    "default": "false",
    "recommended": "true",
    "not_recommended": "false"
},
{
    "conftype": "web.config",
    "name": "@slidingExpiration",
    "xpath": ".//system.web/authentication[@mode=\"Forms\"]/forms",
    "default": "true",
    "recommended": "false"
}
],
{
    "conftype": "web.config",
    "name": "@users",
    "xpath": ".//system.web/authorization/deny",
    "default": "",
    "recommended": "?"
},
{
    "conftype": "web.config",
    "name": "@connectionProtection",
    "xpath": ".//system.web/membership/providers/add[@name=\"MembershipADProvider\"]",
    "default": "Secure",
    "recommended": "Secure"
},
[
{
    "conftype": "web.config",
    "name": "@enabled",
    "xpath": ".//system.web/roleManager",
    "default": "false",
    "recommended": "false",
    "not_recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@cookieProtection",
    "xpath": ".//system.web/roleManager[@enabled=\"true\"]",
    "default": "All",
    "recommended": "All"
}
],
[
{
    "conftype": "web.config",
    "name": "@enabled",
    "xpath": ".//system.web/roleManager",
    "default": "false",
    "recommended": "false",
    "not_recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@cookieRequireSSL",
    "xpath": ".//system.web/roleManager[@enabled=\"true\"]",
    "default": "false",
    "recommended": "true"
}
],
[
{
    "conftype": "web.config",
    "name": "@enabled",
    "xpath": ".//system.web/roleManager",
    "default": "false",
    "recommended": "false",
    "not_recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@cookieRequireSSL",
    "xpath": ".//system.web/roleManager[@enabled=\"true\"]",
    "default": "false",
    "recommended": "false",
    "not_recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@cookieTimeout",
    "xpath": ".//system.web/roleManager[@enabled=\"true\"]",
    "default": "30",
    "recommended": "15",
    "comparison_type": "<="
}
],
[
{
    "conftype": "web.config",
    "name": "@enabled",
    "xpath": ".//system.web/roleManager",
    "default": "false",
    "recommended": "false",
    "not_recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@cookieRequireSSL",
    "xpath": ".//system.web/roleManager[@enabled=\"true\"]",
    "default": "false",
    "recommended": "true",
    "not_recommended": "false"
},
{
    "conftype": "web.config",
    "name": "@cookieSlidingExpiration",
    "xpath": ".//system.web/roleManager[@enabled=\"true\"]",
    "default": "true",
    "recommended": "false"
}
],
[
{
    "conftype": "web.config",
    "name": "@enabled",
    "xpath": ".//system.web/roleManager",
    "default": "false",
    "recommended": "false",
    "not_recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@createPersistentCookie",
    "xpath": ".//system.web/roleManager[@enabled=\"true\"]",
    "default": "false",
    "recommended": "false"
}
],
{
    "conftype": "web.config",
    "name": "@validation",
    "xpath": ".//system.web/machineKey",
    "default": "SHA1",
    "recommended": ["SHA1", "AES"]
},
{
    "conftype": "web.config",
    "name": "@decryptionKey",
    "xpath": ".//system.web/machineKey",
    "default": "AutoGenerate,IsolateApps",
    "recommended": "AutoGenerate,IsolateApps"
},
{
    "conftype": "web.config",
    "name": "@validationKey",
    "xpath": ".//system.web/machineKey",
    "default": "AutoGenerate,IsolateApps",
    "recommended": "AutoGenerate,IsolateApps"
},
{
    "conftype": "web.config",
    "name": "@allowOverride",
    "xpath": ".//location",
    "default": "true",
    "recommended": "false"
},
{
    "conftype": "web.config",
    "name": "@maxEventLengthForSimpleMessage",
    "xpath": ".//system.web/healthMonitoring/providers/add",
    "default": "5000",
    "recommended": "5000",
    "comparison_type": "<="
},
{
    "conftype": "web.config",
    "name": "@maxSizeForSimpleMessage",
    "xpath": [".//system.web/healthMonitoring/providers/add[@name=\"SimpleMailWebEventProvider\"]", ".//system.web/healthMonitoring/providers/add[@name=\"TemplateMailWebEventProvider\"]"],
    "default": "1024",
    "recommended": "1024",
    "comparison_type": "<="
},
[
{
    "conftype": "web.config",
    "name": "@allowOverride",
    "xpath": ".//location",
    "default": "true",
    "recommended": "true",
    "not_recommended": "false"
},
{
    "conftype": "web.config",
    "name": "@level",
    "xpath": ".//location[@allowOverride=\"false\"]/system.web/trust",
    "default": "Full",
    "recommended": ["Medium", "Low", "Minimal"]
}
],
{
    "conftype": "web.config",
    "name": "@maxEventDetailLength",
    "xpath": ".//system.web/healthMonitoring/providers/add[@name=\"SqlWebEventProvider\"]",
    "default": "5000",
    "recommended": "5000",
    "comparison_type": "<="
},
[
{
    "conftype": "web.config",
    "name": "@name",
    "xpath": ".//system.web/membership/providers/add",
    "default": "",
    "recommended": "",
    "not_recommended": "Sql",
    "comparison_type": "in"
},
{
    "conftype": "web.config",
    "name": "@minRequiredPasswordLength",
    "xpath": ".//system.web/membership/providers/add",
    "default": "7",
    "recommended": "7",
    "comparison_type": ">="
}
],
[
{
    "conftype": "web.config",
    "name": "@name",
    "xpath": ".//system.web/membership/providers/add",
    "default": "",
    "recommended": "",
    "not_recommended": "Sql",
    "comparison_type": "in"
},
{
    "conftype": "web.config",
    "name": "@minRequiredNonalphanumericCharacters",
    "xpath": ".//system.web/membership/providers/add",
    "default": "1",
    "recommended": "1",
    "comparison_type": ">="
}
],
[
{
    "conftype": "web.config",
    "name": "@mode",
    "xpath": ".//system.web/sessionState",
    "default": "InProc",
    "recommended": "Off",
    "not_recommended": "SQLServer"
},
{
    "conftype": "web.config",
    "name": "CipherValue[@sessionState]",
    "xpath": ".//system.web/sessionState/EncryptedData/CipherData",
    "default": "",
    "recommended": "encrypted data",
    "not_recommended": ""
}
],
[
{
    "conftype": "web.config",
    "name": "@password",
    "xpath": ".//system.web/authentication[@mode=\"Forms\"]/forms/credentials/user",
    "default": "",
    "recommended": "do not use"
},
{
    "conftype": "web.config",
    "name": "@name[@credentials]",
    "xpath": ".//system.web/authentication[@mode=\"Forms\"]/forms/credentials/user",
    "default": "",
    "recommended": ["do not use", ""]
}
],
[
{
    "conftype": "web.config",
    "name": "@password",
    "xpath": ".//system.web/identity[@impersonate=\"true\"]",
    "default": "",
    "recommended": "encrypted data",
    "comparison_type": "regexp",
    "regexp": "^(registry:).*"
},
{
    "conftype": "web.config",
    "name": "@userName[@identity]",
    "xpath": ".//system.web/identity[@impersonate=\"true\"]",
    "default": "",
    "recommended": "encrypted data",
    "comparison_type": "regexp",
    "regexp": ["^(registry:).*", "^$"]
}
],
{
    "conftype": "web.config",
    "name": "@requireSSL[@authentication]",
    "xpath": ".//system.web/authentication[@mode=\"Forms\"]/forms",
    "default": "false",
    "recommended": "true"
},
{
    "conftype": "web.config",
    "name": "@cookieless",
    "xpath": ".//system.web/authentication[@mode=\"Forms\"]/forms",
    "default": "UseDeviceProfile",
    "recommended": "UseCookies"
},
{
    "conftype": "web.config",
    "name": "@enableCrossAppRedirects",
    "xpath": ".//system.web/authentication[@mode=\"Forms\"]/forms",
    "default": "false",
    "recommended": "false"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "400"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "401"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "403"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "404"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "405"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "408"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "411"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "413"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "414"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "500"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "502"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "503"
},
{
    "conftype": "web.config",
    "name": "@statusCode",
    "xpath": ".//system.web/customErrors/error",
    "default": "",
    "recommended": "504"
},
{
    "conftype": "web.config",
    "name": "@value[@AccessControlAllowOriginHeader]",
    "xpath": ".//system.webServer/httpProtocol/customHeaders/add[@name=\"Access-Control-Allow-Origin\"]",
    "default": "",
    "recommended": "",
    "not_recommended": "*"
}
]
