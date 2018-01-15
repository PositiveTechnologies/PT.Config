# -*- mode: python -*-
import os

a = Analysis(['main.py'],
             hiddenimports=['xml.dom', 'xml.etree.ElementTree', 'chardet', 'json',
                            'configparser', 'nginxparser', 'lxml.etree', 'ply.lex', 'ply.yacc', 'wmi',
                            'lighttpd',],
             datas=[
                 ('*.js', 'inner_rules'),
                 ('.htaccess.js', 'inner_rules'),
             ],
             pathex=['C:\Python35\Lib'],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('../build', 'conf.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=True)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('../build/config')
               )
