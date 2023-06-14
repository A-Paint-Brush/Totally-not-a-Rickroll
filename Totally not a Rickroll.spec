# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py', 'Home_Page.py', 'Lyrics.py', 'Lyrics_Window.py', 'Path.py', 'Resize.py', 'Rickroll.py', 'Timer.py', 'Video.py'],
             pathex=[],
             binaries=[],
             datas=[(".\\Video\\*.mp4", "Video"), (".\\Sound\\*.wav", "Sound"),
             ("C:\\Users\\cliff\\envs\\video_env\\Lib\\site-packages\\imageio_ffmpeg\\*", "imageio_ffmpeg"),
             ("C:\\Users\\cliff\\envs\\video_env\\Lib\\site-packages\\imageio\\*", "imageio")],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='Totally not a Rickroll',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='NONE')
