[{
    "conftype": "machine.config",
    "name": "@passwordFormat",
    "xpath": ".//system.web/credentials",
    "default": "SHA1",
    "recommended": "SHA1"
},
{
    "conftype": "machine.config",
    "name": "@retail",
    "xpath": ".//system.web/deployment",
    "default": "false",
    "recommended": "true"
},
{
    "conftype": "machine.config",
    "name": "@decryption",
    "xpath": ".//system.web/machineKey",
    "default": "Auto",
    "recommended": ["Auto", "AES"]
},
{
    "conftype": "machine.config",
    "name": "@decryptionKey",
    "xpath": ".//system.web/machineKey",
    "default": "AutoGenerate,IsolateApps",
    "recommended": "AutoGenerate,IsolateApps"
},
{
    "conftype": "machine.config",
    "name": "@validation",
    "xpath": ".//system.web/machineKey",
    "default": "HMACSHA256",
    "recommended": "AES"
},
{
    "conftype": "machine.config",
    "name": "@validationKey",
    "xpath": ".//system.web/machineKey",
    "default": "AutoGenerate,IsolateApps",
    "recommended": "AutoGenerate,IsolateApps"
},
[
    {
        "conftype": "machine.config",
        "name": "@retail",
        "xpath": ".//system.web/deployment",
        "default": "false",
        "recommended": "true"
    },
    {
        "conftype": "machine.config",
        "name": "@debug",
        "xpath": ".//system.web/compilation",
        "default": "false",
        "recommended": "false"
    }
]
]