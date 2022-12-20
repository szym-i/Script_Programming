import * as fs from 'fs';

const args = process.argv.slice(2);

args.forEach(arg =>{
    if (fs.existsSync(arg) === true){
        if (fs.lstatSync(arg).isDirectory()) {
            console.log(`'${arg}' jest katalogiem`);
        }
        else{
            console.log(`'${arg}' jest plikiem, a jego zawartością jest:\n${fs.readFileSync(arg, 'utf8')}`);
        }
    }
    else{
        console.log(`Plik ${arg} nie istnieje`)
    }
});
