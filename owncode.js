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

const changeBinding = ["Change Binding", "Modifier", "Belegung ändern", "Cambiar", "Cambiar", "Cambia", "Изменить назначение", "解除", "Zmień przypisanie", "Alterar atribuição", "키 할당 변경", "更改键位绑定", "變更按鍵綁定"];
const clear = ["Clear", "Supprimer", "Entfernen", "Borrar", "Borrar", "Cancella", "Удалить назначение", "変更", "Usuń przypisanie", "Remover", "키 할당 해제", "清除键位绑定", "清除按鍵綁定"]
