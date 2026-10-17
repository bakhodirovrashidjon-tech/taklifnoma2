from PIL import Image
import os
src=Image.open('icon-source.png').convert('RGB')
for d,s in {'mdpi':48,'hdpi':72,'xhdpi':96,'xxhdpi':144,'xxxhdpi':192}.items():
    for n in ('ic_launcher.png','ic_launcher_round.png','ic_launcher_foreground.png'):
        p=f'android/app/src/main/res/mipmap-{d}/{n}'
        if os.path.exists(p):
            k=s if n!='ic_launcher_foreground.png' else int(s*108/48)
            src.resize((k,k)).save(p)
for f in ('ic_launcher.xml','ic_launcher_round.xml'):
    p='android/app/src/main/res/mipmap-anydpi-v26/'+f
    if os.path.exists(p): os.remove(p)
