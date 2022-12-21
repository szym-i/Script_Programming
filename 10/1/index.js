import {Operation} from './module.js';

const args = process.argv.slice(2,4);

console.log(new Operation(Number(args.at(0)), Number(args.at(1))).sum());
