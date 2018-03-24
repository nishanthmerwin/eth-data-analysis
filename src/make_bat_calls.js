
var Web3 = require('web3');
var fs = require("fs");
var jsonfile = require('jsonfile');


var contr_addr = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"

var url1 = "wss://mainnet.infura.io/ws";
var web3 = new Web3(url1);

var contract_abi = JSON.parse(fs.readFileSync("../data/bat_abi.json"));
const contract = new web3.eth.Contract(contract_abi, contr_addr);

web3.eth.net.isListening()
.then(() => console.log('is connected'))
.catch(e => console.log('Wow. Something went wrong'));

start = process.argv[2];
end = process.argv[3];
outfile = process.argv[4];

console.log(start, end, outfile)

contract.getPastEvents('Transfer', {
	fromBlock: start,
	toBlock: end})
.then(function(events){
	//console.log(events);
	jsonfile.writeFileSync(outfile, events);
	console.log("DONE")
	process.exit()
});

/*
var start_block = 5218685;
web3.eth.getBlock("latest")
	.then(function(block){
		last_block = block.number
		console.log(last_block);
		get_transactions(start_block, block.number, contract);
	});
*/
