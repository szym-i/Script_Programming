"use strict";
var expect = chai.expect;

function isNumber(char) {
	return /^\d$/.test(char);
}

function isLetter(char) {
  return /[a-z]/.test(char);
}

function cyfry(napis){
  var result = 0;
  for (let i = 0; i < napis.length; i++){
    if (isNumber(napis[i]) === true){
      result += Number(napis[i]);
    }
  }
  return result;
}
function litery(napis){
  var result = 0;
  for (let i = 0; i < napis.length; i++){
    if (isLetter(napis[i]) === true){
      result += 1;
    }
  }
  return result;
}
function suma(napis){
  let number = parseInt(napis);

  if (!isNaN(number)){
    total += number;
  }
  return total;
}

describe('The cyfry() function', function() {
  it('Returns 6 for 222', function() {
    expect(cyfry('111')).to.equal(3);
  });
  it('Returns 0 for aaa', function() {
    expect(cyfry('aaa')).to.equal(0);
  });
  it('Returns 2 for 11aa', function() {
    expect(cyfry('11aa')).to.equal(2);
  });
  it('Returns 15 for a3453a', function() {
    expect(cyfry('a3453a')).to.equal(15);
  });
  it('Returns 0 for ""', function() {
    expect(cyfry('')).to.equal(0);
  });
});

describe('The litery() function', function() {
  it('Returns 0 for 111', function() {
    expect(litery('111')).to.equal(0);
  });
  it('Returns 3 for aaa', function() {
    expect(litery('aaa')).to.equal(3);
  });
  it('Returns 2 for 11aa', function() {
    expect(litery('11aa')).to.equal(2);
  });
  it('Returns 2 for a3453a', function() {
    expect(litery('a3453a')).to.equal(2);
  });
  it('Returns 0 for ""', function() {
    expect(cyfry('')).to.equal(0);
  });
});

let total = 0;
describe('The suma() function', function() {
  it('Returns 11 for 11aa', function() {
    expect(suma('11aa')).to.equal(11);
  });

  it('Returns 11 for aaa', function() {
    expect(suma('aaa')).to.equal(11);
  });

  it('Returns 122 for 111', function() {
    expect(suma('111')).to.equal(122);
  });

  it('Returns 122 for a3453a', function() {
    expect(suma('a345a')).to.equal(122);
  });
  it('Returns 122 for ""', function() {
    expect(suma('')).to.equal(122);
  });
});