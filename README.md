# doom-translation-fix
Fix hardcoded translations in Doom + Doom II

## Installation
1. Download the fixed translations from [here](https://github.com/helpme970/doom-translation-fix/releases/download/1.3/Common.kpf)
2. Put the downloaded file into the main game folder (e.g. C:\GOG Games\DOOM + DOOM II\)
3. Override the file if prompted
4. Enjoy the game

> If you find a translation bug or the fix does not work, please report it to me via the issue section.

|State|Image|
|-|-|
|Before|<img width="960" height="540" alt="Bildschirmfoto_20261004_191350" src="https://github.com/user-attachments/assets/09a51009-f979-42b7-a496-263ffd4875c1" />|
|After|<img width="960" height="540" alt="Bildschirmfoto_20261004_191434" src="https://github.com/user-attachments/assets/0771e2ed-9504-4c0b-826e-92a2fe75936a" />|

## Developer notes
### File
| File                  | Explanation                                                     |
|-----------------------|-----------------------------------------------------------------|
| index original.js     | original unmodified version                                     |
| index deobfuscated.js | `index original.js` deobfuscated, see JS Tools for the used tool|
| index fixed.js        | original file with the translation fix                          |
| owncode.js            | the code for the fix, that is applied to `index original.js` (deprecated)    |
| doom.py               | Python program to patch the index.js                            |

### JS Tools
index.js taken from <path-to-game>/Common.kpf/menu/

Tools used:
| Tool                    | Link                                     |
|-------------------------|------------------------------------------|
| Javascript deobfuscator | https://willnode.github.io/deobfuscator/ |
| Javascript compressor   | https://jscompressor.treblereel.dev/     |

### KPF
"KEX program file" or "KEX Pack File"

Zip-File compressed with Deflate or just stored without compression

Resources:
- https://www.doom64.com/structures/kpf/
- https://doomwiki.org/wiki/KPF
- https://doomwiki.org/wiki/Common.kpf
