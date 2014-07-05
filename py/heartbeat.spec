# -*- mode: python -*-
a = Analysis(['heartbeat.py'],
             pathex=['e:\\mabodev\\mabo-radar\\py'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='heartbeat.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='favicon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='heartbeat')
