# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Propuesta_I.py'],
             pathex=['C:\\Users\\Admin\\Documents\\Clases\\URIA\\Junio\\Semana_4\\Semana_4_Sesión_3\\Empaquetar_con_archivo_externo'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Propuesta_I',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )