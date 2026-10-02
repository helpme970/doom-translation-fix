function translation() {
    switch(kex.CvarGet("g_language", 0)) {
        case "en":
            return 0;
            break;
        case "fr":
            return 1;
            break;
        case "de":
            return 2;
            break;
        case "es":
            return 3;
            break;
        case "es-mx":
            return 4;
            break;
        case "it":
            return 5;
            break;
        case "ru":
            return 6;
            break;
        case "ja":
            return 7;
            break;
        case "pl":
            return 8;
            break;
        case "pt-BR":
            return 9;
            break;
        case "ko":
            return 10;
            break;
        case "zh-CN":
            return 11;
            break;
        case "zh-TW":
            return 12;
            break;
        default:
            return "error";
    }
}

const changeBinding = ["Change Binding", "", "Zuordnung ändern", "", "", "", "", "", "", "", "", "", ""];
const clear = ["Clear", "", "Entfernen", "", "", "", "", "", "", "", "", "", ""]
