import * as fs from 'fs';

const args = process.argv.slice(2);

function check(arg){
    if (fs.exists(arg) === true){
        if (fs.isDirectory(arg)) {
            return(`'${arg}' jest katalogiem`);
        }
        else{
            return(`'${arg}' jest plikiem, a jego zawartością jest:\n${fs.readFileSync(arg, 'utf8')}`);
        }
    }
    else{
        return `Plik '${arg}' nie istnieje`
    }
}

args.forEach(arg =>{
    console.log(check(arg));
});
