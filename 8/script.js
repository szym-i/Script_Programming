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
function suma(napis,sum){
  var num = '';
  for (let i = 0; i < napis.length; i++){
    if (isNumber(napis[i]) === true){
      num += napis[i];
    }
    else{
      break;
    }
  }
  return sum+Number(num);
}

describe('The cyfry() function', function() {
  it('Returns 6 for 222', function() {
    expect(cyfry('111')).to.equal(3);
  });
  it('Returns 2 for 11aa', function() {
    expect(cyfry('11aa')).to.equal(2);
  });
  it('Returns 15 for a3453a', function() {
    expect(cyfry('a3453a')).to.equal(15);
  });
});

describe('The litery() function', function() {
  it('Returns 0 for 111', function() {
    expect(litery('111')).to.equal(0);
  });
  it('Returns 2 for 11aa', function() {
    expect(litery('11aa')).to.equal(2);
  });
  it('Returns 2 for a3453a', function() {
    expect(litery('a3453a')).to.equal(2);
  });
});

describe('The suma() function', function() {
  let sum = 0;

  sum = suma('11aa',sum)
  it('Returns 2 for 11aa', function() {
    expect(sum).to.equal(122);
  });

  sum = suma('111',sum)
  it('Returns 0 for 111', function() {
    expect(sum).to.equal(122);
  });

  sum = suma('a3453a',sum)
  it('Returns 2 for a3453a', function() {
    expect(sum).to.equal(122);
  });
});
