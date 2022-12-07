import { incode, decode } from "./encrypt.js";
import { incodeByUnicode, decodeByUnicode } from "./unicodeEncrypt.js";
export { incode, decode, incodeByUnicode, decodeByUnicode}

import {createRequire} from "module"
const require = createRequire(import.meta.url);
const fs =  require("fs");
const path = require("path");
const args = require("minimist")(process.argv.slice(2));
const readline = require('readline');
let r1 = readline.createInterface({
    input:process.stdin,
    output:process.stdout
});

// 1.读取参数
if (!args["f"]) {
    console.log("node index.js -f <zero_txt>");
    process.exit(-1);
} else {
    // var file_path = path.join(process.cwd(), args["f"]);
    var file_path = path.join(args["f"]);
}

// 2.读取文件解开零宽
fs.readFile(file_path, "utf-8", function(err, data){
    if (err == null) {
        console.log(decodeByUnicode(data));
    }
})

// 3.阻塞
r1.question("", function(anwser) {
    r1.close();
})
