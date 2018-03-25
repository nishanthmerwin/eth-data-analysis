
var Web3 = require('web3');
var fs = require("fs");
var jsonfile = require('jsonfile');
var sleep = require("sleep");

var url1 = "wss://mainnet.infura.io/ws";
var web3 = new Web3(url1);


var test = web3.toAscii("0x6db432dc5e660b");

console.log(test);


