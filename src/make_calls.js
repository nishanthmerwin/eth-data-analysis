
var Web3 = require('web3');
var fs = require("fs");
var jsonfile = require('jsonfile');


var bunny_contract_address = "0x755eb14D2fefF2939EB3026f5CaD9D03775b9fF4";

var url1 = "wss://mainnet.infura.io/ws";
var web3 = new Web3(url1);

var contract_abi = JSON.parse(fs.readFileSync("../data/bunny_abi.json"));
const contract = new web3.eth.Contract(contract_abi, bunny_contract_address);

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
