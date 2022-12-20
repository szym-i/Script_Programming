import * as assert from 'assert';
import * as fs from 'fs';

function check(arg){
    if (fs.existsSync(arg) === true){
        if (fs.lstatSync(arg).isDirectory()) {
            return(`'${arg}' jest katalogiem`);
        }
        if (fs.lstatSync(arg).isFile()) {
            return(`'${arg}' jest plikiem, a jego zawartością jest:\n${fs.readFileSync(arg, 'utf8')}`);
        }
        else{
            return `'${arg}' istnieje ale nie wiem czym jest`
        }
    }
    else{
        return(`Plik '${arg}' nie istnieje`)
    }
}

describe('exists', function () {
    it('file tekst.txt', function () {
        assert.strictEqual(check('tekst.txt'), `'tekst.txt' jest plikiem, a jego zawartością jest:\n12314\n31421\nsasa`)
    });
    it('dir .', function () {
         assert.strictEqual(check('.'), "'.' jest katalogiem")
    });
    it('dir /etc', function () {
         assert.strictEqual(check('/etc'), "'/etc' jest katalogiem")
    });
    it('not existing path', function () {
        assert.strictEqual(check('non-existing-path'), "Plik 'non-existing-path' nie istnieje")
    });
});