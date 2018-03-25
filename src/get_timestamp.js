
var Web3 = require('web3');
var fs = require("fs");
var jsonfile = require('jsonfile');
var sleep = require("sleep");

var url1 = "wss://mainnet.infura.io/ws";
var web3 = new Web3(url1);

web3.eth.net.isListening()
.then(() => console.log('is connected'))
.catch(e => console.log('Wow. Something went wrong'));

for (i=1; i<100; i++){
	web3.eth.getBlock(i).then(function(resp){
		console.log(resp.timestamp);
	})
	sleep.msleep(200);
}


/*
var start_block = 5218685;
web3.eth.getBlock("latest")
	.then(function(block){
		last_block = block.number
		console.log(last_block);
		get_transactions(start_block, block.number, contract);
	});
*/
