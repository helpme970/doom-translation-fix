#!/bin/python3

########################
# Produce translations #
########################
translation1 = ["Change Binding", "Modifier", "Belegung ändern", "Cambiar", "Cambiar", "Cambia", "Изменить назначение", "解除", "Zmień przypisanie", "Alterar atribuição", "키 할당 변경", "更改键位绑定", "變更按鍵綁定"]
translation2 = ["Clear", "Supprimer", "Entfernen", "Borrar", "Borrar", "Cancella", "Удалить назначение", "変更", "Usuń przypisanie", "Remover", "키 할당 해제", "清除键位绑定", "清除按鍵綁定"]
languages = ["en", "fr", "de", "es", "\"es-mx\"", "it", "ru", "ja", "pl", "\"pt-BR\"", "ko", "\"zh-CN\"", "\"zh-TW\""]
translations = []

for i in range(len(translation1)):
    translations.append(f"{languages[i]}:" + "{" + f"change_binding:\"{translation1[i]}\",clear:\"{translation2[i]}\",")

for i in translations:
    print(i)

##################################
# produce stuff that is replaced #
##################################
orig =      ['"Change Binding"', '"Clear"', 'function s(){engine.on("InputCaptured",i),kex.CaptureNextInput(),t(!0),osiris.StartSound(t6.pistol)}', 'engine.on("MenuOpenButtonPressed",e=>rk("useGamepadHints",!e))']
replacement =   ['t("change_binding")', 't("clear")', 't=ir();function s(){engine.on("InputCaptured",i),kex.CaptureNextInput(),t(!0),osiris.StartSound(t6.pistol)}', 'engine.on("MenuOpenButtonPressed",e => {if(kex.GetGamepadType(0)=="unknown"||e == 0)a = 0;else a=1;rk("useGamepadHints", a);})']
# alt: 'engine.on("MenuOpenButtonPressed",e => {if (kex.GetGamepadType(0)=="unknown"||e == 0)a = 0;else a=1;rk("useGamepadHints", a);})'
# "keyboard" !== e.source
# "gamepad" == e.source

# add translations for replacement
for i in range(len(languages)):
    orig.append(f"{languages[i]}:"+"{")
    replacement.append(translations[i])

############################
# replace/patch javascript #
############################
txt = open("index.js", "r", encoding="utf-8").readlines()

found=0
for l in range(len(txt)):
    for i in range(len(orig)):
        if orig[i] in txt[l]:
            found += 1
            tmp = txt[l]
            print(f"found: {orig[i]} :: {replacement[i]}")
            txt[l] = txt[l].replace(orig[i], replacement[i])
            if tmp == txt[l]:
                print("Patch hat nicht funktioniert")

open("index.js", "w", encoding="utf-8").writelines(txt)
print("Successfully patched file")
print(f"{found}/{len(orig)} Patches applied")
