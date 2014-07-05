# -*- mode: python -*-
a = Analysis(['heartbeat.py'],
             pathex=['e:\\mabodev\\mabo-radar\\py'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='heartbeat.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
